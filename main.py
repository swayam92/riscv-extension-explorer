import json

with open("riscv-extensions-landscape/src/instr_dict.json", "r") as f:
    data = json.load(f)

print(type(data))
print(len(data))

first_key = list(data.keys())[0]

print("\nFIRST INSTRUCTION:")
print(first_key)

print("\nDATA:")
print(data[first_key])


extension_map = {}

for instruction, details in data.items():

    extensions = details.get("extension", [])

    for ext in extensions:

        if ext not in extension_map:
            extension_map[ext] = []

        extension_map[ext].append(instruction)



print("\nEXTENSION SUMMARY:\n")

for ext, instructions in extension_map.items():

    print(
        f"{ext} | {len(instructions)} instructions | e.g. {instructions[0]}"
    )


print("\nMULTI-EXTENSION INSTRUCTIONS:\n")

for instruction, details in data.items():

    extensions = details.get("extension", [])

    if len(extensions) > 1:

        print(f"{instruction} -> {extensions}")