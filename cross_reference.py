import os
import re

manual_extensions = set()

for root, dirs, files in os.walk("riscv-isa-manual"):

    for file in files:

        if file.endswith(".adoc"):

            path = os.path.join(root, file)

            with open(path, "r", encoding="utf-8") as f:

                content = f.read()

                matches = re.findall(r'\b[zs][a-zA-Z0-9]+\b', content)

                for match in matches:
                    manual_extensions.add(match.lower())

print("\nMANUAL EXTENSIONS:\n")

for ext in sorted(manual_extensions):

    print(ext)