import React, { useEffect, useState } from 'react';

const BlockList = () => {
  const [blocks, setBlocks] = useState([]);

  const fetchBlocks = async () => {
    const res = await fetch('http://localhost:8000/block');
    if (res.ok) {
      const data = await res.json();
      setBlocks(data);
    }
  };

  useEffect(() => {
    fetchBlocks();
  }, []);

  return (
    <div className="mt-4">
      <h2 className="font-bold text-lg mb-2">Bloki kodu</h2>
      <div className="space-y-2">
        {blocks.map((block) => (
          <div
            key={block.id}
            className="p-3 border rounded bg-white shadow text-sm"
          >
            <div className="flex justify-between items-center mb-1">
              <strong>{block.name}</strong>
              <span className="text-xs px-2 py-1 bg-blue-100 rounded">{block.type}</span>
            </div>
            <pre className="whitespace-pre-wrap text-xs text-gray-700">
              {block.commentary || 'Brak opisu'}
            </pre>
          </div>
        ))}
      </div>
    </div>
  );
};

export default BlockList;
