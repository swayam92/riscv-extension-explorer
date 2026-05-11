import json
import os



with open("riscv-extensions-landscape/src/instr_dict.json", "r") as f:
    data = json.load(f)

json_extensions = set()

for instruction, details in data.items():

    extensions = details.get("extension", [])

    for ext in extensions:
        clean_ext = ext.lower()

        clean_ext = clean_ext.replace("rv32_", "")
        clean_ext = clean_ext.replace("rv64_", "")
        clean_ext = clean_ext.replace("rv_", "")

        json_extensions.add(clean_ext)


manual_extensions = set()

for root, dirs, files in os.walk("riscv-isa-manual"):

    for file in files:

        if file.endswith(".adoc"):

            path = os.path.join(root, file)

            with open(path, "r", encoding="utf-8") as f:

                content = f.read().lower()

                for ext in json_extensions:

                    if ext in content:
                        manual_extensions.add(ext)


matched = json_extensions & manual_extensions

json_only = json_extensions - manual_extensions

manual_only = manual_extensions - json_extensions



print("\nMATCHED EXTENSIONS:\n")

for ext in sorted(matched):
    print(ext)

print("\nJSON ONLY:\n")

for ext in sorted(json_only):
    print(ext)

print("\nMANUAL ONLY:\n")

for ext in sorted(manual_only):
    print(ext)

print("\nSUMMARY:\n")

print(f"{len(matched)} matched")
print(f"{len(json_only)} JSON only")
print(f"{len(manual_only)} manual only")