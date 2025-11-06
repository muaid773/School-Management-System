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
from django.core.management.utils import get_random_secret_key

ENV_PATH = ".env"


def write_env_key(path: str, key: str):
    # If .env exists, replace DJANGO_SECRET_KEY line if present, else append.
    lines = []
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            lines = f.read().splitlines()

    pattern = re.compile(r'^DJANGO_SECRET_KEY\s*=')
    replaced = False
    for i, line in enumerate(lines):
        if pattern.match(line):
            lines[i] = f'DJANGO_SECRET_KEY={key}'
            replaced = True
            break

    if not replaced:
        lines.append(f'DJANGO_SECRET_KEY={key}')

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def main():
    new_key = get_random_secret_key()
    write_env_key(ENV_PATH, new_key)
    print("✅ Generated a new DJANGO_SECRET_KEY and wrote it to .env")
    print("   - .env file path:", os.path.abspath(ENV_PATH))
    print("   - Next: ensure .env is in .gitignore and restart your dev server.")


if __name__ == '__main__':
    main()
