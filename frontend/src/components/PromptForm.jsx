import React from 'react';

const PromptForm = ({ value, onChange, onRun }) => {
  return (
    <div className="flex gap-2 items-start">
      <textarea
        placeholder="Wpisz prompt do LLM"
        value={value}
        onChange={(e) => onChange(e.target.value)}
        className="flex-1 p-2 border rounded resize-none h-24"
      />
      <button
        onClick={onRun}
        className="bg-blue-600 text-white px-4 py-2 rounded shadow hover:bg-blue-700"
      >
        Wygeneruj
      </button>
    </div>
  );
};

export default PromptForm;
