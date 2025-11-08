"""VUSKey.py

Utility to generate a new DJANGO_SECRET_KEY and store it in a local .env file
instead of writing secrets directly into settings.py. This keeps secrets out of
the repository and works with the README changes that load .env via python-dotenv.

Usage:
  python VUSKey.py

After running, a `.env` file will be created or updated with the variable
`DJANGO_SECRET_KEY=<generated-key>`.
"""

import re
import os
import random
import string

SETTING_PATH = "_Schoolmuaid_/settings.py"


def write_env_key(path: str, key: str):
    # If .env exists, replace DJANGO_SECRET_KEY line if present, else append.
    lines = []
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            lines = f.read().splitlines()

    pattern = re.compile(r'SECRET_KEY=')
    replaced = False
    for i, line in enumerate(lines):
        if pattern.match(line):
            print("Maybe SECRET_KEY variable is alrey exisit")
            choice = input("Do you want to continue[Y/N]? ").upper()
            if choice == "Y":
                lines[i] = f"SECRET_KEY='{key}'"
                replaced = True
                print(f"✅ Change is successful in line {i+1}\n      file:{path}")
                print(f"NEW LINE:\n    SECRET_KEY='{key}'\n")
            else:
                print(f"Canceled...")
            replaced = True
            break

    if not replaced:
        lines.append(f"SECRET_KEY='{key}'")
        print(f"✅ Change is successful in last line\n      file:{path}")
        print(f"NEW LINE:\n    SECRET_KEY='{key}'\n")

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def main():

    new_key = ''.join(random.choices("!#$%&()*+,-./:;<=>?@[\]^_{|}" + string.ascii_letters + string.digits, k=50))
    write_env_key(SETTING_PATH, new_key)



if __name__ == '__main__':
    main()
