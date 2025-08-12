# Dubem - Your Personal Coding Assistant

Dubem is a command-line coding assistant powered by Google's Gemini AI.

## Installation

1.  Clone this repository.
2.  Install the necessary packages:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

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

To use Dubem, run the following command in your terminal:

```bash
python -m dubem.main "Your coding question or prompt"
```

For example:

```bash
python -m dubem.main "How do I reverse a list in Python?"
```
