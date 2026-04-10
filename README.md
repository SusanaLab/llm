# Proyecto: Asistente de escritura con LLM

## Descripción
Este proyecto implementa un asistente de escritura utilizando la API de OpenAI. Permite generar texto, mejorar redacción y corregir estilo a partir de una idea proporcionada por el usuario.

---

## Instrucciones

### 1. Clonar repositorio
git clone <URL>
cd proyecto

### 2. Crear entorno virtual
python -m venv .venv

Activar:

Windows:
.venv\Scripts\activate

Linux/Mac:
source .venv/bin/activate

### 3. Instalar dependencias
pip install -r requirements.txt

### 4. Configurar API KEY
Crear archivo `.env`:
OPENAI_API_KEY=tu_api_key

### 5. Ejecutar
python app.py