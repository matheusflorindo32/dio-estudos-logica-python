<div align="center">

<h1>Python Logic Lab</h1>

<p>
  <strong>Evidence-Informed Programming Logic Laboratory</strong><br>
  A compact and reproducible path from programming fundamentals to automated software quality.
</p>

<p>
  <a href="./README.md"><strong>English</strong></a> ·
  <a href="./README.pt-BR.md">Português do Brasil</a>
</p>

<p>
  <a href="https://github.com/matheusflorindo32/dio-estudos-logica-python/actions/workflows/python-tests.yml">
    <img alt="CI status" src="https://github.com/matheusflorindo32/dio-estudos-logica-python/actions/workflows/python-tests.yml/badge.svg">
  </a>
  <a href="https://www.python.org/">
    <img alt="Python 3.11 to 3.14" src="https://img.shields.io/badge/Python-3.11%E2%80%933.14-3776AB?logo=python&logoColor=white">
  </a>
  <a href="https://docs.astral.sh/ruff/">
    <img alt="Ruff" src="https://img.shields.io/badge/code%20quality-Ruff-D7FF64?logo=ruff&logoColor=black">
  </a>
  <a href="https://mypy-lang.org/">
    <img alt="mypy" src="https://img.shields.io/badge/static%20types-mypy-2A6DB2">
  </a>
  <a href="./LICENSE">
    <img alt="MIT License" src="https://img.shields.io/badge/license-MIT-green.svg">
  </a>
  <a href="https://github.com/matheusflorindo32/dio-estudos-logica-python/wiki">
    <img alt="Official Wiki" src="https://img.shields.io/badge/wiki-published-0366D6">
  </a>
</p>

<p>
  <a href="#overview">Overview</a> ·
  <a href="#learning-path">Learning Path</a> ·
  <a href="#quick-start">Quick Start</a> ·
  <a href="#quality-gates">Quality</a> ·
  <a href="#scientific-foundation">Science</a> ·
  <a href="#documentation">Documentation</a>
</p>

</div>

DIO evaluators: the complete Brazilian Portuguese version is available in README.pt-BR.md.

Overview

Python Logic Lab is a compact open-source learning environment for introductory programming logic. It combines progressive Python examples, automated testing, static analysis, continuous integration, a published Wiki, and peer-reviewed computing-education literature.

Rather than presenting code only as reading material, the repository turns each concept into executable, testable, and reproducible software behavior.

Who this project is for

beginners learning programming logic with Python;

DIO learners completing open-source and GitHub challenges;

educators looking for small, testable teaching examples;

contributors who want a clear and auditable Python repository;

recruiters and reviewers assessing practical software-quality fundamentals.

Why this repository exists

Introductory programming repositories often explain syntax but do not show how to validate behavior, separate business logic from terminal input/output, or apply software-quality checks.

This project addresses that gap through:

small and progressive exercises;

explicit boundary and invalid-input cases;

importable business rules;

automated tests;

line and branch coverage;

lint and formatting checks;

static type verification;

multi-version Python compatibility;

published scientific and technical documentation.

Learning outcomes

After completing the learning path, learners should be able to:

model simple problems using variables, operators, conditions, loops, functions, and lists;

distinguish reusable business logic from terminal interaction;

validate inputs and handle predictable errors with clear messages;

use type hints, docstrings, and focused functions;

test normal, boundary, invalid-input, and command-line behavior;

run lint, formatting, type, coverage, and compatibility checks locally;

understand a practical GitHub workflow with Issues, branches, pull requests, CI, and Wiki documentation.

Learning path

Stage

Focus

Practice

Suggested level

01

Variables, data types, and operators

desafios/01_variaveis.py

Foundation

02

Conditions and boundary values

desafios/02_condicionais.py

Foundation

03

for, while, and loop control

desafios/03_repeticoes.py

Developing

04

Functions, contracts, and type hints

desafios/04_funcoes.py

Developing

05

Lists, search, ordering, and removal

desafios/05_listas.py

Intermediate

06

Testable terminal applications

exemplos/ and tests/

Applied

See the five-week study plan and the official Wiki for guided activities, independent exercises, common errors, and published references.

Pedagogical architecture

flowchart TB
    A["Published computing-education research"] --> D["Progressive learning sequence"]
    B["Documented novice difficulties"] --> E["Boundary and error cases"]
    C["Cognitive load principles"] --> F["Small, focused examples"]

    D --> G["Executable Python modules"]
    E --> H["Automated tests"]
    F --> I["Clear explanations and Wiki"]

    G --> J["Reproducible behavior"]
    H --> K["Verifiable quality"]
    I --> L["Transferable learning"]

The project is evidence-informed, not a claim of experimentally proven educational effectiveness. Its design is guided by published literature, while the repository itself verifies software behavior through code, tests, coverage, lint, typing, and CI.

Quick start

Requirements: Python 3.11–3.14 and Git.

The runtime examples use only the Python standard library. Development tools are isolated in requirements-dev.txt.

Windows PowerShell

git clone https://github.com/matheusflorindo32/dio-estudos-logica-python.git
Set-Location dio-estudos-logica-python

python -m venv .venv
.\.venv\Scripts\Activate.ps1

python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
python -m pytest -v

Linux and macOS

git clone https://github.com/matheusflorindo32/dio-estudos-logica-python.git
cd dio-estudos-logica-python

python3 -m venv .venv
source .venv/bin/activate

python3 -m pip install --upgrade pip
python3 -m pip install -r requirements-dev.txt
python3 -m pytest -v

Practical examples

Run the interactive programs from the repository root:

python exemplos/calculadora.py
python exemplos/organizador_estudos.py
python exemplos/verificador_aprovacao.py

Import the same rules without starting the terminal interface:

from exemplos.calculadora import calcular

result = calcular(12, "/", 4)
print(result)  # 3.0

This separation allows the same business rules to be reused by terminal interfaces, tests, APIs, or future graphical applications.

Quality gates

The current verified baseline is:

Check

Current result

Enforced policy

Tests

76 passing

All must pass

Combined line and branch coverage

100%

Minimum 90%

Ruff lint

0 errors

0 errors

Ruff formatting

Clean

No formatting drift

mypy

Clean

No type-checking errors

Python compatibility

3.11, 3.12, 3.13, 3.14

All supported versions

Reproduce the full quality pipeline locally:

python -m compileall .
python -m ruff check .
python -m ruff format --check .
python -m mypy exemplos desafios
python -m pytest --cov=exemplos --cov=desafios --cov-branch --cov-report=term-missing

GitHub Actions runs:

a complete quality job on Python 3.14;

the test suite on Python 3.11, 3.12, 3.13, and 3.14;

coverage reporting and artifact upload;

compilation, lint, formatting, typing, and tests.

See docs/quality.md for the complete policy and interpretation.

Test coverage

Coverage is measured with pytest-cov for both lines and branches.

The project:

reports missing lines and partial branches in the terminal;

rejects coverage below the configured minimum;

generates XML and HTML reports locally;

uploads coverage.xml from CI;

excludes generated coverage artifacts from version control.

The repository does not rely on a static coverage badge as proof. The authoritative source is the executable CI pipeline.

Why this repository is different

Dimension

Conventional introductory repository

Python Logic Lab

Research grounding

Often undocumented

Published sources with DOI

Examples

Usually isolated snippets

Executable modules

Tests

Limited or absent

Normal, boundary, error, and CLI cases

Coverage

Rarely measured

Line and branch coverage

Type hints

Optional

Enforced in core learning modules

Static analysis

Usually absent

Ruff and mypy

CI

Manual validation

GitHub Actions on four Python versions

Architecture

Logic often mixed with I/O

Importable business rules

Documentation

README only

README, docs, and official Wiki

Languages

Usually one

English and Brazilian Portuguese

Repository map

.
├── .github/              # CI workflow and contribution templates
├── desafios/             # Progressive fundamentals exercises
├── exemplos/             # Testable terminal applications
├── tests/                # Unit, boundary, error, and CLI tests
├── wiki/                 # Versioned sources for the official Wiki
├── docs/                 # Study, quality, science, i18n, and evidence
├── README.md             # International English version
├── README.pt-BR.md       # Brazilian Portuguese version
├── pyproject.toml        # Project and tool configuration
├── requirements-dev.txt  # Development dependencies
└── LICENSE               # MIT License

Scientific foundation

The project uses published and peer-reviewed literature to guide its instructional design. It does not use preprints in the active bibliography.

Key themes include:

novice programming difficulties;

misconceptions and error patterns;

cognitive load in computing education;

computational thinking;

progressive examples and explicit tracing;

code reuse, testability, and separation of concerns.

Selected references:

Topic

Published source

Learning programming

Robins, Rountree, and Rountree (2003), DOI

Novice difficulties

Lahtinen, Ala-Mutka, and Järvinen (2005), DOI

Cognitive load

Sweller (1988), DOI

Computing education

Duran, Zavgorodniaia, and Sorva (2022), DOI

Programming misconceptions

Herman et al. (2010), DOI

Complementary books:

Eric Matthes, Python Crash Course, 3rd ed., No Starch Press, 2023;

Luciano Ramalho, Fluent Python, 2nd ed., O'Reilly Media, 2022.

Language behavior is grounded in the official Python 3.14 documentation.

See the full bibliography in docs/scientific-foundation.md.

Official Wiki

The official Wiki includes five connected pages with:

prerequisites;

learning objectives;

annotated examples;

step-by-step explanations;

common errors;

good practices;

guided and independent exercises;

repository links;

persistent DOI references.

Documentation

Resource

Purpose

Language

Official Wiki

Structured learning pages and references

PT-BR

Study plan

Five-week guided progression

PT-BR

Quality guide

Tooling, coverage, CI, and interpretation

EN

Scientific foundation

Published bibliography and DOI links

EN

Internationalization

EN ↔ PT-BR synchronization policy

EN

GitHub resources

Delivery evidence and GitHub features

PT-BR

Internationalization

English is the international landing language. Brazilian Portuguese is the complete learner-facing counterpart.

The exercises and the official Wiki remain in Brazilian Portuguese to preserve curriculum consistency. Documentation changes should keep both README versions synchronized according to docs/internationalization.md.

Contributing

Before opening a pull request:

read CONTRIBUTING.md;

read the didactic contribution guide;

follow the Code of Conduct;

keep changes focused;

add or update tests;

run the complete quality pipeline locally.

Contribution principles:

preserve compatibility with supported Python versions;

expand exercises only when they add a clear learning outcome;

keep examples small, readable, and testable;

document behavior and edge cases;

keep English and Portuguese documentation synchronized.

Roadmap

maintain compatibility with supported Python releases;

expand exercises with clear learning outcomes and useful tests;

improve accessibility and navigation through learner feedback;

add lightweight demonstrations only when they improve understanding;

evaluate future language versions with accountable review and synchronization.

License

Distributed under the MIT License.

Author

Created and maintained by Matheus Florindo de Deus.

Systems Analysis and Development student at IFES;

multidisciplinary educator and researcher;

research collaborator in Translational Physiology at UFES;

ORCID: 0009-0006-3848-0662;

GitHub profile.

<div align="center">

Built with discipline, reproducibility, and open-source practice.

Don't negotiate with your mind.

</div>
