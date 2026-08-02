# Python Logic Lab

**Learn programming logic through tested code, scientific foundations, and open-source practices.**

[![Python quality](https://github.com/matheusflorindo32/dio-estudos-logica-python/actions/workflows/python-tests.yml/badge.svg)](https://github.com/matheusflorindo32/dio-estudos-logica-python/actions/workflows/python-tests.yml)
[![Python 3.11–3.14](https://img.shields.io/badge/Python-3.11%E2%80%933.14-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Ruff](https://img.shields.io/badge/code_style-Ruff-D7FF64?logo=ruff&logoColor=black)](https://docs.astral.sh/ruff/)
[![mypy](https://img.shields.io/badge/types-mypy-2A6DB2)](https://mypy-lang.org/)
[![MIT license](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

**English** · [Português do Brasil](README.pt-BR.md)

> DIO evaluators: [full Portuguese version available here](README.pt-BR.md).

[Official Wiki](https://github.com/matheusflorindo32/dio-estudos-logica-python/wiki) · [Quick start](#quick-start) · [Learning path](#learning-path) · [Contributing](#contributing)

An open educational repository for learning programming logic with small, executable Python programs. It combines an incremental study path, peer-reviewed computing-education research, automated tests, static analysis, and a published GitHub Wiki.

## Overview

An open-source learning laboratory for programming logic with Python, combining progressive examples, automated tests, software quality checks, and published scientific literature. It is designed for beginners, DIO learners, educators, and contributors who want a compact project whose claims can be reproduced locally and in CI.

## Why this repository exists

The project turns introductory concepts into observable behavior: each challenge can be run from the terminal, its business rules can be imported, and relevant success, boundary, and failure paths are tested. It also demonstrates a transparent open-source workflow using Issues, branches, pull requests, continuous integration, community files, and documentation.

## Learning outcomes

After completing the path, learners should be able to:

- model simple problems with variables, operators, conditions, loops, functions, and lists;
- distinguish reusable business logic from terminal input and output;
- validate inputs and handle predictable errors with useful messages;
- use type hints, docstrings, focused functions, and immutable views where appropriate;
- test normal, boundary, invalid-input, and command-line behaviors with pytest;
- run lint, formatting, type, coverage, and compatibility checks locally.

## Learning path

| Stage | Focus | Practice |
|---|---|---|
| 1 | Variables, types, and operators | `desafios/01_variaveis.py` |
| 2 | Conditions and boundaries | `desafios/02_condicionais.py` |
| 3 | `for`, `while`, and loop control | `desafios/03_repeticoes.py` |
| 4 | Functions, contracts, and type hints | `desafios/04_funcoes.py` |
| 5 | Lists, search, ordering, and removal | `desafios/05_listas.py` |
| 6 | Testable terminal applications | `exemplos/` and `tests/` |

See the [five-week study plan](docs/plano-de-estudos.md) and the [official Wiki](https://github.com/matheusflorindo32/dio-estudos-logica-python/wiki) for explanations, guided activities, independent exercises, and references.

## Quick start

Requirements: Python 3.11–3.14 and Git. The programs use only the Python standard library; development tools are isolated in `requirements-dev.txt`.

### Windows PowerShell

```powershell
git clone https://github.com/matheusflorindo32/dio-estudos-logica-python.git
Set-Location dio-estudos-logica-python
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
python -m pytest -v
```

### Linux and macOS

```bash
git clone https://github.com/matheusflorindo32/dio-estudos-logica-python.git
cd dio-estudos-logica-python
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements-dev.txt
python3 -m pytest -v
```

## Practical examples

Run an interactive program from the repository root:

```bash
python exemplos/calculadora.py
python exemplos/organizador_estudos.py
python exemplos/verificador_aprovacao.py
```

Import the same rules without starting the terminal interface:

```python
from exemplos.calculadora import calcular

result = calcular(12, "/", 4)
print(result)  # 3.0
```

The calculator validates operators and zero division. The study organizer validates descriptions and identifiers, while exposing tasks as an immutable tuple. These behaviors are covered by unit and command-line smoke tests.

## Quality gates

The current local baseline is **76 passing tests** and **100% combined line and branch coverage** across `desafios/` and `exemplos/`. The enforced minimum is 90%; reproduce the result instead of relying on a static coverage badge:

```bash
python -m compileall .
python -m ruff check .
python -m ruff format --check .
python -m mypy exemplos desafios
python -m pytest --cov=exemplos --cov=desafios --cov-branch --cov-report=term-missing
```

GitHub Actions runs the complete quality job on Python 3.14 and executes the test suite on Python 3.11, 3.12, 3.13, and 3.14. See the [quality guide](docs/quality.md) for scope and interpretation.

## Test coverage

pytest-cov measures both statements and decision branches. The configuration rejects coverage below 90%, reports missing lines and partial branches in the terminal, generates local HTML and XML reports, and uploads the XML report from CI. Generated reports are deliberately excluded from version control.

## Repository map

```text
.
├── .github/          # CI workflow and contribution templates
├── desafios/         # Incremental fundamentals exercises
├── exemplos/         # Testable terminal applications
├── tests/            # Unit, boundary, error, and CLI tests
├── wiki/             # Versioned sources for the official Wiki
├── docs/             # Study, quality, science, and delivery records
├── README.md         # International English documentation
├── README.pt-BR.md   # Equivalent Brazilian Portuguese documentation
├── pyproject.toml    # Project and tool configuration
└── requirements-dev.txt
```

## Evidence-informed teaching

The teaching approach uses progressive examples, explicit tracing, boundary tests, and separation of concerns. Its foundation is documented with published literature on novice misconceptions, error patterns, cognitive load, computational thinking, and learning strategies. Bibliographic metadata and persistent DOI links are recorded in [Scientific foundation](docs/scientific-foundation.md); documentation policy excludes unpublished manuscripts from the active bibliography.

Recommended books used as complementary references are Eric Matthes's *Python Crash Course*, 3rd edition (No Starch Press, 2023), and Luciano Ramalho's *Fluent Python*, 2nd edition (O'Reilly Media, 2022).

Key sources include Robins, Rountree, and Rountree on learning programming ([DOI](https://doi.org/10.1076/csed.13.2.137.14200)); Lahtinen, Ala-Mutka, and Järvinen on novice difficulties ([DOI](https://doi.org/10.1145/1151954.1067453)); Sweller on cognitive load ([DOI](https://doi.org/10.1207/s15516709cog1202_4)); and Duran, Zavgorodniaia, and Sorva on cognitive load research in computing education ([DOI](https://doi.org/10.1145/3483843)). Language behavior is grounded in the [Python 3.14 documentation](https://docs.python.org/3.14/).

## Official Wiki

The [published Wiki](https://github.com/matheusflorindo32/dio-estudos-logica-python/wiki) contains five connected pages with prerequisites, learning objectives, annotated examples, walkthroughs, common errors, good practices, guided and independent exercises, repository links, and persistent references.

## Internationalization

English is the international landing language; Brazilian Portuguese is the complete learner-facing counterpart. Exercises and the Wiki remain in Brazilian Portuguese to preserve a coherent curriculum and API. See the [synchronization policy](docs/internationalization.md).

## Documentation

- [Official GitHub Wiki](https://github.com/matheusflorindo32/dio-estudos-logica-python/wiki)
- [Study plan](docs/plano-de-estudos.md)
- [Quality assurance](docs/quality.md)
- [Scientific foundation](docs/scientific-foundation.md)
- [Internationalization strategy](docs/internationalization.md)
- [GitHub resources and delivery evidence](docs/recursos-github-utilizados.md)

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md), the [didactic contribution guide](docs/guia-de-contribuicao.md), and the [Code of Conduct](CODE_OF_CONDUCT.md). Keep changes focused, open an Issue when appropriate, add or update tests, and run every quality command before submitting a pull request.

## Roadmap

- maintain compatibility with supported Python releases;
- expand exercises only when they add a clear learning outcome and useful tests;
- evolve accessibility and navigation through learner feedback;
- evaluate additional languages only with an accountable reviewer and synchronization process.

## License

Distributed under the [MIT License](LICENSE).

## Author

Created and maintained by **Matheus Florindo de Deus**.
