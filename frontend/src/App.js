import React, { useState } from 'react';
import './App.css';

function App() {
  const [prompt, setPrompt] = useState('');
  const [response, setResponse] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!prompt.trim()) {
      setError('Please enter a prompt.');
      return;
    }

    setIsLoading(true);
    setResponse('');
    setError('');

    try {
      const apiResponse = await fetch('http://127.0.0.1:5000/api/prompt', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ prompt }),
      });

      if (!apiResponse.ok) {
        // Try to get error message from backend, otherwise use status text
        const errorData = await apiResponse.json().catch(() => null);
        throw new Error(errorData?.error || apiResponse.statusText);
      }

      const data = await apiResponse.json();
      setResponse(data.response);
    } catch (err) {
      setError(err.message || 'An unexpected error occurred.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Dubem - Your AI Assistant</h1>
        <p>Ask a question, get an answer.</p>
      </header>
      <main>
        <form onSubmit={handleSubmit}>
          <textarea
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            placeholder="Enter your prompt here..."
            rows="4"
            disabled={isLoading}
          />
          <button type="submit" disabled={isLoading}>
            {isLoading ? 'Getting Answer...' : 'Submit'}
          </button>
        </form>
        {error && <div className="error-message">{error}</div>}
        {response && (
          <div className="response-area">
            <h2>Answer:</h2>
            <pre>{response}</pre>
          </div>
        )}
      </main>
    </div>
  );
}

export default App;
