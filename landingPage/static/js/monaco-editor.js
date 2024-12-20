require.config({ paths: { 'vs': 'https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.43.0/min/vs' } });

let editor; // Global editor variable

require(['vs/editor/editor.main'], function () {
    editor = monaco.editor.create(document.getElementById('editor'), {
        value: `# Welcome to CodeSphere!
# Python code here.
print("Hello, CodeSphere!")`,
        language: 'python',
        theme: 'vs-dark',
        automaticLayout: true,
    });
});

// Code snippets for each language
const cppCode = `#include <iostream>
using namespace std;

int main() {
    cout << "Hello, CodeSphere!" << endl;
    return 0;
}`;

const javaCode = `public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, CodeSphere!");
    }
}`;

const pythonCode = `# Welcome to CodeSphere!
print("Hello, CodeSphere!")`;

// Add event listeners to buttons
document.querySelector('.cpp-btn').addEventListener('click', function () {
    editor.setValue(cppCode);
    monaco.editor.setModelLanguage(editor.getModel(), 'cpp');
});

document.querySelector('.java-btn').addEventListener('click', function () {
    editor.setValue(javaCode);
    monaco.editor.setModelLanguage(editor.getModel(), 'java');
});

document.querySelector('.python-btn').addEventListener('click', function () {
    editor.setValue(pythonCode);
    monaco.editor.setModelLanguage(editor.getModel(), 'python');
});





// *******************  js for the demo list  *********************

document.addEventListener('DOMContentLoaded', function () {
    const demoLinks = document.querySelectorAll('.demo-link');

    demoLinks.forEach(link => {
        link.addEventListener('click', function (event) {
            event.preventDefault();
            demoLinks.forEach(link => link.classList.remove('active'));
            this.classList.add('active');
        });
    });
});
