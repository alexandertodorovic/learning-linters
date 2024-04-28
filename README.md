# On Learning Linters
This project is designed to help you get started with Python linters, specifically `ruff` and `pre-commit`.

## Setup Instructions
Begin by setting up your development environment:

1. **Create a CodeSpace:** Start by creating a GitHub CodeSpace for your project.
2. **Install Poetry:**
   - Run `pipx install poetry` in the terminal.
3. **Install Ruff:**
   - Run `pipx install ruff` in the terminal.
4. **Install Pre-Commit:**
   - Run `pipx install pre-commit` in the terminal.

## Running a Linter on a Template
Follow these steps to lint your Python code using `ruff`:

1. **Prepare the File:**
   - Copy the template from [`templates/times_nolinter.py`](templates/times_nolinter.py) and rename it to `times.py`.
2. **Linting with Ruff:**
   - To lint your file, run `ruff check times.py` in the terminal.
   - For additional parameters and options, you can run `ruff check -h`.

These instructions will guide you through using linters to improve the quality and consistency of your Python code.
