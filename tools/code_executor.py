import subprocess
import tempfile
import os


def execute_python_code(code: str):
    """
    Executes Python code safely in temp file.
    """

    with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as tmp:
        tmp.write(code.encode())
        tmp_path = tmp.name

    try:
        result = subprocess.run(
            ["python", tmp_path],
            capture_output=True,
            text=True,
            timeout=10
        )
        return {
            "stdout": result.stdout,
            "stderr": result.stderr
        }
    finally:
        os.remove(tmp_path)
