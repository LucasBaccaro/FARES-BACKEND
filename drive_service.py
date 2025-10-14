"""
Servicio para buscar archivos en Google Drive
Permite buscar en múltiples carpetas específicas de Diego Fares
"""

import os
import json
from typing import List, Optional, Dict, Any
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dotenv import load_dotenv
from openai_service import SourceLinker

# Cargar variables de entorno
load_dotenv()

# Scopes necesarios para Google Drive API
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']


class DriveSearchService:
    def __init__(self):
        """Inicializar el servicio de Google Drive"""
        self.service = self._get_drive_service()
        self.source_linker = SourceLinker()

        # Configuración de carpetas desde variables de entorno
        self.carpetas = {
            'todas': os.getenv('GOOGLE_DRIVE_PARENT_FOLDER_ID'),
            'articulos': os.getenv('GOOGLE_DRIVE_ARTICULOS_ID'),
            'articulos_revistas': os.getenv('GOOGLE_DRIVE_ARTICULOS_REVISTAS_ID'),
            'audios': os.getenv('GOOGLE_DRIVE_AUDIOS_ID'),
            'contemplaciones': os.getenv('GOOGLE_DRIVE_CONTEMPLACIONES_ID'),
            'libros': os.getenv('GOOGLE_DRIVE_LIBROS_ID'),
            'videos': os.getenv('GOOGLE_DRIVE_VIDEOS_ID')
        }

        # DEBUG: Mostrar valores cargados
        print("DEBUG: Variables de entorno cargadas:")
        for nombre, valor in self.carpetas.items():
            print(f"  {nombre}: {valor}")

    def _get_drive_service(self):
        """Crear y autenticar el servicio de Google Drive usando Service Account"""

        # Primero intentar usar Service Account (para Railway)
        service_account_info = os.getenv('GOOGLE_SERVICE_ACCOUNT_JSON')
        if service_account_info:
            try:
                # Parsear el JSON desde variable de entorno
                service_account_data = json.loads(service_account_info)
                credentials = service_account.Credentials.from_service_account_info(
                    service_account_data, scopes=SCOPES
                )
                print("OK: Usando Service Account desde variable de entorno")
                return build('drive', 'v3', credentials=credentials)
            except Exception as e:
                print(f"ERROR: Error con Service Account: {e}")

        # Fallback: buscar archivo service-account.json local
        if os.path.exists('service-account.json'):
            try:
                credentials = service_account.Credentials.from_service_account_file(
                    'service-account.json', scopes=SCOPES
                )
                print("OK: Usando Service Account desde archivo local")
                return build('drive', 'v3', credentials=credentials)
            except Exception as e:
                print(f"ERROR: Error con archivo Service Account: {e}")

        # Último fallback: OAuth (solo para desarrollo local)
        print("WARNING: Service Account no encontrado, usando OAuth (solo desarrollo local)")
        from google.auth.transport.requests import Request
        from google.oauth2.credentials import Credentials
        from google_auth_oauthlib.flow import InstalledAppFlow

        creds = None
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                if not os.path.exists('credentials.json'):
                    raise Exception("ERROR: No se encontro credentials.json para OAuth")

                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
                creds = flow.run_local_server(port=8080, open_browser=True)

            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        return build('drive', 'v3', credentials=creds)

    def _format_file_response(self, archivo: Dict) -> Dict:
        """Formatear un archivo individual, reemplazando el nombre con el título si se encuentra."""
        drive_filename = archivo.get('name')
        drive_filename_base, _ = os.path.splitext(drive_filename)
        
        source_info = self.source_linker.get_source_info(drive_filename_base) if hasattr(self, 'source_linker') else None
        
        display_name = source_info.get('title') if source_info and source_info.get('title') else drive_filename

        return {
            "id": archivo.get('id'),
            "name": display_name,
            "view_link": archivo.get('webViewLink'),
            "download_link": f"https://drive.google.com/file/d/{archivo.get('id')}/view",
            "mime_type": archivo.get('mimeType'),
            "size": archivo.get('size'),
            "modified_time": archivo.get('modifiedTime')
        }

    def buscar_en_carpeta(self, query: str, carpeta_id: str) -> List[Dict]:
        """Buscar archivos en una carpeta específica"""
        try:
            # Construir query de búsqueda
            search_query = f"parents in '{carpeta_id}'"
            if query and query != '*':
                search_query += f" and fullText contains '{query}'"

            print(f"DEBUG: Buscando en carpeta {carpeta_id} con query: {search_query}")

            # Ejecutar búsqueda con paginación
            archivos = []
            page_token = None
            while True:
                results = self.service.files().list(
                    q=search_query,
                    pageSize=100,
                    fields="nextPageToken, files(id, name, webViewLink, webContentLink, mimeType, size, modifiedTime)",
                    pageToken=page_token
                ).execute()

                archivos.extend(results.get('files', []))
                page_token = results.get('nextPageToken', None)
                if page_token is None:
                    break
            print(f"DEBUG: Encontrados {len(archivos)} archivos")

            # Formatear resultados
            archivos_formateados = [self._format_file_response(archivo) for archivo in archivos]

            return archivos_formateados

        except HttpError as error:
            print(f"Error en Google Drive API: {error}")
            return []
        except Exception as error:
            print(f"Error inesperado: {error}")
            return []

    def buscar_en_todas_las_carpetas(self, query: str) -> Dict[str, List[Dict]]:
        """Buscar en todas las carpetas configuradas"""
        resultados = {}

        for nombre_carpeta, carpeta_id in self.carpetas.items():
            if carpeta_id and nombre_carpeta != 'todas':  # Omitir la carpeta padre
                print(f"Buscando en {nombre_carpeta}...")
                archivos = self.buscar_en_carpeta(query, carpeta_id)
                if archivos:
                    resultados[nombre_carpeta] = archivos

        return resultados

        def listar_carpetas_disponibles(self) -> Dict[str, str]:

            """Devolver las carpetas configuradas"""

            print(f"DEBUG: Carpetas cargadas: {self.carpetas}")

            return {k: v for k, v in self.carpetas.items() if v and v != 'None'}


# Instancia global del servicio
drive_service = DriveSearchService()