# Lab 5 — Static Code Analysis

Software Engineering  
**SRN:** PES1UG24CS176  
**Project:** E-Commerce Cart System

## Overview

This lab focuses on improving Python code quality, security, and formatting using three static analysis tools: Pylint, Bandit, and Flake8.

The assigned program, `ecommerce_cart_system.py`, implements basic shopping cart operations, discount calculations, checkout PIN generation, item hashing, and receipt export.

## Tools Used

- **Pylint:** Identifies code-quality issues, naming violations, and potential programming errors.
- **Bandit:** Detects potentially insecure coding patterns.
- **Flake8:** Checks Python formatting and PEP 8 compliance.

## Issues Addressed

- Replaced unsafe `eval()` usage with validated numeric discount calculations.
- Replaced MD5 with SHA-256 for item hashing.
- Used the `secrets` module to generate checkout PINs.
- Removed shell command execution from receipt export.
- Fixed the mutable default argument and broad exception handling.
- Improved function naming, documentation, file handling, and formatting.

## Analysis Results

| Tool | Initial Result | Final Result |
|---|---|---|
| Pylint | 3.86/10 | 10.00/10 |
| Bandit | 5 reported issues | No issues identified |
| Flake8 | 7 reported violations | No violations reported |

## Repository Contents

- `ecommerce_cart_system.py` — Corrected Python program.
- `issues.md` — Issues identified and their fixes.
- `pylint_report_before.txt` and `pylint_report_after.txt` — Pylint reports.
- `bandit_report_before.txt` and `bandit_report_after.txt` — Bandit reports.
- `flake8_report_before.txt` and `flake8_report_after.txt` — Flake8 reports.

## How to Run

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the analysis tools:

```bash
pip install pylint bandit flake8
```

Run the program:

```bash
python ecommerce_cart_system.py
```

Run static analysis:

```bash
pylint ecommerce_cart_system.py
bandit -r ecommerce_cart_system.py
flake8 ecommerce_cart_system.py
```

## Conclusion

Static analysis helped identify and correct security vulnerabilities, code-quality problems, and formatting violations. After the fixes, the program achieved a Pylint score of 10.00/10, with no findings reported by Bandit or Flake8.
