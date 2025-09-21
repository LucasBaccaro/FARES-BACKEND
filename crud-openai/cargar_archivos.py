"""
Script para cargar TODOS los archivos de una carpeta específica al vector store de OpenAI
Sube archivos de texto (.txt, .md, .pdf, .docx) de forma masiva
"""

import os
import time
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
VECTOR_STORE_ID = os.getenv("VECTOR_STORE_ID")

# Extensiones de archivo permitidas
EXTENSIONES_PERMITIDAS = ['.txt', '.md', '.pdf', '.docx', '.doc', '.rtf']


def obtener_archivos_de_carpeta(ruta_carpeta):
    """Obtiene todos los archivos válidos de la carpeta especificada"""

    carpeta = Path(ruta_carpeta)

    if not carpeta.exists():
        raise ValueError(f"❌ La carpeta no existe: {ruta_carpeta}")

    if not carpeta.is_dir():
        raise ValueError(f"❌ La ruta no es una carpeta: {ruta_carpeta}")

    archivos = []

    # Buscar archivos con extensiones permitidas (incluyendo subcarpetas)
    for extension in EXTENSIONES_PERMITIDAS:
        archivos.extend(carpeta.glob(f"**/*{extension}"))

    return sorted(archivos)


def subir_archivo_a_openai(ruta_archivo):
    """Sube un archivo individual a OpenAI"""

    try:
        print(f"📤 Subiendo: {ruta_archivo.name}")

        with open(ruta_archivo, 'rb') as archivo:
            respuesta = client.files.create(
                file=archivo,
                purpose="assistants"
            )

        print(f"✅ Subido a OpenAI: {ruta_archivo.name} -> {respuesta.id}")
        return respuesta.id

    except Exception as e:
        print(f"❌ Error subiendo {ruta_archivo.name}: {e}")
        return None


def agregar_archivos_al_vector_store(lista_file_ids, tamaño_lote=20):
    """Agrega archivos al vector store en lotes para mejor rendimiento"""

    print(f"\n📁 Agregando {len(lista_file_ids)} archivos al vector store {VECTOR_STORE_ID}")

    # Procesar en lotes
    for i in range(0, len(lista_file_ids), tamaño_lote):
        lote = lista_file_ids[i:i + tamaño_lote]

        try:
            print(f"📦 Procesando lote {i//tamaño_lote + 1}: {len(lote)} archivos")

            # Crear lote en el vector store
            respuesta_lote = client.vector_stores.file_batches.create(
                vector_store_id=VECTOR_STORE_ID,
                file_ids=lote
            )

            print(f"✅ Lote creado: {respuesta_lote.id}")

            # Esperar a que el lote se complete
            while True:
                estado_lote = client.vector_stores.file_batches.retrieve(
                    vector_store_id=VECTOR_STORE_ID,
                    batch_id=respuesta_lote.id
                )

                completados = estado_lote.file_counts.completed
                total = len(lote)

                print(f"⏳ Estado del lote: {estado_lote.status} ({completados}/{total} archivos)")

                if estado_lote.status == 'completed':
                    print(f"✅ Lote completado exitosamente")
                    break
                elif estado_lote.status == 'failed':
                    print(f"❌ Lote falló: {respuesta_lote.id}")
                    break

                time.sleep(3)  # Esperar 3 segundos antes de verificar de nuevo

        except Exception as e:
            print(f"❌ Error procesando lote: {e}")

        # Pausa entre lotes
        time.sleep(1)


def cargar_carpeta_completa():
    """Función principal para cargar todos los archivos de una carpeta"""

    print("📂 CARGA MASIVA DE ARCHIVOS AL VECTOR STORE")
    print("=" * 60)

    # Solicitar ruta de la carpeta
    ruta_carpeta = 'C:\\Users\\Lucas\\Downloads\\TEXTUALES FARES -20250915T180239Z-1-001\\TEXTUALES FARES'

    print(f"\n📁 Carpeta seleccionada: {ruta_carpeta}")
    print(f"🎯 Vector store destino: {VECTOR_STORE_ID}")

    try:
        # Obtener lista de archivos
        archivos = obtener_archivos_de_carpeta(ruta_carpeta)

        if not archivos:
            print("❌ No se encontraron archivos válidos en la carpeta")
            print(f"Extensiones buscadas: {', '.join(EXTENSIONES_PERMITIDAS)}")
            return

        print(f"\n📊 Se encontraron {len(archivos)} archivos para subir")

        # Mostrar algunos ejemplos
        print("\nPrimeros archivos que se subirán:")
        for i, archivo in enumerate(archivos[:10], 1):
            print(f"  {i}. {archivo.name}")

        if len(archivos) > 10:
            print(f"  ... y {len(archivos) - 10} archivos más")

        # Pedir confirmación
        confirmar = input(f"\n¿Proceder con la subida de {len(archivos)} archivos? (s/n): ")
        if confirmar.lower() not in ['s', 'si', 'yes', 'y']:
            print("❌ Operación cancelada")
            return

        # Subir archivos a OpenAI
        print("\n" + "="*60)
        print("📤 SUBIENDO ARCHIVOS A OPENAI")
        print("="*60)

        file_ids_subidos = []

        for archivo in archivos:
            file_id = subir_archivo_a_openai(archivo)
            if file_id:
                file_ids_subidos.append(file_id)
            time.sleep(0.5)  # Pausa para evitar límites de velocidad

        # Resumen de subida
        print(f"\n📊 RESUMEN DE SUBIDA:")
        print(f"  📁 Total de archivos: {len(archivos)}")
        print(f"  ✅ Subidos exitosamente: {len(file_ids_subidos)}")
        print(f"  ❌ Fallaron: {len(archivos) - len(file_ids_subidos)}")

        if not file_ids_subidos:
            print("\n❌ No se subieron archivos. Proceso terminado.")
            return

        # Agregar archivos al vector store
        print("\n" + "="*60)
        print("📁 AGREGANDO ARCHIVOS AL VECTOR STORE")
        print("="*60)

        agregar_archivos_al_vector_store(file_ids_subidos)

        print(f"\n🎉 ¡PROCESO COMPLETADO!")
        print(f"✅ {len(file_ids_subidos)} archivos agregados al vector store {VECTOR_STORE_ID}")

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    cargar_carpeta_completa()