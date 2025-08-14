import os
import time
import google.generativeai as genai
from flask import Flask, request, jsonify, Response, stream_with_context
from flask_cors import CORS
from google.api_core.exceptions import ResourceExhausted

app = Flask(__name__)
CORS(app)

# Configure the API key
try:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Error: GEMINI_API_KEY environment variable not set.")
    genai.configure(api_key=api_key)
except ValueError as e:
    print(e)

DEFAULT_MODEL = "gemini-1.5-pro"
FALLBACK_MODEL = "gemini-1.5-flash"

def stream_response_generator(prompt, retries=1):
    """
    Generates content from the model and streams it chunk by chunk,
    with retry and fallback logic.
    """
    model_name = DEFAULT_MODEL
    for attempt in range(retries + 1):
        try:
            model = genai.GenerativeModel(model_name)
            response_stream = model.generate_content(prompt, stream=True)

            # If we get a response, stream it and exit the retry loop
            yield from (chunk.text for chunk in response_stream if chunk.text)
            return # Successfully streamed, so exit the generator

        except ResourceExhausted as e:
            app.logger.error(f"Quota exceeded on model {model_name} (attempt {attempt + 1}): {e}")
            if attempt < retries and model_name == DEFAULT_MODEL:
                app.logger.info(f"Switching to fallback model {FALLBACK_MODEL}")
                model_name = FALLBACK_MODEL
                continue # Go to the next retry attempt
            else:
                yield "The service is currently busy. Please try again later."
                return
        except Exception as e:
            app.logger.error(f"An unexpected error occurred during streaming: {e}")
            yield "An error occurred while generating the response."
            return

@app.route('/api/prompt', methods=['POST'])
def handle_prompt():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    prompt = data.get('prompt')

    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    return Response(stream_with_context(stream_response_generator(prompt, retries=1)), mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
