require.config({ paths: { 'vs': 'https://cdn.jsdelivr.net/npm/monaco-editor@latest/min/vs' } });

require(['vs/editor/editor.main'], function () {
    window.editor = monaco.editor.create(document.getElementById('editor'), {
        value: `{{ code_snippet|escapejs }}`,
        language: 'python',
        theme: 'vs-dark',
        automaticLayout: true,  // ✅ IMPORTANT
    });
});

function runCode() {
    const code = editor.getValue();
    console.log("Running code:\n", code);
    // Send to backend (optional)
}

function submitCode() {
    const code = editor.getValue();
    console.log("Submitting code:\n", code);
    // Send to backend (optional)
}
