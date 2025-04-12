import React from 'react';

const BlockPreview = ({ block }) => {
  if (!block) return null;

  return (
    <div className="p-4 border rounded bg-white shadow-sm text-sm space-y-2">
      <div className="flex justify-between items-center">
        <h3 className="font-bold">{block.name}</h3>
        <span className="text-xs px-2 py-1 bg-blue-100 rounded">{block.type}</span>
      </div>

      {block.commentary && (
        <pre className="text-xs text-gray-700 whitespace-pre-wrap bg-blue-50 p-2 rounded">
          {block.commentary}
        </pre>
      )}

      <pre className="text-xs whitespace-pre-wrap bg-gray-100 p-3 rounded border overflow-auto">
        {block.code}
      </pre>
    </div>
  );
};
# frontend/src/components/ExportModal.jsx (dokończenie)
cat > frontend/src/components/ExportModal.jsx << 'EOL'
import React, { useState } from 'react';

const ExportModal = ({ blocks }) => {
  const [selected, setSelected] = useState([]);

  const toggleBlock = (id) => {
    setSelected((prev) =>
      prev.includes(id) ? prev.filter((i) => i !== id) : [...prev, id]
    );
  };

  const handleExport = () => {
    const selectedBlocks = blocks.filter((block) => selected.includes(block.id));
    const zipContent = selectedBlocks
      .map(
        (block) =>
          `// ${block.name} (${block.type})\n${block.code}\n\n/* ${block.commentary} */`
      )
      .join('\n\n// -----\n\n');

    const blob = new Blob([zipContent], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = 'sandbox_export.txt';
    link.click();
    URL.revokeObjectURL(url);
  };

  return (
    <div className="p-4 bg-white rounded shadow border mt-4">
      <h2 className="text-lg font-bold mb-2">Eksportuj bloki</h2>
      <ul className="space-y-1 mb-3 max-h-40 overflow-y-auto">
        {blocks.map((block) => (
          <li key={block.id} className="flex items-center gap-2">
            <input
              type="checkbox"
              checked={selected.includes(block.id)}
              onChange={() => toggleBlock(block.id)}
            />
            <span className="text-sm">{block.name}</span>
          </li>
        ))}
      </ul>
      <button
        onClick={handleExport}
        className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
      >
        Eksportuj jako TXT
      </button>
    </div>
  );
};

export default ExportModal;
