# RISC-V Extension Explorer

A Python-based tool for analyzing and cross-referencing RISC-V ISA extensions using the official RISC-V Extensions Landscape repository and the official RISC-V ISA manual.

## Features

### Tier 1 — Instruction Set Parsing
- Parses `instr_dict.json`
- Groups instructions by extension
- Prints extension summaries
- Detects instructions belonging to multiple extensions

### Tier 2 — Cross-Reference with ISA Manual
- Scans `.adoc` files from the official ISA manual
- Extracts extension references using regex
- Normalizes extension names
- Compares JSON extensions with manual extensions
- Reports:
  - matched extensions
  - JSON-only extensions
  - manual-only extensions

## Technologies Used
- Python
- JSON parsing
- Regex
- File system traversal (`os.walk`)

## Files

- `main.py` → Tier 1 parsing and grouping
- `cross_reference.py` → extracts extensions from ISA manual
- `compare_extensions.py` → compares extension sets

## How to Run

```bash
python main.py
python cross_reference.py
python compare_extensions.py
