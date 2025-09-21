"""
Servicio para manejar el chat con OpenAI Assistant
Incluye extracción de citas y matching con fuentes locales
"""

import json
import os
import time
import logging
from typing import List, Optional
from openai import OpenAI
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configurar logging
logger = logging.getLogger(__name__)


class Citation:
    def __init__(self, file_id: str, file_name: str, quote: str, text: str, download_link: Optional[str] = None):
        self.file_id = file_id
        self.file_name = file_name
        self.quote = quote
        self.text = text
        self.download_link = download_link


class ChatResponse:
    def __init__(self, thread_id: str, assistant_message: str, citations: List[Citation]):
        self.thread_id = thread_id
        self.assistant_message = assistant_message
        self.citations = citations


class SourceLinker:
    def __init__(self, json_path: str = "json.json"):
        """Cargar archivo JSON con referencias a fuentes"""
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                self.reference_data = json.load(f)

            # Crear diccionario de lookup para búsqueda O(1)
            self.title_to_link = {}
            valid_items = 0
            invalid_items = 0

            for i, item in enumerate(self.reference_data):
                if isinstance(item, dict) and "titulo" in item and "link" in item:
                    self.title_to_link[item["titulo"]] = item["link"]
                    valid_items += 1
                else:
                    logger.warning(f"Invalid item at index {i}: {item}")
                    invalid_items += 1

            logger.info(f"Loaded {len(self.reference_data)} total items, {valid_items} valid, {invalid_items} invalid")

        except FileNotFoundError:
            logger.error(f"Reference file not found: {json_path}")
            self.reference_data = []
            self.title_to_link = {}
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON: {e}")
            self.reference_data = []
            self.title_to_link = {}

    def get_download_link(self, filename: str) -> Optional[str]:
        """Obtener link de descarga para un archivo específico"""
        return self.title_to_link.get(filename)


class OpenAIService:
    def __init__(self):
        """Inicializar servicio de OpenAI"""
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.assistant_id = os.getenv("ASSISTANT_ID")
        self.source_linker = SourceLinker()

        if not self.assistant_id:
            raise ValueError("ASSISTANT_ID no configurado en variables de entorno")

        logger.info(f"OpenAI service initialized with assistant: {self.assistant_id}")

    def chat(self, message: str, thread_id: Optional[str] = None) -> ChatResponse:
        """
        Enviar mensaje al asistente y obtener respuesta con citas
        """
        try:
            # Crear thread o usar existente
            if thread_id is None:
                thread = self.client.beta.threads.create()
                thread_id = thread.id
                logger.info(f"Created new thread: {thread_id}")
            else:
                logger.info(f"Using existing thread: {thread_id}")

            # Enviar mensaje
            self.client.beta.threads.messages.create(
                thread_id=thread_id,
                role="user",
                content=message
            )

            # Ejecutar asistente
            run = self.client.beta.threads.runs.create(
                thread_id=thread_id,
                assistant_id=self.assistant_id
            )

            logger.info(f"Started run: {run.id}")

            # Esperar completación
            max_iterations = 60
            iterations = 0

            while iterations < max_iterations:
                run_status = self.client.beta.threads.runs.retrieve(
                    thread_id=thread_id,
                    run_id=run.id
                )

                if run_status.status in ["completed", "failed", "cancelled"]:
                    break

                time.sleep(1)
                iterations += 1

            if iterations >= max_iterations:
                raise Exception("Request timeout - assistant took too long to respond")

            if run_status.status == "failed":
                raise Exception(f"Run failed: {run_status.last_error}")

            if run_status.status != "completed":
                raise Exception(f"Run ended with unexpected status: {run_status.status}")

            # Obtener respuesta
            messages = self.client.beta.threads.messages.list(thread_id)
            assistant_message = next(
                (m for m in messages.data if m.role == "assistant" and getattr(m, 'run_id', None) == run.id),
                None
            )

            if not assistant_message:
                raise Exception("No assistant response found")

            # Procesar citas
            citations = []
            response_text = ""

            if assistant_message and assistant_message.content:
                text_content = assistant_message.content[0]
                if hasattr(text_content, 'text'):
                    response_text = text_content.text.value

                    # Extraer annotations (citas)
                    if hasattr(text_content.text, 'annotations') and text_content.text.annotations:
                        for i, annotation in enumerate(text_content.text.annotations):
                            if hasattr(annotation, 'file_citation'):
                                file_citation = annotation.file_citation

                                # Obtener nombre del archivo
                                try:
                                    file_info = self.client.files.retrieve(file_citation.file_id)
                                    file_name = file_info.filename
                                except Exception:
                                    file_name = f"Archivo {file_citation.file_id[-8:]}"

                                # Reemplazar marcador en el texto
                                original_marker = annotation.text
                                new_marker = f"[{i + 1}]"
                                response_text = response_text.replace(original_marker, new_marker)

                                # Obtener link de descarga
                                download_link = self.source_linker.get_download_link(file_name)

                                citations.append(Citation(
                                    file_id=file_citation.file_id,
                                    file_name=file_name,
                                    quote=getattr(file_citation, 'quote', ''),
                                    text=new_marker,
                                    download_link=download_link
                                ))

            logger.info(f"Generated response with {len(citations)} citations")

            return ChatResponse(
                thread_id=thread_id,
                assistant_message=response_text,
                citations=citations
            )

        except Exception as e:
            logger.error(f"Error in chat: {str(e)}")
            raise


# Instancia global del servicio
openai_service = OpenAIService()