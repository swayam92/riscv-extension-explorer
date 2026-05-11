# RISC-V Extension Explorer

A Python-based analysis tool for exploring and cross-referencing RISC-V ISA extensions using:

* The official RISC-V Extensions Landscape repository
* The official RISC-V ISA Manual

This project was developed as part of the Linux Foundation LFX Mentorship coding challenge.

---

# Project Goals

The goal of this project is to:

1. Parse RISC-V instruction extension metadata
2. Group instructions by extension tags
3. Detect instructions shared across multiple extensions
4. Cross-reference extension names with the official ISA manual
5. Identify mismatches and missing references
6. Improve understanding of RISC-V ISA organization

---

# Features

## Tier 1 — Instruction Set Parsing

Implemented in `main.py`

### Functionalities

* Reads `instr_dict.json`
* Parses all instruction entries
* Groups instructions by extension
* Prints extension summary table
* Detects instructions belonging to multiple extensions

### Example Output

```text
rv_zba | 3 instructions | e.g. sh1add
```

### Multi-Extension Detection

The tool identifies instructions shared between multiple ISA extensions.

Example:

```text
andn -> ['rv_zbb', 'rv_zkn', 'rv_zks', 'rv_zk', 'rv_zbkb']
```

---

## Tier 2 — ISA Manual Cross-Reference

Implemented in:

* `cross_reference.py`
* `compare_extensions.py`

### Functionalities

* Scans `.adoc` files from the official RISC-V ISA manual
* Extracts extension names using regex
* Normalizes extension names for accurate matching
* Compares ISA manual references against JSON extension definitions

### Reports Generated

* Matched extensions
* JSON-only extensions
* Manual-only extensions
* Count summaries

### Example Summary

```text
63 matched
22 JSON only
0 manual only
```

---

# Design Decisions

## Extension Normalization

The JSON file uses prefixes such as:

```text
rv_zba
rv64_zbb
rv32_zkn
```

The ISA manual commonly references extensions as:

```text
zba
zbb
zkn
```

To improve matching accuracy, prefixes like:

* `rv_`
* `rv32_`
* `rv64_`

are normalized before comparison.

---

## Regex-Based Extraction

Regex extraction was used to identify extension references inside `.adoc` files.

Pattern used:

```python
r'\b[zs][a-zA-Z0-9]+\b'
```

This allows automatic discovery of extension names throughout the manual source tree.

---

# Edge Cases Handled

## Multiple Extension Membership

Some instructions belong to multiple ISA extensions.

The parser correctly stores all associated extensions.

---

## Missing Extension Tags

Instructions without extension information are skipped safely.

---

## Duplicate References

Sets are used during extraction and comparison to avoid duplicate extension entries.

---

## Naming Variations

Normalization logic reduces mismatches caused by naming differences between:

* JSON metadata
* ISA manual references

---

## Large File Traversal

Recursive traversal using `os.walk()` ensures all `.adoc` files are scanned efficiently.

---

# Repository Structure

```text
riscv-extension-explorer/
│
├── main.py
├── cross_reference.py
├── compare_extensions.py
├── README.md
├── .gitignore
├── riscv-extensions-landscape/
└── riscv-isa-manual/
```

---

# Technologies Used

* Python 3
* JSON Parsing
* Regex
* File System Traversal
* Git + GitHub

---

# How To Run

## Clone Repository

```bash
git clone https://github.com/swayam92/riscv-extension-explorer.git
cd riscv-extension-explorer
```

## Run Tier 1

```bash
python main.py
```

## Run ISA Extraction

```bash
python cross_reference.py
```

## Run Extension Comparison

```bash
python compare_extensions.py
```

---

# Possible Future Improvements

* Graph visualization of shared extensions
* Unit tests for normalization logic
* CLI interface with arguments
* Export reports to CSV/JSON
* Automated repository cloning
* Better extension categorization

---

# Bonus Ideas Implemented / Planned

## Repository Quality

* GitHub repository setup
* `.gitignore` configuration
* Clean commit history
* Organized file structure

## Edge Case Handling

* Duplicate extension handling
* Extension normalization
* Multi-extension instruction detection

## Future Bonus Possibilities

* Network graph of extension relationships
* Pytest-based automated tests
* Performance optimizations


## Extension Relationship Graph

The graph below visualizes relationships between RISC-V extensions that share instructions.

![Extension Graph](extension_graph.png)

---

# References

* [https://github.com/riscv/riscv-isa-manual](https://github.com/riscv/riscv-isa-manual)
* [https://github.com/rpsene/riscv-extensions-landscape](https://github.com/rpsene/riscv-extensions-landscape)

---

# Author

Swayam

Linux Foundation LFX Mentorship Applicant
