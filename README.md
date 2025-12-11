# chat-translation-backend

A Django-based backend application that provides language translation services using the Azure OpenAI API. This project is configured to work with a frontend application (e.g., running on `localhost:3000`) and exposes a RESTful endpoint for translating text.

## Features

- **Text Translation**: Translates text from one language to another using Azure's OpenAI GPT models (specifically configured for `gpt35`).
- **REST API**: Simple API endpoint to process translation requests.
- **CORS Support**: Configured to allow Cross-Origin Resource Sharing (CORS) from `http://localhost:3000`.
- **Swagger/OpenAPI Support**: Includes dependencies (`drf-yasg`) for API documentation.

## Prerequisites

- Python 3.12+
- Azure OpenAI Service credentials

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/greatwhite9/chat-translation-backend
    cd translation
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Environment Configuration:**
    Create a `.env` file in the project root (or inside the `chat_translation` directory) to store your Azure OpenAI credentials. The application requires the following variables:

    ```env
    AZURE_OAI_ENDPOINT=https://your-resource-name.openai.azure.com/
    AZURE_OAI_KEY=your_api_key_here
    AZURE_OAI_DEPLOYMENT=gpt35
    ```

5.  **Run Migrations:**
    Initialize the SQLite database.
    ```bash
    python manage.py migrate
    ```

6.  **Start the Development Server:**
    ```bash
    python manage.py runserver
    ```
    The server will start at `http://127.0.0.1:8000/`.

## API Usage

### Translate Text

**Endpoint:** `/translate/`
**Method:** `POST` (or `GET`)

**Request Body (JSON):**

| Field   | Type   | Description                         |
| :------ | :----- | :---------------------------------- |
| `text1` | String | The text you want to translate.     |
| `text2` | String | The target language (e.g., "Spanish", "French"). |

**Example Request:**

```bash
curl -X POST http://127.0.0.1:8000/translate/ \
     -H "Content-Type: application/json" \
     -d '{"text1": "Hello, how are you?", "text2": "German"}'
