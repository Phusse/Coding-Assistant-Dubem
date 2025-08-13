import os
import time
import google.generativeai as genai
from flask import Flask, request, jsonify
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

def generate_with_retry(prompt, model_name=DEFAULT_MODEL, retries=1):
    """Try generating content, retry on quota error, switch to fallback model if needed."""
    for attempt in range(retries + 1):
        try:
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(prompt)
            return response.text
        except ResourceExhausted as e:
            # Quota error
            app.logger.error(f"Quota exceeded on model {model_name}: {e}")
            if "retry_delay" in str(e):
                try:
                    delay_seconds = int(str(e).split("seconds: ")[1].split("\n")[0])
                    app.logger.info(f"Retrying after {delay_seconds} seconds...")
                    time.sleep(delay_seconds)
                except Exception:
                    time.sleep(5)  # default wait
            if model_name == DEFAULT_MODEL:
                app.logger.info(f"Switching to fallback model {FALLBACK_MODEL}")
                model_name = FALLBACK_MODEL
            else:
                raise
        except Exception as e:
            app.logger.error(f"An error occurred with model {model_name}: {e}")
            raise
    return None

@app.route('/api/prompt', methods=['POST'])
def handle_prompt():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    prompt = data.get('prompt')

    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    try:
        result = generate_with_retry(prompt, retries=2)
        if result is None:
            return jsonify({"error": "Failed after retries"}), 500
        return jsonify({"response": result})
    except Exception as e:
        app.logger.error(f"Final error: {e}", exc_info=True)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
