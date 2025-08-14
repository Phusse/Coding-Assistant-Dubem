import React, { useState, useRef } from 'react';
import './App.css';

// Simple spinner component
const Spinner = () => (
  <div className="spinner-container">
    <div className="spinner"></div>
  </div>
);

function App() {
  const [prompt, setPrompt] = useState('');
  const [response, setResponse] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');
  const responseRef = useRef(null);

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

  const copyToClipboard = () => {
    if (responseRef.current) {
      navigator.clipboard.writeText(responseRef.current.innerText);
      alert('Response copied to clipboard!');
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Dubem - Your AI Assistant</h1>
        <p>A modern interface for interacting with Google's Gemini AI.</p>
      </header>
      <main>
        <div className="form-container">
          <form onSubmit={handleSubmit}>
            <textarea
              value={prompt}
              onChange={(e) => setPrompt(e.target.value)}
              placeholder="Enter your prompt here..."
              rows="5"
              disabled={isLoading}
            />
            <button type="submit" disabled={isLoading}>
              {isLoading ? 'Getting Answer...' : 'Submit'}
            </button>
          </form>
        </div>

        {error && <div className="error-message">{error}</div>}

        <div className="response-container">
          {isLoading && <Spinner />}
          {response && (
            <div className="response-area">
              <div className="response-header">
                <h2>Answer</h2>
                <button onClick={copyToClipboard} className="copy-btn">Copy</button>
              </div>
              <div className="response-content" ref={responseRef}>
                <pre>{response}</pre>
              </div>
            </div>
          )}
        </div>
      </main>
    </div>
  );
}

export default App;
