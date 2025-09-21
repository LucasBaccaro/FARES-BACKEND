"""
Script para eliminar TODOS los archivos del vector store de OpenAI
ATENCIÓN: Esta operación elimina los archivos completamente de OpenAI (no se pueden recuperar)
"""

import os
import time
from openai import OpenAI
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
VECTOR_STORE_ID = os.getenv("VECTOR_STORE_ID")


def confirmar_eliminacion():
    """Pide confirmación al usuario antes de eliminar archivos"""
    print("⚠️  ADVERTENCIA: Esta operación eliminará TODOS los archivos del vector store")
    print("⚠️  Los archivos se eliminarán PERMANENTEMENTE de OpenAI")
    print("⚠️  Esta acción NO se puede deshacer")
    print()

    respuesta = input("¿Estás SEGURO de que quieres continuar? Escribe 'ELIMINAR' para confirmar: ")
    return respuesta == "ELIMINAR"


def eliminar_archivo_del_vector_store(file_id):
    """Elimina un archivo específico del vector store"""
    try:
        client.vector_stores.files.delete(
            vector_store_id=VECTOR_STORE_ID,
            file_id=file_id
        )
        return True
    except Exception as e:
        print(f"❌ Error eliminando {file_id} del vector store: {e}")
        return False


def eliminar_archivo_de_openai(file_id):
    """Elimina un archivo completamente de OpenAI"""
    try:
        client.files.delete(file_id)
        return True
    except Exception as e:
        print(f"❌ Error eliminando {file_id} de OpenAI: {e}")
        return False


def borrar_todos_los_archivos():
    """Elimina todos los archivos del vector store y de OpenAI"""

    print("🗑️  ELIMINACIÓN MASIVA DE ARCHIVOS")
    print("=" * 50)

    try:
        # Primero listar todos los archivos
        print("📋 Obteniendo lista de archivos...")
        archivos = client.vector_stores.files.list(VECTOR_STORE_ID)
        lista_archivos = list(archivos)

        if not lista_archivos:
            print("✅ No hay archivos para eliminar")
            return

        print(f"📊 Se encontraron {len(lista_archivos)} archivos para eliminar")

        # Mostrar algunos nombres de archivos
        print("\nPrimeros archivos que se eliminarán:")
        for i, archivo in enumerate(lista_archivos[:5], 1):
            try:
                detalles = client.files.retrieve(archivo.id)
                nombre = detalles.filename
            except:
                nombre = "Nombre desconocido"
            print(f"  {i}. {nombre}")

        if len(lista_archivos) > 5:
            print(f"  ... y {len(lista_archivos) - 5} archivos más")

        print()

        # Pedir confirmación
        if not confirmar_eliminacion():
            print("❌ Operación cancelada")
            return

        print("\n🚀 Iniciando eliminación...")
        archivos_eliminados = 0

        # Eliminar cada archivo
        for i, archivo in enumerate(lista_archivos, 1):
            print(f"[{i}/{len(lista_archivos)}] Eliminando {archivo.id}...")

            # Eliminar del vector store
            if eliminar_archivo_del_vector_store(archivo.id):
                # Eliminar completamente de OpenAI
                if eliminar_archivo_de_openai(archivo.id):
                    archivos_eliminados += 1
                    print(f"✅ Eliminado completamente: {archivo.id}")
                else:
                    print(f"⚠️  Eliminado del vector store pero falló eliminación total: {archivo.id}")

            # Pausa pequeña para evitar límites de velocidad
            time.sleep(0.3)

        print("\n" + "=" * 50)
        print(f"🎉 Eliminación completada!")
        print(f"✅ Archivos eliminados exitosamente: {archivos_eliminados}/{len(lista_archivos)}")

    except Exception as e:
        print(f"❌ Error durante la eliminación: {e}")


if __name__ == "__main__":
    borrar_todos_los_archivos()