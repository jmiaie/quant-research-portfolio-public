# Contributing

## Development setup

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Development workflow

1. Keep changes small and well-scoped.
2. Prefer deterministic examples and tests.
3. Run the local quality checks before opening or updating a pull request.
4. Document any new public example so a reviewer can reproduce it from a fresh checkout.

## Local checks

```bash
python -m ruff check .
python -m mypy src
python -m pytest
```

## Public-safe content rules

Do not commit:

- secrets, tokens, or credentials
- broker or exchange integrations
- proprietary research artifacts or private datasets
- large generated outputs from notebooks or experiments
- unsupported claims about strategy performance or live readiness

## Example design guidance

Examples should use synthetic or openly specified data, explain the research intent, and separate reusable code from experiment-specific logic. If a future contribution introduces notebook files, clear large outputs before committing them.
