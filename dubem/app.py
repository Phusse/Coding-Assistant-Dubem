import os
import google.generativeai as genai
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will allow the frontend to make requests to the backend

# Configure the API key
try:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Error: GEMINI_API_KEY environment variable not set.")
    genai.configure(api_key=api_key)
except ValueError as e:
    print(e)
    # You might want to handle this more gracefully
    # For now, we'll let the app crash if the key isn't set,
    # which will be visible in the server logs.


@app.route('/api/prompt', methods=['POST'])
def handle_prompt():
    """
    Handles the prompt from the frontend and returns a response from the Gemini model.
    """
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    prompt = data.get('prompt')

    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    try:
        # Create the model
        model = genai.GenerativeModel('gemini-pro')

        # Generate content
        response = model.generate_content(prompt)

        return jsonify({"response": response.text})
    except Exception as e:
        # Log the exception for debugging
        app.logger.error(f"An error occurred: {e}")
        return jsonify({"error": "An internal error occurred."}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
