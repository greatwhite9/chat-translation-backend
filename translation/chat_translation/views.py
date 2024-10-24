import os
from dotenv import load_dotenv
from rest_framework.decorators import api_view
from rest_framework.response import Response
from openai import AzureOpenAI

# Load environment variables from .env file
load_dotenv()

# Get Azure OpenAI configuration settings from environment variables
azure_oai_endpoint = os.getenv("AZURE_OAI_ENDPOINT")
azure_oai_key = os.getenv("AZURE_OAI_KEY")
azure_oai_deployment = os.getenv("AZURE_OAI_DEPLOYMENT")

# Initialize the Azure OpenAI client
client = AzureOpenAI(
    azure_endpoint=azure_oai_endpoint,
    api_key=azure_oai_key,
    api_version="2024-02-15-preview"
)

@api_view(['POST'])
def translate_text(request):
    try:
        # Get the two strings (text to translate and target language) from the request
        text_to_translate = request.data.get('text1')
        target_language = request.data.get('text2')

        if not text_to_translate or not target_language:
            return Response({"error": "Both 'text1' and 'text2' are required"}, status=400)

        # System message defining the task (language translation)
        system_message = f"""You are a language translation assistant. Please translate the given text to {target_language}.
        """

        # Initialize messages array with the system message
        messages_array = [{"role": "system", "content": system_message}]
        
        # Add the user prompt (text to translate) to the messages array
        messages_array.append({"role": "user", "content": text_to_translate})

        # Send request to Azure OpenAI model for translation
        response = client.chat.completions.create(
            model=azure_oai_deployment,
            temperature=0.7,
            max_tokens=1200,
            messages=messages_array
        )

        # Extract the generated translated text from the response
        translated_text = response.choices[0].message.content

        # Return the translated text in the response
        return Response({"translated_text": translated_text}, status=200)

    except Exception as ex:
        return Response({"error": str(ex)}, status=500)
