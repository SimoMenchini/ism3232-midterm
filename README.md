# ISM3232 Midterm: Seabreeze Inn

- **Name:** Simone Menchini
- **Version:** 1.0.0
- **Date:** October 25, 2026

## What This Program Does

This program calculates pricing, discounts, cleaning fees, and eligibility checks for guest reservations at Seabreeze Inn. It processes reservation records to evaluate total booking amounts, determine which guests require credit checks, and assign welcome packages. Finally, it prints a formatted summary report to the terminal displaying individual stay details along with aggregate hotel metrics.

## Business Rules

1. The room cost is the nightly rate times the number of nights.
2. Stays of fewer than 4 nights receive no duration discount, stays from 4 to 13 nights receive a 6% discount, and stays of 14 nights or more receive an 18% discount.
3. Corporate-account guests always get at least the 6% discount, even on stays of fewer than 4 nights.
4. A $40 cleaning fee is added when the discounted cost is $300 or less.
5. A stay total of $2,000 or more requires a credit check.
6. A stay gets a welcome package when it runs more than 5 nights and its stay total is $1,000 or more.

## How to Run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

## How to Test

ruff check .
pytest -v

I wrote 23 automated unit tests covering all eight business functions, boundary values, corporate overrides, and list aggregation.

## Files in This Repository

.gitignore: Configures Git to ignore the virtual environment directory and Python bytecode cache folders.
README.md: Documents project specifications, operational instructions, testing steps, file contents, and course disclosures.
business_rules.py: Contains defined business constants and calculation functions for room rates, discounts, fees, and aggregates.
commands.md: Records terminal output verifying project construction, virtual environment activation, tree structure, search results, and Git commits.
main.py: Imports business calculation functions, processes the dataset of stays, and prints the terminal report.
requirements.txt: Records the specific virtual environment dependencies including pytest and ruff.
tests/__init__.py: Marks the test directory as an importable Python package.
tests/test_business_rules.py : Contains the unit test suite verifying function outputs against expected rules and boundary limits.

## AI Use Statement

I did not use AI on this exam.