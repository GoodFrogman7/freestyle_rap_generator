import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [prompt, setPrompt] = useState('');
  const [temperature, setTemperature] = useState(0.8);
  const [maxLength, setMaxLength] = useState(50);
  const [output, setOutput] = useState('');

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
    <div style={{ maxWidth: 700, margin: '40px auto', padding: 20, fontFamily: 'Arial' }}>
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
      <button onClick={generate} style={{ padding: '8px 16px', fontSize: 16 }}>
        Generate 🔥
      </button>
      <pre style={{ whiteSpace: 'pre-wrap', marginTop: 20 }}>{output}</pre>
    </div>
  );
}

export default App;
