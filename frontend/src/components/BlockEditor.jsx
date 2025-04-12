import React, { useState, useEffect } from 'react';
import MonacoEditor from '@monaco-editor/react';

const BlockEditor = ({ blockId }) => {
  const [block, setBlock] = useState(null);

  useEffect(() => {
    const fetchBlock = async () => {
      const res = await fetch(`http://localhost:8000/block/${blockId}`);
      if (res.ok) {
        const data = await res.json();
        setBlock(data);
      }
    };

    if (blockId) fetchBlock();
  }, [blockId]);

  const handleSave = async () => {
    const res = await fetch(`http://localhost:8000/block/${block.id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(block),
    });

    if (res.ok) alert('Zapisano blok.');
    else alert('Błąd zapisu.');
  };

  if (!block) return <div className="text-sm text-gray-500">Wybierz blok...</div>;

  return (
    <div className="space-y-2 mt-4">
      <input
        type="text"
        value={block.name}
        onChange={(e) => setBlock({ ...block, name: e.target.value })}
        className="w-full p-2 border rounded"
        placeholder="Nazwa bloku"
      />
      <textarea
        value={block.commentary}
        onChange={(e) => setBlock({ ...block, commentary: e.target.value })}
        className="w-full p-2 border rounded h-20"
        placeholder="Komentarz"
      />
      <select
        value={block.type}
        onChange={(e) => setBlock({ ...block, type: e.target.value })}
        className="p-2 border rounded"
      >
        <option value="component">component</option>
        <option value="api">api</option>
        <option value="style">style</option>
        <option value="hook">hook</option>
        <option value="merged">merged</option>
      </select>

      <MonacoEditor
        height="300px"
        language="javascript"
        theme="vs-light"
        value={block.code}
        onChange={(value) => setBlock({ ...block, code: value })}
      />

      <button
        onClick={handleSave}
        className="bg-green-600 text-white px-4 py-2 rounded shadow hover:bg-green-700"
      >
        Zapisz blok
      </button>
    </div>
  );
};

export default BlockEditor;
