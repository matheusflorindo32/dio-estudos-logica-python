# Estudos de Lógica de Programação com Python

[![Testes Python](https://github.com/matheusflorindo32/dio-estudos-logica-python/actions/workflows/python-tests.yml/badge.svg)](https://github.com/matheusflorindo32/dio-estudos-logica-python/actions/workflows/python-tests.yml)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Licença MIT](https://img.shields.io/badge/licen%C3%A7a-MIT-green.svg)](LICENSE)

Repositório educacional com exemplos simples, testáveis e comentados sobre os fundamentos da lógica de programação usando Python. O projeto foi criado para o desafio da DIO **“Utilizando Recursos do GitHub em um Projeto Open Source”**.

## Objetivo do desafio

Praticar lógica de programação e demonstrar, em um projeto individual legítimo, um fluxo open source com documentação, templates, Issue, branch, Pull Request, automação de testes e Wiki.

## Conteúdos estudados

- variáveis, tipos de dados e operadores;
- estruturas condicionais com `if`, `elif` e `else`;
- repetições com `for` e `while`;
- funções, parâmetros, retornos, docstrings e type hints;
- listas, ordenação, busca, remoção e compreensão de listas;
- separação entre lógica de negócio e interface de terminal;
- testes automatizados com pytest.

## Recursos do GitHub utilizados

- repositório público e licença MIT;
- templates de Issue e Pull Request;
- branch de funcionalidade e Pull Request ligado a uma Issue;
- GitHub Actions para Python 3.11 e 3.12;
- documentação preparada para GitHub Wiki;
- arquivos comunitários: `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md` e `CHANGELOG.md`.

Os registros verificáveis estão em [docs/recursos-github-utilizados.md](docs/recursos-github-utilizados.md) e [docs/evidencias-entrega.md](docs/evidencias-entrega.md).

## Estrutura do projeto

```text
dio-estudos-logica-python/
├── .github/                 # Templates e workflow de integração contínua
├── desafios/                # Exercícios didáticos de fundamentos
├── docs/                    # Guias, plano e evidências da entrega
├── exemplos/                # Aplicações de terminal com lógica testável
├── tests/                   # Testes automatizados
├── wiki/                    # Fontes das páginas da Wiki
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── pyproject.toml
└── requirements-dev.txt
```

## Requisitos

- Python 3.11 ou superior;
- Git, para trabalhar com branches e contribuições;
- pytest, instalado por `requirements-dev.txt`, para executar os testes.

O projeto não possui dependências de execução além da biblioteca padrão do Python.

## Instalação

### PowerShell (Windows)

```powershell
git clone https://github.com/matheusflorindo32/dio-estudos-logica-python.git
Set-Location dio-estudos-logica-python
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

### Bash (Linux e macOS)

```bash
git clone https://github.com/matheusflorindo32/dio-estudos-logica-python.git
cd dio-estudos-logica-python
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements-dev.txt
```

## Executando os exemplos

Cada arquivo pode ser executado isoladamente a partir da raiz do projeto:

```powershell
python .\exemplos\calculadora.py
python .\exemplos\organizador_estudos.py
python .\exemplos\verificador_aprovacao.py
python .\desafios\02_condicionais.py
```

No Bash, substitua as barras invertidas por `/` e, se necessário, use `python3`.

### Exemplo de uso

```text
Primeiro número: 12
Operação (+, -, *, /): /
Segundo número: 4
Resultado: 3
```

As regras também podem ser importadas sem iniciar a interface:

```python
from exemplos.calculadora import dividir

resultado = dividir(12, 4)
print(resultado)  # 3.0
```

## Executando os testes

```powershell
python -m compileall .
python -m pytest -v
```

No Bash, os mesmos comandos funcionam com `python3` quando esse for o nome do executável. O workflow em `.github/workflows/python-tests.yml` repete os testes no Ubuntu com Python 3.11 e 3.12.

## Fluxo individual com Issue, branch e Pull Request

O projeto demonstra colaboração sem inventar outra identidade:

1. o proprietário registra uma melhoria em uma Issue;
2. cria a branch `feature/estruturas-condicionais`;
3. implementa e testa a mudança;
4. abre um Pull Request relacionado à Issue;
5. aguarda o GitHub Actions;
6. faz o merge somente após os testes passarem.

Esse processo mantém discussão, código e automação rastreáveis mesmo em um projeto individual.

## Como contribuir

Leia [CONTRIBUTING.md](CONTRIBUTING.md) e o [Código de Conduta](CODE_OF_CONDUCT.md). Sugestões podem ser registradas pelas templates de Issue. Antes de abrir um Pull Request, execute a compilação e os testes.

## Licença

Distribuído sob a licença MIT. Consulte [LICENSE](LICENSE).

## Autor

**Matheus Florindo de Deus**

## Checklist da entrega DIO

- [x] exemplos de lógica de programação em Python;
- [x] testes automatizados e workflow de CI;
- [x] README e documentação open source;
- [x] templates de Issue e Pull Request;
- [x] licença MIT;
- [x] Wiki preparada no diretório `wiki/`;
- [x] Issue, Pull Request, merge e GitHub Actions confirmados;
- [ ] Wiki publicada — a inicialização manual ainda é necessária; consulte as evidências.
