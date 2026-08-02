# Recursos do GitHub utilizados

## Repositório e histórico

O Git registra a evolução em commits focados. A branch `main` representa a linha principal e branches de funcionalidade isolam melhorias.

## Issues

As templates em `.github/ISSUE_TEMPLATE/` padronizam relatos de erro e solicitações de funcionalidade. Campos objetivos facilitam reprodução e definição de critérios de aceitação.

## Pull Requests

A template `.github/PULL_REQUEST_TEMPLATE.md` solicita descrição, tipo, testes, checklist e Issue relacionada. O fluxo individual não envolve identidade ou aprovação fictícia.

## GitHub Actions

O workflow `.github/workflows/python-tests.yml` é executado em `push` e `pull_request`. A matriz usa Python 3.11 e 3.12 no Ubuntu, instala apenas a dependência de desenvolvimento e executa pytest.

## Wiki

As fontes versionadas ficam em `wiki/`. A publicação na GitHub Wiki usa um repositório Git separado, o que permite manter as páginas preparadas mesmo quando a Wiki ainda não está habilitada.

## Arquivos comunitários

- `CONTRIBUTING.md`: processo de contribuição;
- `CODE_OF_CONDUCT.md`: ambiente respeitoso e seguro;
- `LICENSE`: permissões da licença MIT;
- `CHANGELOG.md`: histórico das versões.

Consulte [evidencias-entrega.md](evidencias-entrega.md) para distinguir itens preparados localmente de recursos confirmados no GitHub.

