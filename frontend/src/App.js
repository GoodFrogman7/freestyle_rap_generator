import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [prompt, setPrompt] = useState('');
  const [temperature, setTemperature] = useState(0.8);
  const [maxLength, setMaxLength] = useState(50);
  const [output, setOutput] = useState('');

  // Apply a dark theme background when the component mounts
  useEffect(() => {
    const originalBg = document.body.style.backgroundColor;
    const originalColor = document.body.style.color;
    document.body.style.backgroundColor = '#121212';
    document.body.style.color = '#f5f5f5';
    return () => {
      // Cleanup when component unmounts
      document.body.style.backgroundColor = originalBg;
      document.body.style.color = originalColor;
    };
  }, []);

  const generate = async () => {
    try {
      const res = await axios.post('http://localhost:8000/api/v1/generate', {
        prompt,
        temperature,
        max_length: maxLength,
        top_k: 50,
        top_p: 0.9
      });

      console.log('API Response:', res.data); // Debug: log the full response

      // Handle different possible key names
      const lyrics =
        res.data.lyrics || res.data.text || res.data.output || 'No lyrics found.';
      setOutput(lyrics);
    } catch (err) {
      console.error('Error generating lyrics:', err);
      setOutput('Error generating lyrics.');
    }
  };

  return (
    <div
      style={{
        maxWidth: 720,
        margin: '40px auto',
        padding: 24,
        fontFamily: 'Arial, Helvetica, sans-serif',
        backgroundColor: '#1e1e1e',
        borderRadius: 8,
        boxShadow: '0 4px 12px rgba(0,0,0,0.5)'
      }}
    >
      <h1>🎤 Freestyle Rap Generator</h1>
      <textarea
        rows="4"
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        placeholder="Enter your rap prompt..."
        style={{ width: '100%', marginBottom: 12, fontSize: 16 }}
      />
      <div style={{ marginBottom: 10 }}>
        <label>Temperature: </label>
        <input
          type="number"
          step="0.1"
          min="0.1"
          max="1.0"
          value={temperature}
          onChange={(e) => setTemperature(Number(e.target.value))}
        />
      </div>
      <div style={{ marginBottom: 10 }}>
        <label>Max Length: </label>
        <input
          type="number"
          min="10"
          max="200"
          value={maxLength}
          onChange={(e) => setMaxLength(Number(e.target.value))}
        />
      </div>
      <button
        onClick={generate}
        style={{
          padding: '10px 20px',
          fontSize: 16,
          backgroundColor: '#ff5722',
          color: '#fff',
          border: 'none',
          borderRadius: 6,
          cursor: 'pointer'
        }}
      >
        Generate 🔥
      </button>
      <textarea
        readOnly
        rows={8}
        value={output}
        placeholder="Generated lyrics will appear here..."
        style={{
          width: '100%',
          marginTop: 24,
          backgroundColor: '#262626',
          color: '#f5f5f5',
          border: '1px solid #555',
          borderRadius: 6,
          padding: 12,
          fontSize: 15,
          resize: 'vertical',
          whiteSpace: 'pre-wrap'
        }}
      />
    </div>
  );
}

export default App;
