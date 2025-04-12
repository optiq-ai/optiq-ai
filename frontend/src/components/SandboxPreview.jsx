import React, { useEffect, useRef } from 'react';

const SandboxPreview = ({ code }) => {
  const iframeRef = useRef(null);

  useEffect(() => {
    if (!iframeRef.current) return;

    const html = `
      <html>
        <head>
          <style>body { margin: 0; font-family: sans-serif; }</style>
        </head>
        <body>
          <div id="root"></div>
          <script type="module">
            try {
              ${code}
            } catch (e) {
              document.body.innerHTML = '<pre style="color: red;">' + e + '</pre>';
            }
          </script>
        </body>
      </html>
    `;

    const blob = new Blob([html], { type: 'text/html' });
    const url = URL.createObjectURL(blob);
    iframeRef.current.src = url;

    return () => URL.revokeObjectURL(url);
  }, [code]);

  return (
    <div className="h-[400px] border rounded shadow overflow-hidden">
      <iframe
        title="Sandbox Preview"
        ref={iframeRef}
        sandbox="allow-scripts"
        className="w-full h-full bg-white"
      />
    </div>
  );
};

export default SandboxPreview;
