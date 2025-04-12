import React from 'react';

const LLMSelector = ({ selected, onChange }) => {
  const models = [
    'openai_gpt4',
    'together_mistral',
    'ollama_codellama',
    'ollama_mistral',
    'custom_local',
  ];

  return (
    <select
      value={selected}
      onChange={(e) => onChange(e.target.value)}
      className="p-2 rounded border bg-white shadow"
    >
      {models.map((model) => (
        <option key={model} value={model}>
          {model}
        </option>
      ))}
    </select>
  );
};

export default LLMSelector;
