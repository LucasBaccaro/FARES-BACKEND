"""
Servicio para buscar archivos en Google Drive
Permite buscar en múltiples carpetas específicas de Diego Fares
"""

import os
import json
from typing import List, Optional, Dict, Any
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Scopes necesarios para Google Drive API
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']


class DriveSearchService:
    def __init__(self):
        """Inicializar el servicio de Google Drive"""
        self.service = self._get_drive_service()

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
        """Crear y autenticar el servicio de Google Drive"""
        creds = None

        # Buscar token guardado
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)

        # Si no hay credenciales válidas, solicitar autorización
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                # Necesitarás crear credentials.json desde Google Cloud Console
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
                # Usar puerto específico y mostrar la URL
                creds = flow.run_local_server(port=8080,
                                            open_browser=True,
                                            access_type='offline',
                                            prompt='consent')

            # Guardar las credenciales para la próxima ejecución
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        return build('drive', 'v3', credentials=creds)

    def buscar_en_carpeta(self, query: str, carpeta_id: str) -> List[Dict]:
        """Buscar archivos en una carpeta específica"""
        try:
            # Construir query de búsqueda
            search_query = f"name contains '{query}' and parents in '{carpeta_id}'"

            print(f"DEBUG: Buscando en carpeta {carpeta_id} con query: {search_query}")

            # Ejecutar búsqueda
            results = self.service.files().list(
                q=search_query,
                pageSize=50,
                fields="nextPageToken, files(id, name, webViewLink, webContentLink, mimeType, size, modifiedTime)"
            ).execute()

            archivos = results.get('files', [])
            print(f"DEBUG: Encontrados {len(archivos)} archivos")

            # Formatear resultados
            archivos_formateados = []
            for archivo in archivos:
                archivos_formateados.append({
                    "id": archivo.get('id'),
                    "name": archivo.get('name'),
                    "view_link": archivo.get('webViewLink'),
                    "download_link": f"https://drive.google.com/file/d/{archivo.get('id')}/view",
                    "mime_type": archivo.get('mimeType'),
                    "size": archivo.get('size'),
                    "modified_time": archivo.get('modifiedTime')
                })

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

    def obtener_archivos_de_carpeta(self, carpeta_id: str, limite: int = 50) -> List[Dict]:
        """Obtener todos los archivos de una carpeta específica"""
        try:
            query = f"parents in '{carpeta_id}'"

            results = self.service.files().list(
                q=query,
                pageSize=limite,
                fields="nextPageToken, files(id, name, webViewLink, webContentLink, mimeType, size, modifiedTime)"
            ).execute()

            archivos = results.get('files', [])

            archivos_formateados = []
            for archivo in archivos:
                archivos_formateados.append({
                    "id": archivo.get('id'),
                    "name": archivo.get('name'),
                    "view_link": archivo.get('webViewLink'),
                    "download_link": f"https://drive.google.com/file/d/{archivo.get('id')}/view",
                    "mime_type": archivo.get('mimeType'),
                    "size": archivo.get('size'),
                    "modified_time": archivo.get('modifiedTime')
                })

            return archivos_formateados

        except Exception as error:
            print(f"Error obteniendo archivos: {error}")
            return []


# Instancia global del servicio
drive_service = DriveSearchService()