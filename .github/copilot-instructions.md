# Project Instructions

## Project

Smart Sales Data Manager is a Python CLI application for cleaning and analyzing sales CSV data.

## Software Engineering Principles

- Follow Separation of Concerns.
- Keep each module focused on one responsibility.
- Follow the Single Responsibility Principle.
- Prefer modular and maintainable code.
- Avoid unnecessary coupling between modules.
- Follow the DRY principle and avoid unnecessary duplication.
- Keep the design simple and understandable.

## Clean Code Rules

- Keep the code simple, readable, and maintainable.
- Use clear and descriptive names.
- Keep each function focused on one responsibility.
- Avoid unnecessary complexity.
- Write small and focused functions.
- Add comments or docstrings only when they provide useful information.

## Project Structure

- Keep input/output operations in `io.py`.
- Keep data cleaning logic in `cleaning.py`.
- Keep data analysis logic in `analysis.py`.
- Keep command-line execution in `cli.py`.
- Do not mix responsibilities between modules without a clear reason.

## Testing

- Run `pytest -q` after code changes.
- The project must maintain 15 passing tests.
- Do not modify tests unless explicitly requested.
- Do not consider a change complete if tests fail.

## Git

- Make small, focused commits.
- Use clear commit messages.
- Review changes before committing.
- Check `git diff` before committing.
- Keep the working tree clean after completing a task.

## Vibe Coding

- Use AI as an assistant, not as an automatic decision maker.
- Explain the proposed changes before applying them when possible.
- Review generated code before accepting it.
- Do not accept suggestions blindly.
- Prefer changes that follow the project architecture and requirements.
- Run tests after AI-generated code changes.

## Data Safety

- Do not commit secrets, credentials, API keys, or private data.
- Use synthetic sample data for development.
- Do not add unnecessary data files to Git.
