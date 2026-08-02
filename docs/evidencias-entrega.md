# Evidências da entrega

> Este documento registra somente resultados verificados em 2 de agosto de 2026.

| Item | Evidência ou status |
|---|---|
| Repositório | `dio-estudos-logica-python` |
| URL do repositório | <https://github.com/matheusflorindo32/dio-estudos-logica-python> |
| URL da Issue | <https://github.com/matheusflorindo32/dio-estudos-logica-python/issues/1> |
| Pull Request da funcionalidade | <https://github.com/matheusflorindo32/dio-estudos-logica-python/pull/2> |
| Pull Request da documentação científica | <https://github.com/matheusflorindo32/dio-estudos-logica-python/pull/3> — mesclado |
| Pull Request da publicação oficial | <https://github.com/matheusflorindo32/dio-estudos-logica-python/pull/4> |
| Status do merge da funcionalidade | CONCLUÍDO — merge commit `2dc87bd`, em 2026-08-02 12:01:40 UTC |
| Status da Issue | ENCERRADA automaticamente pelo `Closes #1` do Pull Request |
| Status da Wiki | PUBLICADA E VERIFICADA — cinco páginas oficiais acessíveis |
| Branch da Wiki | `master` |
| Commit da Wiki | `efef0c26b4104805945e9b68c0be5950441a91ba` |
| Data da publicação da Wiki | 2 ago. 2026, 10:23:51 (UTC-03:00) |
| Status do GitHub Actions | APROVADO — Python 3.11 e 3.12 |
| Execução após o merge | <https://github.com/matheusflorindo32/dio-estudos-logica-python/actions/runs/30746960378> |
| Execução após atualizar as Actions | <https://github.com/matheusflorindo32/dio-estudos-logica-python/actions/runs/30747091128> |
| Branch utilizada | `feature/estruturas-condicionais` — removida do remoto após o merge |
| Testes locais | 39 aprovados, 0 reprovados, com Python 3.11.15 e pytest 8.4.1 |
| Compilação local | APROVADA — `python -m compileall .` sem erro |

## Commits realizados

```text
aec1dfe chore: inicia estrutura do projeto
248cff7 feat: adiciona desafios de lógica com Python
999a272 feat: adiciona exemplos funcionais
422840b test: adiciona testes automatizados
3242086 docs: adiciona documentação open source
1095d65 ci: adiciona workflow de testes
8f4e257 feat: aprimora exemplo de estruturas condicionais
2dc87bd Merge pull request #2 from matheusflorindo32/feature/estruturas-condicionais
1e883b4 docs: registra evidências da entrega
b3fdf46 ci: atualiza actions para Node.js 24
```

O commit que atualiza este próprio registro pode ser consultado com `git log --oneline --reverse`; ele não é autorreferenciado com um hash dentro do mesmo conteúdo.

## Validações executadas

```text
python -m pip install -r requirements-dev.txt
python -m compileall .
python -m pytest -v
```

Resultado local desta revisão: `39 passed in 0.08s`. No GitHub Actions, os jobs de Python 3.11 e 3.12 passaram no push da branch, no Pull Request, no commit de merge e após a atualização para `actions/checkout@v7` e `actions/setup-python@v7`.

## Situação da Wiki

A Wiki oficial foi publicada na branch `master` do repositório `dio-estudos-logica-python.wiki.git`, no commit `efef0c2`. A página Home criada anteriormente foi inspecionada antes da atualização; nenhuma página existente foi apagada e não houve force push.

### Páginas oficiais verificadas

- [Home](https://github.com/matheusflorindo32/dio-estudos-logica-python/wiki)
- [Introdução à Lógica de Programação com Python](https://github.com/matheusflorindo32/dio-estudos-logica-python/wiki/Introducao-a-Logica-de-Programacao-com-Python)
- [Estruturas Condicionais](https://github.com/matheusflorindo32/dio-estudos-logica-python/wiki/Estruturas-Condicionais)
- [Estruturas de Repetição](https://github.com/matheusflorindo32/dio-estudos-logica-python/wiki/Estruturas-de-Repeticao)
- [Funções em Python](https://github.com/matheusflorindo32/dio-estudos-logica-python/wiki/Funcoes-em-Python)

A validação remota confirmou títulos, conteúdo não vazio, blocos de código renderizados, seções de referências, links DOI e ausência de 404. Os quatro links `Voltar para Home` apontam para `Home`; um clique real de retorno também foi confirmado no navegador.

### Revisão científica e ABNT

- quatro artigos revisados por pares tiveram autores, títulos, periódicos, volumes, números, páginas, anos e DOIs conferidos no Crossref;
- os trabalhos de Naude, Denny e Luxton-Reilly (2024) e Eckert e Kautz (2026) foram confirmados no arXiv e identificados explicitamente como preprints;
- os DOIs foram convertidos em links persistentes `https://doi.org/`;
- a documentação oficial foi fixada na versão Python 3.14;
- citações autor-data e referências foram revisadas conforme a ABNT NBR 6023:2018, na medida aplicável.

### Histórico preservado

Uma tentativa anterior de clone havia retornado `Repository not found`, pois a primeira Home ainda não existia. Após a inicialização manual, `git ls-remote` e o clone oficial passaram a funcionar. Esse histórico explica a pendência registrada nas versões anteriores deste documento.

## GitHub Project

PENDENTE — requer ação manual. O token atual do GitHub CLI não possui o escopo `read:project`, e nenhuma permissão adicional foi concedida automaticamente.

Após revisar a solicitação de acesso, execute:

```powershell
gh auth refresh -s read:project,project
gh project create --owner matheusflorindo32 --title "Evolução dos Estudos de Python"
gh project list --owner matheusflorindo32
```

Use o número retornado no lugar de `NUMERO` para adicionar os itens:

```powershell
gh project item-create NUMERO --owner matheusflorindo32 --title "Fundamentos"
gh project item-create NUMERO --owner matheusflorindo32 --title "Condicionais"
gh project item-create NUMERO --owner matheusflorindo32 --title "Repetições"
gh project item-create NUMERO --owner matheusflorindo32 --title "Funções"
gh project item-create NUMERO --owner matheusflorindo32 --title "Testes"
gh project item-create NUMERO --owner matheusflorindo32 --title "Documentação"
```

## Checklist final para envio à DIO

- [x] arquivos e exemplos criados localmente;
- [x] documentação open source e Wiki preparadas;
- [x] compilação e testes locais registrados;
- [x] repositório público confirmado;
- [x] Issue e Pull Request reais confirmados;
- [x] workflow remoto aprovado;
- [x] merge realizado e Issue encerrada;
- [x] Wiki oficial publicada e cinco páginas verificadas;
- [x] referências científicas e padrão ABNT revisados;
- [x] URL exata do repositório pronta para “Entregar Projeto”.
