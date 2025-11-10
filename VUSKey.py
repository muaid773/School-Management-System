import os
import random
import string
import re

SETTING_PATH = "_Schoolmuaid_/settings.py"

def write_secret_key(path: str, key: str):
    lines = []
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            lines = f.read().splitlines()

    pattern = re.compile(r'^\s*SECRET_KEY\s*=')  # يتجاهل المسافات في البداية
    replaced = False

    for i, line in enumerate(lines):
        if pattern.match(line):
            print("SECRET_KEY already exists, replacing it...")
            lines[i] = f"SECRET_KEY='{key}'"
            replaced = True
            break

    if not replaced:
        lines.append(f"SECRET_KEY='{key}'")
        print("SECRET_KEY added as a new line at the end of the file.")

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"✅ SECRET_KEY is set successfully in {path}")

def generate_key(length=50):
    chars = string.ascii_letters + string.digits + "#()*+,-.:;<=>?@[]^_|"
    return ''.join(random.choices(chars, k=length))

if __name__ == "__main__":
    new_key = generate_key()
    write_secret_key(SETTING_PATH, new_key)
