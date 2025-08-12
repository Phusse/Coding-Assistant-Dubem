import argparse
import os
import google.generativeai as genai

def main():
    """
    The main function for the Dubem CLI.
    """
    # Configure the API key
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not set.")
        return
    genai.configure(api_key=api_key)

    parser = argparse.ArgumentParser(description="Dubem: Your personal coding assistant.")
    parser.add_argument("prompt", type=str, help="The coding question or prompt for Dubem.")
    args = parser.parse_args()

    try:
        # Create the model
        model = genai.GenerativeModel('gemini-pro')

        # Generate content
        response = model.generate_content(args.prompt)

        print(response.text)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
