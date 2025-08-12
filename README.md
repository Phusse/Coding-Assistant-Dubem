# Dubem - Your Personal AI Assistant

Dubem is an AI assistant powered by Google's Gemini AI. You can interact with it through a modern web interface or a simple command-line tool.

## Configuration

Before you begin, you need to configure your Gemini API key.

1.  **Get a Gemini API Key:**
    - Go to the [Google AI for Developers](https://ai.google.dev/) website.
    - Create an API key in Google AI Studio.
2.  **Set the API Key as an Environment Variable:**
    - **Linux/macOS:**
      ```bash
      export GEMINI_API_KEY='YOUR_API_KEY'
      ```
    - **Windows:**
      ```powershell
      $env:GEMINI_API_KEY='YOUR_API_KEY'
      ```
    Replace `YOUR_API_KEY` with the key you obtained. For persistent storage, add this line to your shell's startup file (e.g., `.bashrc`, `.zshrc`, or your PowerShell profile).

## Usage

You can use Dubem in two ways:

### 1. Web Application (Recommended)

The web application provides a user-friendly interface for interacting with the AI.

**Installation:**
1.  Install the Python backend dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2.  Install the JavaScript frontend dependencies:
    ```bash
    cd frontend
    npm install
    cd ..
    ```

**Running the Application:**
You need to run two processes in separate terminals.

-   **Terminal 1: Start the Backend**
    ```bash
    python -m dubem.app
    ```
    This will start the Flask server on `http://127.0.0.1:5000`.

-   **Terminal 2: Start the Frontend**
    ```bash
    cd frontend
    npm start
    ```
    This will open the web application in your browser at `http://localhost:3000`.

### 2. Command-Line Tool

For quick queries, you can use the original command-line interface.

**Installation:**
```bash
pip install -r requirements.txt
```

**Usage:**
```bash
python -m dubem.main "Your coding question or prompt"
```

For example:
```bash
python -m dubem.main "How do I reverse a list in Python?"
```
