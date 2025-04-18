import docker
import uuid
import os

client = docker.from_env()

def run_code(language, code):
    lang_map = {
        "python": {"image": "python:3.9", "cmd": "python"},
        "cpp": {"image": "gcc:latest", "cmd": "g++ run_code.cpp -o run && ./run"},
        "java": {"image": "openjdk:17", "cmd": "javac RunCode.java && java RunCode"},
        "js": {"image": "node:latest", "cmd": "node run_code.js"},
        "c": {"image": "gcc:latest", "cmd": "gcc run_code.c -o run && ./run"}
    }

    if language not in lang_map:
        return "Unsupported language!"

    # Generate a unique filename
    extension_map = {"python": "py", "cpp": "cpp", "java": "java", "js": "js", "c": "c"}
    filename = f"run_code_{uuid.uuid4()}.{extension_map[language]}"
    
    # Write the user's code to a temp file
    with open(filename, "w") as f:
        f.write(code)

    try:
        # Run the code inside Docker
        container = client.containers.run(
            image=lang_map[language]["image"],
            command=f"/bin/sh -c '{lang_map[language]['cmd']}'",
            volumes={os.path.abspath(filename): {'bind': f"/app/{filename}", 'mode': 'ro'}},
            working_dir="/app",
            remove=True
        )
        return container.decode('utf-8')
    except Exception as e:
        return str(e)
    finally:
        # Clean up temp file
        if os.path.exists(filename):
            os.remove(filename)

# Example usage
code_python = "print('Hello from Python!')"
print(run_code("python", code_python))

code_js = "console.log('Hello from JavaScript!');"
print(run_code("js", code_js))

code_c = """
#include <stdio.h>
int main() {
    printf("Hello from C!\\n");
    return 0;
}
"""
print(run_code("c", code_c))
