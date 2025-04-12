import React, { useState } from 'react';
import MonacoEditor from '@monaco-editor/react';
import SandboxPreview from './components/SandboxPreview';
import LLMSelector from './components/LLMSelector';
import PromptForm from './components/PromptForm';
import BlockList from './components/BlockList';

export default function App() {
  const [code, setCode] = useState('// Wygenerowany kod pojawi się tutaj');
  const [commentary, setCommentary] = useState('');
  const [llm, setLlm] = useState('openai_gpt4');
  const [prompt, setPrompt] = useState('');

  const handleRun = async () => {
    const res = await fetch('http://localhost:8000/generate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt, model: llm }),
    });

    if (res.ok) {
      const data = await res.json();
      setCode(data.code);
      setCommentary(data.commentary);
    } else {
      setCode('// Błąd generowania kodu');
    }
  };

  return (
    <div className="h-screen flex flex-col bg-white text-gray-800">
      <header className="p-4 flex justify-between items-center border-b bg-blue-100">
        <h1 className="text-xl font-bold">AI Sandbox</h1>
        <LLMSelector selected={llm} onChange={setLlm} />
      </header>

      <div className="flex flex-1 overflow-hidden">
        <div className="w-1/2 p-4 flex flex-col gap-2">
          <PromptForm value={prompt} onChange={setPrompt} onRun={handleRun} />
          <MonacoEditor
            height="70%"
            language="javascript"
            theme="vs-light"
            value={code}
            onChange={(value) => setCode(value)}
            className="border rounded shadow"
          />
          <div className="text-xs text-gray-500 p-2 bg-blue-50 border rounded">{commentary}</div>
        </div>

        <div className="w-1/2 p-4 bg-gray-50 border-l">
          <SandboxPreview code={code} />
          <BlockList />
        </div>
      </div>
    </div>
  );
}
