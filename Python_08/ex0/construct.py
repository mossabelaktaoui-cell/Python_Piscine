import sys
import os
import site

current_env = sys.prefix
current_python = sys.executable

if current_env == sys.base_prefix:
    print(
        "\nMATRIX STATUS: You're still plugged in\n\n"
        f"Current Python: {current_python}\n"
        "Virtual Environment: None detected\n\n"
        "WARNING: You're in the global environment!\n"
        "The machines can see everything you install.\n\n"
        "To enter the construct, run:\n"
        "python -m venv matrix_env\n"
        "source matrix_env/bin/activate # On Unix\n"
        "matrix_env\n"
        "Scripts\n"
        "activate    # On Windows\n\n"
        "Then run this program again."
    )
else:
    print(
        "\nMATRIX STATUS: Welcome to the construct\n\n"
        f"Current Python: {current_python}\n"
        f"Virtual Environment: {os.environ['VIRTUAL_ENV_PROMPT']}\n"
        f"Environment Path: {current_env}\n\n"
        "SUCCESS: You're in an isolated environment!\n"
        "Safe to install packages without affecting the global system.\n\n"
        "Package installation path:\n"
        f"{site.getsitepackages()[0]}"
    )
