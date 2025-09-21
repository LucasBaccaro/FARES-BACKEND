# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a FastAPI backend that integrates an OpenAI Assistant with Google Drive search functionality for Diego Fares content. The API provides chat capabilities with automatic citation extraction and Google Drive file search across specific folders.

## Architecture

**Core Components:**
- `main.py` - FastAPI application with CORS middleware and API endpoints
- `openai_service.py` - OpenAI Assistant integration with citation processing
- `drive_service.py` - Google Drive API service for file search
- `json.json` - Reference data mapping filenames to download links (980 references)

**Key Services:**
- **OpenAIService**: Manages chat threads, processes assistant responses, extracts citations with automatic numbering
- **DriveSearchService**: Handles Google Drive authentication and file search across multiple folders
- **SourceLinker**: Maps file citations to download links using reference data

## Development Commands

**Run the server:**
```bash
python main.py
# or
uvicorn main:app --host 127.0.0.1 --port 8000
```

**Install dependencies:**
```bash
pip install -r requirements.txt
```

**File management scripts (in crud-openai/ directory):**
```bash
# List all files in OpenAI vector store
python crud-openai/listar_archivos.py

# Upload files to vector store
python crud-openai/cargar_archivos.py

# Delete all files from vector store
python crud-openai/borrar_archivos.py
```

## Configuration

**Required environment variables (.env):**
- `OPENAI_API_KEY` - OpenAI API key
- `ASSISTANT_ID` - OpenAI Assistant ID
- `GOOGLE_DRIVE_*_ID` - Google Drive folder IDs for different content categories

**Google Drive folder mapping:**
- `articulos` - Articles folder
- `audios` - Audio files folder
- `contemplaciones` - Contemplations folder
- `libros` - Books folder
- `videos` - Videos folder

## API Endpoints

- `POST /ask` - Chat with OpenAI Assistant (returns citations)
- `POST /search-drive` - Search Google Drive files by folder
- `GET /health` - Service health check

## Key Implementation Details

- Citation system uses file annotations from OpenAI and maps them to download links
- Google Drive search supports both specific folder and global search
- Thread management allows conversation continuity
- Reference data in json.json provides O(1) lookup for download links
- CORS enabled for all origins