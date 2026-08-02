# Quality assurance

This project treats executable behavior, formatting, static analysis, test coverage, and interpreter compatibility as separate quality signals. A change is ready only when every applicable gate passes.

## Local quality gate

From an activated virtual environment, run:

```bash
python -m compileall .
python -m ruff check .
python -m ruff format --check .
python -m mypy exemplos desafios
python -m pytest --cov=exemplos --cov=desafios --cov-branch --cov-report=term-missing --cov-report=xml:coverage.xml --cov-report=html:htmlcov
```

| Gate | Purpose | Enforced scope |
|---|---|---|
| `compileall` | Detect syntax and import-time compilation errors | Repository Python files |
| Ruff lint | Detect selected correctness, import, modernization, and simplification issues | Entire repository |
| Ruff format | Keep Python formatting deterministic | Entire repository |
| mypy | Check declared contracts and typed function bodies | `exemplos/`, `desafios/` |
| pytest | Verify business rules, boundaries, failures, and command-line entry points | `tests/` |
| pytest-cov | Measure line and branch execution | `exemplos/`, `desafios/` |

## Coverage policy

Coverage uses branch measurement and fails below **90%**. The verified local result for this upgrade is **76 tests passed**, **100% line coverage**, and **100% branch coverage** over the learning programs. Coverage is evidence of exercised code, not proof that every requirement is correct; assertions and boundary selection remain subject to review.

Generated `.coverage`, `coverage.xml`, and `htmlcov/` outputs are ignored by Git. CI uploads `coverage.xml` as a 14-day diagnostic artifact and writes the combined percentage to the run summary. The README intentionally has no coverage badge because no external service is configured to publish a trustworthy, commit-specific value.

## Continuous integration

The `Quality` job uses Python 3.14 and runs compilation, Ruff lint and format checks, mypy, pytest, and branch coverage. A separate matrix runs compilation and tests on Python 3.11, 3.12, 3.13, and 3.14 with `fail-fast: false`, so a failure in one interpreter does not hide the others.

The workflow grants only read access to repository contents. It uses pinned major releases of official GitHub Actions and does not require repository secrets.

## Adding tests

Prefer tests that add decision value:

- one representative successful path;
- exact boundary values where classifications change;
- malformed, empty, or unsupported input;
- domain errors and useful exception messages;
- a smoke path through each `main()` interface;
- state transitions such as add, complete, find, and remove.

Avoid assertions that merely repeat implementation details or exist only to increase a percentage.
