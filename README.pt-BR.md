<div align="center">

<h1>Laboratório de Lógica com Python</h1>

<p>
  <strong>Laboratório de Lógica de Programação Orientado por Evidências</strong><br>
  Uma trilha compacta e reproduzível dos fundamentos da programação à qualidade automatizada de software.
</p>

<p>
  <a href="./README.md">English</a> ·
  <a href="./README.pt-BR.md"><strong>Português do Brasil</strong></a>
</p>

<p>
  <a href="https://github.com/matheusflorindo32/dio-estudos-logica-python/actions/workflows/python-tests.yml">
    <img alt="Status do CI" src="https://github.com/matheusflorindo32/dio-estudos-logica-python/actions/workflows/python-tests.yml/badge.svg">
  </a>
  <a href="https://www.python.org/">
    <img alt="Python 3.11 a 3.14" src="https://img.shields.io/badge/Python-3.11%E2%80%933.14-3776AB?logo=python&logoColor=white">
  </a>
  <a href="https://docs.astral.sh/ruff/">
    <img alt="Ruff" src="https://img.shields.io/badge/qualidade%20de%20c%C3%B3digo-Ruff-D7FF64?logo=ruff&logoColor=black">
  </a>
  <a href="https://mypy-lang.org/">
    <img alt="mypy" src="https://img.shields.io/badge/tipos%20est%C3%A1ticos-mypy-2A6DB2">
  </a>
  <a href="./LICENSE">
    <img alt="Licença MIT" src="https://img.shields.io/badge/licen%C3%A7a-MIT-green.svg">
  </a>
  <a href="https://github.com/matheusflorindo32/dio-estudos-logica-python/wiki">
    <img alt="Wiki oficial" src="https://img.shields.io/badge/wiki-publicada-0366D6">
  </a>
</p>

<p>
  <a href="#visão-geral">Visão geral</a> ·
  <a href="#trilha-de-aprendizagem">Trilha</a> ·
  <a href="#início-rápido">Início rápido</a> ·
  <a href="#controles-de-qualidade">Qualidade</a> ·
  <a href="#fundamentação-científica">Ciência</a> ·
  <a href="#documentação">Documentação</a>
</p>

</div>

Visão geral

O Laboratório de Lógica com Python é um ambiente educacional open source, compacto e voltado aos fundamentos da lógica de programação. O projeto combina exemplos progressivos em Python, testes automatizados, análise estática, integração contínua, Wiki publicada e literatura científica revisada por pares na área de educação em computação.

Em vez de apresentar código apenas como material de leitura, o repositório transforma cada conceito em comportamento de software executável, testável e reproduzível.

Para quem é este projeto

iniciantes em lógica de programação com Python;

estudantes da DIO em desafios de GitHub e open source;

professores que buscam exemplos pequenos e testáveis;

colaboradores interessados em um repositório claro e auditável;

recrutadores e avaliadores que desejam verificar fundamentos práticos de qualidade de software.

Por que este repositório existe

Repositórios introdutórios frequentemente explicam sintaxe, mas nem sempre mostram como validar comportamentos, separar regras de negócio da entrada e saída do terminal ou aplicar controles básicos de qualidade.

Este projeto trabalha essas lacunas por meio de:

exercícios pequenos e progressivos;

casos de limite e entradas inválidas;

regras de negócio importáveis;

testes automatizados;

cobertura de linhas e ramificações;

verificação de lint e formatação;

análise estática de tipos;

compatibilidade com múltiplas versões do Python;

documentação científica e técnica publicada.

Resultados de aprendizagem

Ao concluir a trilha, o estudante deverá ser capaz de:

modelar problemas simples com variáveis, operadores, condições, repetições, funções e listas;

separar regras reutilizáveis da interação com o terminal;

validar entradas e tratar erros previsíveis com mensagens claras;

utilizar type hints, docstrings e funções com responsabilidades bem definidas;

testar comportamentos normais, limites, entradas inválidas e fluxos de linha de comando;

executar verificações de lint, formatação, tipos, cobertura e compatibilidade;

compreender um fluxo prático de GitHub com Issues, branches, Pull Requests, CI e Wiki.

Trilha de aprendizagem

Etapa

Foco

Prática

Nível sugerido

01

Variáveis, tipos de dados e operadores

desafios/01_variaveis.py

Fundamentos

02

Condições e valores de fronteira

desafios/02_condicionais.py

Fundamentos

03

for, while e controle de repetição

desafios/03_repeticoes.py

Em desenvolvimento

04

Funções, contratos e type hints

desafios/04_funcoes.py

Em desenvolvimento

05

Listas, busca, ordenação e remoção

desafios/05_listas.py

Intermediário

06

Aplicações de terminal testáveis

exemplos/ e tests/

Aplicado

Consulte o plano de estudos de cinco semanas e a Wiki oficial para atividades guiadas, exercícios independentes, erros comuns e referências publicadas.

Arquitetura pedagógica

flowchart TB
    A["Pesquisa publicada em educação em computação"] --> D["Sequência progressiva de aprendizagem"]
    B["Dificuldades documentadas de iniciantes"] --> E["Casos de fronteira e erro"]
    C["Princípios de carga cognitiva"] --> F["Exemplos pequenos e focados"]

    D --> G["Módulos Python executáveis"]
    E --> H["Testes automatizados"]
    F --> I["Explicações claras e Wiki"]

    G --> J["Comportamento reproduzível"]
    H --> K["Qualidade verificável"]
    I --> L["Aprendizagem transferível"]

O projeto é orientado por evidências, mas não afirma eficácia educacional experimentalmente comprovada. Seu desenho é guiado por literatura publicada, enquanto o próprio repositório verifica o comportamento do software por meio de código, testes, cobertura, lint, tipagem e CI.

Início rápido

Requisitos: Python 3.11–3.14 e Git.

Os exemplos em execução utilizam apenas a biblioteca padrão do Python. As ferramentas de desenvolvimento ficam isoladas em requirements-dev.txt.

Windows PowerShell

git clone https://github.com/matheusflorindo32/dio-estudos-logica-python.git
Set-Location dio-estudos-logica-python

python -m venv .venv
.\.venv\Scripts\Activate.ps1

python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
python -m pytest -v

Linux e macOS

git clone https://github.com/matheusflorindo32/dio-estudos-logica-python.git
cd dio-estudos-logica-python

python3 -m venv .venv
source .venv/bin/activate

python3 -m pip install --upgrade pip
python3 -m pip install -r requirements-dev.txt
python3 -m pytest -v

Exemplos práticos

Execute os programas interativos a partir da raiz:

python exemplos/calculadora.py
python exemplos/organizador_estudos.py
python exemplos/verificador_aprovacao.py

Importe as mesmas regras sem iniciar a interface de terminal:

from exemplos.calculadora import calcular

resultado = calcular(12, "/", 4)
print(resultado)  # 3.0

Essa separação permite que as mesmas regras sejam reutilizadas por interfaces de terminal, testes, APIs ou futuras aplicações gráficas.

Controles de qualidade

A linha de base atualmente verificada é:

Verificação

Resultado atual

Política aplicada

Testes

76 aprovados

Todos devem passar

Cobertura combinada de linhas e branches

100%

Mínimo de 90%

Lint com Ruff

0 erros

0 erros

Formatação com Ruff

Aprovada

Sem divergência

mypy

Aprovado

Sem erros de tipos

Compatibilidade Python

3.11, 3.12, 3.13 e 3.14

Todas as versões suportadas

Reproduza localmente toda a esteira:

python -m compileall .
python -m ruff check .
python -m ruff format --check .
python -m mypy exemplos desafios
python -m pytest --cov=exemplos --cov=desafios --cov-branch --cov-report=term-missing

O GitHub Actions executa:

um job completo de qualidade no Python 3.14;

a suíte de testes no Python 3.11, 3.12, 3.13 e 3.14;

relatório de cobertura e envio de artefato;

compilação, lint, formatação, tipagem e testes.

Consulte docs/quality.md para a política completa e sua interpretação.

Cobertura de testes

A cobertura é medida com pytest-cov para linhas e ramificações.

O projeto:

informa linhas ausentes e branches parciais no terminal;

reprova cobertura abaixo do mínimo configurado;

gera relatórios XML e HTML localmente;

envia coverage.xml como artefato do CI;

exclui artefatos gerados do controle de versão.

O repositório não utiliza badge estático de cobertura como prova. A fonte de verdade é a esteira executável de CI.

Por que este repositório é diferente

Dimensão

Repositório introdutório convencional

Laboratório de Lógica com Python

Fundamentação

Frequentemente não documentada

Fontes publicadas com DOI

Exemplos

Trechos isolados

Módulos executáveis

Testes

Limitados ou ausentes

Casos normais, limites, erros e CLI

Cobertura

Raramente medida

Linhas e ramificações

Type hints

Opcionais

Verificados nos módulos centrais

Análise estática

Geralmente ausente

Ruff e mypy

CI

Validação manual

GitHub Actions em quatro versões

Arquitetura

Lógica misturada à entrada e saída

Regras de negócio importáveis

Documentação

Apenas README

README, docs e Wiki oficial

Idiomas

Normalmente um

Inglês e português brasileiro

Mapa do repositório

.
├── .github/              # Workflow de CI e templates de contribuição
├── desafios/             # Exercícios progressivos de fundamentos
├── exemplos/             # Aplicações de terminal testáveis
├── tests/                # Testes unitários, limites, erros e CLI
├── wiki/                 # Fontes versionadas da Wiki oficial
├── docs/                 # Estudos, qualidade, ciência, i18n e evidências
├── README.md             # Versão internacional em inglês
├── README.pt-BR.md       # Versão em português brasileiro
├── pyproject.toml        # Configuração do projeto e das ferramentas
├── requirements-dev.txt  # Dependências de desenvolvimento
└── LICENSE               # Licença MIT

Fundamentação científica

O projeto utiliza literatura publicada e revisada por pares para orientar seu desenho didático. A bibliografia ativa não utiliza preprints.

Os principais temas são:

dificuldades de iniciantes em programação;

concepções equivocadas e padrões de erro;

carga cognitiva em educação em computação;

pensamento computacional;

exemplos progressivos e rastreamento explícito;

reutilização, testabilidade e separação de responsabilidades.

Referências selecionadas:

Tema

Fonte publicada

Aprendizagem de programação

Robins, Rountree e Rountree (2003), DOI

Dificuldades de iniciantes

Lahtinen, Ala-Mutka e Järvinen (2005), DOI

Carga cognitiva

Sweller (1988), DOI

Educação em computação

Duran, Zavgorodniaia e Sorva (2022), DOI

Concepções equivocadas em programação

Herman et al. (2010), DOI

Livros complementares:

Eric Matthes, Python Crash Course, 3. ed., No Starch Press, 2023;

Luciano Ramalho, Fluent Python, 2. ed., O'Reilly Media, 2022.

O comportamento da linguagem é fundamentado na documentação oficial do Python 3.14.

Consulte a bibliografia completa em docs/scientific-foundation.md.

Wiki oficial

A Wiki oficial reúne cinco páginas conectadas com:

pré-requisitos;

objetivos de aprendizagem;

exemplos comentados;

explicações passo a passo;

erros comuns;

boas práticas;

exercícios guiados e independentes;

links para o repositório;

referências persistentes com DOI.

Documentação

Recurso

Finalidade

Idioma

Wiki oficial

Páginas estruturadas e referências

PT-BR

Plano de estudos

Progressão guiada de cinco semanas

PT-BR

Guia de qualidade

Ferramentas, cobertura, CI e interpretação

EN

Fundamentação científica

Bibliografia publicada e links DOI

EN

Internacionalização

Política de sincronização EN ↔ PT-BR

EN

Recursos do GitHub

Evidências e recursos utilizados

PT-BR

Internacionalização

O inglês é o idioma de apresentação internacional. O português brasileiro é a versão integral voltada ao estudante.

Os exercícios e a Wiki oficial permanecem em português brasileiro para preservar a consistência curricular. Alterações documentais devem manter os dois READMEs sincronizados conforme docs/internationalization.md.

Como contribuir

Antes de abrir um Pull Request:

leia CONTRIBUTING.md;

leia o guia didático de contribuição;

siga o Código de Conduta;

mantenha a alteração focada;

adicione ou atualize testes;

execute toda a esteira de qualidade localmente.

Princípios de contribuição:

preservar compatibilidade com as versões suportadas do Python;

ampliar exercícios apenas quando houver objetivo de aprendizagem claro;

manter exemplos pequenos, legíveis e testáveis;

documentar comportamentos e casos de fronteira;

manter as versões em inglês e português sincronizadas.

Roadmap

manter compatibilidade com versões suportadas do Python;

ampliar exercícios com objetivos claros e testes úteis;

melhorar acessibilidade e navegação com base no retorno dos estudantes;

adicionar demonstrações leves apenas quando melhorarem a compreensão;

avaliar futuras versões linguísticas com revisão responsável e sincronização.

Licença

Distribuído sob a Licença MIT.

Autor

Criado e mantido por Matheus Florindo de Deus.

estudante de Análise e Desenvolvimento de Sistemas no IFES;

educador e pesquisador multidisciplinar;

colaborador de pesquisa em Fisiologia Translacional na UFES;

ORCID: 0009-0006-3848-0662;

perfil no GitHub.

<div align="center">

Construído com disciplina, reprodutibilidade e prática open source.

Não negocie com sua mente.

</div>
