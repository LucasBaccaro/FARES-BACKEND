# API Backend - Diego Fares Assistant

API backend que integra un asistente de OpenAI con búsqueda en Google Drive para contenido de Diego Fares.

## 🚀 Servidor en funcionamiento

**Base URL:** `http://localhost:8000`

**Documentación interactiva:** `http://localhost:8000/docs`

## 📝 Endpoints disponibles

### 1. **POST `/ask`** - Chat con Asistente OpenAI

Envía un mensaje al asistente de Diego Fares y obtiene respuesta con citas automáticas.

**Request:**
```json
{
    "message": "¿Qué dice Diego Fares sobre la cultura del encuentro?",
    "thread_id": "opcional_para_continuar_conversacion"
}
```

**Response:**
```json
{
    "thread_id": "thread_abc123",
    "assistant_message": "Según Diego Fares, la cultura del encuentro...[1]",
    "citations": [
        {
            "file_id": "file-xyz789",
            "file_name": "libros - papa francisco- La Cutura del Encuentro Ed Edhasa.txt",
            "quote": "La cultura del encuentro es...",
            "text": "[1]",
            "download_link": "https://drive.google.com/file/d/..."
        }
    ]
}
```

**Ejemplo JavaScript:**
```javascript
const response = await fetch('http://localhost:8000/ask', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
        message: "¿Qué opina Diego Fares sobre la esperanza?",
        thread_id: null // o el thread_id de una conversación previa
    })
});

const result = await response.json();
console.log('Respuesta:', result.assistant_message);
console.log('Citas:', result.citations);
```

---

### 2. **POST `/search-drive`** - Búsqueda en Google Drive

Busca archivos en las carpetas de Google Drive de Diego Fares.

**Carpetas disponibles:**
- `"articulos"`
- `"audios"`
- `"contemplaciones"`
- `"libros"`
- `"videos"`

**Request:**
```json
{
    "query": "cultura encuentro",
    "carpeta": "libros"
}
```

**Response:**
```json
{
    "success": true,
    "total": 3,
    "carpeta_buscada": "libros",
    "archivos": [
        {
            "id": "1ABC123",
            "name": "La Cultura del Encuentro - Diego Fares.pdf",
            "view_link": "https://drive.google.com/file/d/1ABC123/view",
            "download_link": "https://drive.google.com/file/d/1ABC123/view",
            "mime_type": "application/pdf",
            "size": "1234567",
            "modified_time": "2023-01-15T10:30:00Z"
        }
    ]
}
```

**Ejemplo JavaScript:**
```javascript
// Búsqueda en carpeta específica
const searchInFolder = async (query, folder) => {
    const response = await fetch('http://localhost:8000/search-drive', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            query: query,
            carpeta: folder
        })
    });

    const result = await response.json();
    return result.archivos;
};

// Uso
const libros = await searchInFolder("esperanza", "libros");
const audios = await searchInFolder("discernimiento", "audios");
```

**Búsqueda global (sin especificar carpeta):**
```json
{
    "query": "francisco"
}
```

---

### 3. **GET `/health`** - Estado del servidor

Verifica que todos los servicios estén funcionando.

**Response:**
```json
{
    "status": "healthy",
    "openai_enabled": true,
    "drive_enabled": true,
    "assistant_id": "asst_C7z5xqHOSlOFDbXWL9YaFhNR",
    "references_loaded": 980
}
```

## 🎯 Flujo de trabajo recomendado

### Para Chat con Asistente:
1. **Primera consulta**: Enviar mensaje sin `thread_id`
2. **Guardar** el `thread_id` de la respuesta
3. **Conversaciones siguientes**: Enviar con el mismo `thread_id`
4. **Mostrar citas**: Usar los `download_link` para enlaces de descarga

### Para Búsqueda en Drive:
1. **Frontend conoce las carpetas**: `["articulos", "audios", "libros", "videos", "contemplaciones"]`
2. **Usuario selecciona carpeta** en la UI
3. **Usuario escribe término** de búsqueda
4. **Enviar a `/search-drive`** con carpeta + query
5. **Mostrar resultados** con links de descarga

## ⚠️ Manejo de errores

### Error 400 - Carpeta no configurada
```json
{
    "detail": "Carpeta 'inexistente' no configurada en el servidor"
}
```

### Error 500 - Error interno
```json
{
    "detail": "Error interno: descripción del error"
}
```

### Error 504 - Timeout
```json
{
    "detail": "Request timeout - assistant took too long to respond"
}
```

## 🔧 Configuración de CORS

El servidor ya está configurado para aceptar requests desde cualquier origen. Si necesitas configuración específica, contacta al equipo backend.

## 📱 Ejemplo completo React/JS

```javascript
class DiegoFaresAPI {
    constructor() {
        this.baseURL = 'http://localhost:8000';
        this.currentThreadId = null;
    }

    async chat(message) {
        const response = await fetch(`${this.baseURL}/ask`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                message,
                thread_id: this.currentThreadId
            })
        });

        if (!response.ok) {
            throw new Error(`Error ${response.status}: ${await response.text()}`);
        }

        const result = await response.json();
        this.currentThreadId = result.thread_id; // Guardar para siguientes mensajes
        return result;
    }

    async searchDrive(query, folder = null) {
        const body = { query };
        if (folder) body.carpeta = folder;

        const response = await fetch(`${this.baseURL}/search-drive`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(body)
        });

        if (!response.ok) {
            throw new Error(`Error ${response.status}: ${await response.text()}`);
        }

        return await response.json();
    }

    async health() {
        const response = await fetch(`${this.baseURL}/health`);
        return await response.json();
    }

    newConversation() {
        this.currentThreadId = null;
    }
}

// Uso
const api = new DiegoFaresAPI();

// Chat
const chatResult = await api.chat("¿Qué dice Diego Fares sobre la esperanza?");
console.log(chatResult.assistant_message);

// Búsqueda
const searchResult = await api.searchDrive("cultura encuentro", "libros");
console.log(searchResult.archivos);
```

## 📞 Contacto

Para dudas técnicas o problemas con la API, contactar al equipo de backend.