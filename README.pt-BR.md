# Laboratório de Lógica com Python

**Aprenda lógica de programação com código testado, fundamentação científica e práticas open source.**

[![Qualidade Python](https://github.com/matheusflorindo32/dio-estudos-logica-python/actions/workflows/python-tests.yml/badge.svg)](https://github.com/matheusflorindo32/dio-estudos-logica-python/actions/workflows/python-tests.yml)
[![Python 3.11–3.14](https://img.shields.io/badge/Python-3.11%E2%80%933.14-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Ruff](https://img.shields.io/badge/estilo-Ruff-D7FF64?logo=ruff&logoColor=black)](https://docs.astral.sh/ruff/)
[![mypy](https://img.shields.io/badge/tipos-mypy-2A6DB2)](https://mypy-lang.org/)
[![Licença MIT](https://img.shields.io/badge/licen%C3%A7a-MIT-green.svg)](LICENSE)

[English](README.md) · **Português do Brasil**

[Wiki oficial](https://github.com/matheusflorindo32/dio-estudos-logica-python/wiki) · [Início rápido](#início-rápido) · [Trilha de aprendizagem](#trilha-de-aprendizagem) · [Como contribuir](#como-contribuir)

Repositório educacional aberto para aprender lógica de programação com programas Python pequenos e executáveis. O projeto combina uma trilha incremental, pesquisas revisadas por pares sobre educação em computação, testes automatizados, análise estática e uma Wiki oficial publicada no GitHub.

## Visão geral

Um laboratório educacional open source para lógica de programação com Python, combinando exemplos progressivos, testes automatizados, controles de qualidade de software e literatura científica publicada. Foi criado para iniciantes, estudantes da DIO, docentes e contribuidores que desejam um projeto compacto cujas afirmações possam ser reproduzidas localmente e no CI.

## Por que este repositório existe

O projeto transforma conceitos introdutórios em comportamentos observáveis: cada desafio pode ser executado no terminal, suas regras de negócio podem ser importadas e os caminhos relevantes de sucesso, fronteira e falha são testados. Ele também demonstra um fluxo open source transparente com Issues, branches, Pull Requests, integração contínua, arquivos comunitários e documentação.

## Resultados de aprendizagem

Ao concluir a trilha, a pessoa estudante deverá ser capaz de:

- modelar problemas simples com variáveis, operadores, condições, repetições, funções e listas;
- diferenciar lógica de negócio reutilizável de entrada e saída do terminal;
- validar entradas e tratar erros previsíveis com mensagens úteis;
- empregar type hints, docstrings, funções focadas e visões imutáveis quando apropriado;
- testar comportamentos normais, limites, entradas inválidas e interfaces de terminal com pytest;
- executar verificações locais de lint, formatação, tipos, cobertura e compatibilidade.

## Trilha de aprendizagem

| Etapa | Foco | Prática |
|---|---|---|
| 1 | Variáveis, tipos e operadores | `desafios/01_variaveis.py` |
| 2 | Condições e valores de fronteira | `desafios/02_condicionais.py` |
| 3 | `for`, `while` e controle de repetição | `desafios/03_repeticoes.py` |
| 4 | Funções, contratos e type hints | `desafios/04_funcoes.py` |
| 5 | Listas, busca, ordenação e remoção | `desafios/05_listas.py` |
| 6 | Aplicações de terminal testáveis | `exemplos/` e `tests/` |

Consulte o [plano de estudos de cinco semanas](docs/plano-de-estudos.md) e a [Wiki oficial](https://github.com/matheusflorindo32/dio-estudos-logica-python/wiki) para encontrar explicações, atividades guiadas, exercícios independentes e referências.

## Início rápido

Requisitos: Python 3.11–3.14 e Git. Os programas usam apenas a biblioteca padrão do Python; as ferramentas de desenvolvimento estão isoladas em `requirements-dev.txt`.

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

### Linux e macOS

```bash
git clone https://github.com/matheusflorindo32/dio-estudos-logica-python.git
cd dio-estudos-logica-python
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements-dev.txt
python3 -m pytest -v
```

## Exemplos práticos

Execute uma aplicação interativa a partir da raiz do repositório:

```bash
python exemplos/calculadora.py
python exemplos/organizador_estudos.py
python exemplos/verificador_aprovacao.py
```

Importe as mesmas regras sem iniciar a interface de terminal:

```python
from exemplos.calculadora import calcular

resultado = calcular(12, "/", 4)
print(resultado)  # 3.0
```

A calculadora valida operadores e divisão por zero. O organizador de estudos valida descrições e identificadores, além de expor as tarefas como uma tupla imutável. Esses comportamentos são cobertos por testes unitários e smoke tests da linha de comando.

## Controles de qualidade

A linha de base local atual é de **76 testes aprovados** e **100% de cobertura combinada de linhas e branches** em `desafios/` e `exemplos/`. O mínimo exigido é 90%; reproduza o resultado em vez de depender de um badge estático de cobertura:

```bash
python -m compileall .
python -m ruff check .
python -m ruff format --check .
python -m mypy exemplos desafios
python -m pytest --cov=exemplos --cov=desafios --cov-branch --cov-report=term-missing
```

O GitHub Actions executa o job completo de qualidade no Python 3.14 e roda a suíte de testes no Python 3.11, 3.12, 3.13 e 3.14. Consulte o [guia de qualidade](docs/quality.md) para entender escopo e interpretação.

## Cobertura de testes

O pytest-cov mede instruções e branches de decisão. A configuração reprova cobertura abaixo de 90%, informa linhas ausentes e branches parciais no terminal, gera relatórios locais em HTML e XML e envia o XML a partir do CI. Os relatórios gerados são intencionalmente excluídos do versionamento.

## Mapa do repositório

```text
.
├── .github/          # Workflow de CI e templates de colaboração
├── desafios/         # Exercícios incrementais de fundamentos
├── exemplos/         # Aplicações de terminal testáveis
├── tests/            # Testes unitários, de fronteira, erro e CLI
├── wiki/             # Fontes versionadas da Wiki oficial
├── docs/             # Estudos, qualidade, ciência e evidências
├── README.md         # Documentação internacional em inglês
├── README.pt-BR.md   # Documentação equivalente em português
├── pyproject.toml    # Configuração do projeto e das ferramentas
└── requirements-dev.txt
```

## Ensino fundamentado em evidências

A abordagem didática usa exemplos progressivos, rastreamento explícito, testes de fronteira e separação de responsabilidades. Sua fundamentação reúne literatura publicada sobre concepções equivocadas de iniciantes, padrões de erro, carga cognitiva, pensamento computacional e estratégias de aprendizagem. Os metadados bibliográficos e links DOI persistentes estão em [Fundamentação científica](docs/scientific-foundation.md); a política documental exclui manuscritos não publicados da bibliografia ativa.

Os livros recomendados e usados como referências complementares são *Python Crash Course*, 3ª edição, de Eric Matthes (No Starch Press, 2023), e *Fluent Python*, 2ª edição, de Luciano Ramalho (O'Reilly Media, 2022).

As fontes centrais incluem Robins, Rountree e Rountree sobre aprendizagem de programação ([DOI](https://doi.org/10.1076/csed.13.2.137.14200)); Lahtinen, Ala-Mutka e Järvinen sobre dificuldades de iniciantes ([DOI](https://doi.org/10.1145/1151954.1067453)); Sweller sobre carga cognitiva ([DOI](https://doi.org/10.1207/s15516709cog1202_4)); e Duran, Zavgorodniaia e Sorva sobre carga cognitiva na educação em computação ([DOI](https://doi.org/10.1145/3483843)). O comportamento da linguagem se baseia na [documentação do Python 3.14](https://docs.python.org/3.14/).

## Wiki oficial

A [Wiki publicada](https://github.com/matheusflorindo32/dio-estudos-logica-python/wiki) contém cinco páginas conectadas com pré-requisitos, objetivos, exemplos comentados, leitura passo a passo, erros comuns, boas práticas, exercícios guiados e independentes, ligações com o repositório e referências persistentes.

## Internacionalização

O inglês é o idioma internacional de entrada; o português do Brasil é a contraparte integral voltada à aprendizagem. Os exercícios e a Wiki permanecem em português para preservar um currículo e uma API coerentes. Consulte a [política de sincronização](docs/internationalization.md).

## Documentação

- [Wiki oficial no GitHub](https://github.com/matheusflorindo32/dio-estudos-logica-python/wiki)
- [Plano de estudos](docs/plano-de-estudos.md)
- [Garantia de qualidade](docs/quality.md)
- [Fundamentação científica](docs/scientific-foundation.md)
- [Estratégia de internacionalização](docs/internationalization.md)
- [Recursos do GitHub e evidências](docs/recursos-github-utilizados.md)

## Como contribuir

Leia [CONTRIBUTING.md](CONTRIBUTING.md), o [guia didático de contribuição](docs/guia-de-contribuicao.md) e o [Código de Conduta](CODE_OF_CONDUCT.md). Mantenha as mudanças focadas, abra uma Issue quando apropriado, adicione ou atualize testes e execute todos os comandos de qualidade antes de enviar um Pull Request.

## Roadmap

- manter compatibilidade com as versões de Python suportadas;
- ampliar exercícios somente quando houver objetivo de aprendizagem claro e testes úteis;
- evoluir acessibilidade e navegação a partir de feedback de estudantes;
- avaliar novos idiomas apenas com revisor responsável e processo de sincronização.

## Licença

Distribuído sob a [Licença MIT](LICENSE).

## Autor

Criado e mantido por **Matheus Florindo de Deus**.
