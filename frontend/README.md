# Dubem Frontend

This is the React-based frontend for the Dubem AI Assistant.

## Running the Frontend

To run this application, you need to have Node.js and npm installed.

1.  **Navigate to the frontend directory:**
    ```bash
    cd frontend
    ```

2.  **Install dependencies:**
    This command will install all the necessary packages defined in `package.json`.
    ```bash
    npm install
    ```

3.  **Start the development server:**
    This will run the app in development mode. Open [http://localhost:3000](http://localhost:3000) to view it in your browser.
    ```bash
    npm start
    ```

The page will reload when you make changes. You may also see any lint errors in the console.

## Connecting to the Backend

This frontend is designed to connect to the Python Flask backend, which should be running separately. By default, it will try to connect to the backend at `http://127.0.0.1:5000`.

Make sure the backend is running before you start using the application.
