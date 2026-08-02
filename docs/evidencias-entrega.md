# Evidências da entrega

> Registro verificável da evolução internacional associada à Issue #5, em 2 de agosto de 2026. Estados remotos são atualizados somente após confirmação no GitHub.

## Identificação

| Item | Evidência ou status atual |
|---|---|
| Repositório público | <https://github.com/matheusflorindo32/dio-estudos-logica-python> |
| Issue principal | [#5 — Evolução internacional](https://github.com/matheusflorindo32/dio-estudos-logica-python/issues/5) |
| Branch | `feature/international-quality-upgrade` |
| Pull Request | [#6 — feat: eleva projeto a padrão internacional de qualidade](https://github.com/matheusflorindo32/dio-estudos-logica-python/pull/6) — aberto |
| Branch principal | `main` |
| README internacional | [README.md](../README.md) |
| README em português | [README.pt-BR.md](../README.pt-BR.md) |
| URL final da entrega | <https://github.com/matheusflorindo32/dio-estudos-logica-python> |

## Qualidade local

Ambiente local: Python 3.11.15, pytest 9.1.1, pytest-cov 7.1.0, Coverage.py 7.15.2, Ruff 0.16.1 e mypy 2.3.0.

| Controle | Resultado verificado |
|---|---|
| `python -m compileall .` | APROVADO |
| `python -m ruff check .` | APROVADO — nenhum erro |
| `python -m ruff format --check .` | APROVADO — 39 arquivos formatados |
| `python -m mypy exemplos desafios` | APROVADO — 8 arquivos-fonte, nenhum problema |
| `python -m pytest -v` | APROVADO — 76 aprovados, 0 reprovados |
| Cobertura de linhas | 100,00% — 226 instruções, 0 ausentes |
| Cobertura de branches | 100,00% — 70 branches, 0 parciais |
| Meta mínima | 90% em `pyproject.toml` |
| Arquivos com lacunas | Nenhum no escopo `desafios/` e `exemplos/` |

Linha de base anterior à evolução: 39 testes aprovados e 41% de cobertura combinada, com 134 instruções ausentes e 5 branches parciais. Os novos testes cobrem regras, fronteiras, erros, transições de estado e os oito pontos de entrada de terminal; não foram usados marcadores para excluir código testável.

## Integração contínua

O workflow possui um job `Quality` no Python 3.14 e uma matriz independente para Python 3.11, 3.12, 3.13 e 3.14. O Pull Request #6 iniciou os checks; o resultado final e a execução após o merge serão registrados após a conclusão real.

## Fundamentação científica

- duas fontes sem publicação formal foram removidas integralmente do estado atual do repositório e da Wiki oficial;
- oito artigos publicados tiveram autores, título, veículo, ano, volume, número, páginas e DOI conferidos no Crossref;
- os oito endereços DOI retornaram redirecionamento persistente para os respectivos editores;
- as citações usam sistema autor-data e as referências seguem ABNT NBR 6023:2018 na medida aplicável;
- *Python Crash Course*, 3ª edição, e *Fluent Python*, 2ª edição, foram conferidos nas páginas oficiais das editoras;
- a documentação da linguagem está fixada no Python 3.14.

A lista completa e a aplicação pedagógica estão em [scientific-foundation.md](scientific-foundation.md).

## Wiki oficial

| Item | Evidência |
|---|---|
| URL | <https://github.com/matheusflorindo32/dio-estudos-logica-python/wiki> |
| Repositório Git | `dio-estudos-logica-python.wiki.git` |
| Branch | `master` |
| Commit publicado | `cf7fab0998e42321bcd592514fb16032c9c28b15` |
| Mensagem | mensagem de publicação definida na missão |
| Publicação | APROVADA — push sem force |

Páginas verificadas com HTTP 200 e inspeção da renderização no navegador:

- [Home](https://github.com/matheusflorindo32/dio-estudos-logica-python/wiki)
- [Introdução à Lógica de Programação com Python](https://github.com/matheusflorindo32/dio-estudos-logica-python/wiki/Introducao-a-Logica-de-Programacao-com-Python)
- [Estruturas Condicionais](https://github.com/matheusflorindo32/dio-estudos-logica-python/wiki/Estruturas-Condicionais)
- [Estruturas de Repetição](https://github.com/matheusflorindo32/dio-estudos-logica-python/wiki/Estruturas-de-Repeticao)
- [Funções em Python](https://github.com/matheusflorindo32/dio-estudos-logica-python/wiki/Funcoes-em-Python)

A inspeção confirmou títulos e acentuação, conteúdo não vazio, blocos de código, referências, links DOI, navegação e ausência de páginas 404. O link `Voltar para Home` foi acionado no navegador e retornou à página inicial.

## GitHub Project

PENDENTE OPCIONAL — `gh auth refresh -h github.com -s read:project,project` foi tentado, mas aguardou autorização interativa. A execução foi encerrada sem alterar o token. O token permanece sem `read:project`; por isso nenhum Project foi criado e nenhuma vinculação foi alegada.

Com autorização manual, executar:

```powershell
gh auth refresh -h github.com -s read:project,project
```

Depois criar o Project `Evolução dos Estudos de Python`, configurar o campo Status e vincular a Issue #5.

## Histórico preservado

A entrega inicial permanece rastreável nos Pull Requests [#2](https://github.com/matheusflorindo32/dio-estudos-logica-python/pull/2), [#3](https://github.com/matheusflorindo32/dio-estudos-logica-python/pull/3) e [#4](https://github.com/matheusflorindo32/dio-estudos-logica-python/pull/4), todos anteriores a esta evolução. Seus resultados não são apresentados como estado atual de qualidade.

## Estado de conclusão

- [x] referências atuais revisadas e busca proibitiva sem ocorrências;
- [x] cobertura real de linhas e branches registrada;
- [x] Ruff lint e formatação aprovados;
- [x] mypy e compilação aprovados;
- [x] README internacional e versão integral em português criados;
- [x] Wiki oficial sincronizada e cinco páginas verificadas;
- [x] Pull Request #6 aberto e ligado à Issue #5;
- [ ] CI final aprovado em todos os cinco jobs;
- [ ] Pull Request mesclado e commit de merge registrado;
- [ ] Issue #5 encerrada.
