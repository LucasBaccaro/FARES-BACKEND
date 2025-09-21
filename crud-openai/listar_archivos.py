"""
Script para listar todos los archivos en el vector store de OpenAI
Muestra la cantidad total y detalles de cada archivo
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
VECTOR_STORE_ID = os.getenv("VECTOR_STORE_ID")


def listar_archivos_vector_store():
    """Lista todos los archivos del vector store y muestra la cantidad total"""

    print(f"📁 Listando archivos en vector store: {VECTOR_STORE_ID}")
    print("=" * 60)

    try:
        # Obtener lista de archivos del vector store
        archivos = client.vector_stores.files.list(VECTOR_STORE_ID)
        lista_archivos = list(archivos)

        if not lista_archivos:
            print("❌ No hay archivos en el vector store")
            return

        print(f"📊 TOTAL DE ARCHIVOS: {len(lista_archivos)}")
        print("-" * 60)

        # Mostrar detalles de cada archivo
        for i, archivo in enumerate(lista_archivos, 1):
            try:
                # Obtener detalles del archivo
                detalles = client.files.retrieve(archivo.id)
                nombre = detalles.filename
                tamaño = detalles.bytes
                fecha_creacion = detalles.created_at

            except Exception:
                nombre = "Nombre desconocido"
                tamaño = 0
                fecha_creacion = "Fecha desconocida"

            print(f"{i:3}. Archivo: {nombre}")
            print(f"     ID: {archivo.id}")
            print(f"     Tamaño: {tamaño:,} bytes")
            print(f"     Estado: {archivo.status}")
            print(f"     Creado: {fecha_creacion}")
            print()

        print("=" * 60)
        print(f"✅ Listado completado. Total: {len(lista_archivos)} archivos")

    except Exception as e:
        print(f"❌ Error al listar archivos: {e}")


if __name__ == "__main__":
    listar_archivos_vector_store()