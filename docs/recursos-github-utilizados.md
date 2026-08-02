# Recursos do GitHub utilizados

## Repositório e histórico

O Git registra a evolução em commits focados. A branch `main` representa a linha principal e branches de funcionalidade isolam melhorias.

## Issues

As templates em `.github/ISSUE_TEMPLATE/` padronizam relatos de erro e solicitações de funcionalidade. Campos objetivos facilitam reprodução e definição de critérios de aceitação.

## Pull Requests

A template `.github/PULL_REQUEST_TEMPLATE.md` solicita descrição, tipo, testes, checklist e Issue relacionada. O fluxo individual não envolve identidade ou aprovação fictícia.

## GitHub Actions

O workflow `.github/workflows/python-tests.yml` é executado em `push` e `pull_request` com permissões somente de leitura. O job `Quality`, no Python 3.14, executa compilação, Ruff lint e formatação, mypy, pytest e cobertura de linhas e branches, publica um resumo e envia `coverage.xml` como artefato temporário. A matriz independente executa compilação e testes no Python 3.11, 3.12, 3.13 e 3.14.

## Wiki

As fontes versionadas ficam em `wiki/`. A publicação na [GitHub Wiki oficial](https://github.com/matheusflorindo32/dio-estudos-logica-python/wiki) usa um repositório Git separado. As cinco páginas são sincronizadas preservando nomes e páginas existentes, e a validação inclui conteúdo renderizado, navegação, código, referências e ausência de respostas 404.

## Arquivos comunitários

- `CONTRIBUTING.md`: processo de contribuição;
- `CODE_OF_CONDUCT.md`: ambiente respeitoso e seguro;
- `LICENSE`: permissões da licença MIT;
- `CHANGELOG.md`: histórico das versões.
- `README.md` e `README.pt-BR.md`: apresentação internacional e versão integral em português.
- `docs/quality.md`: controles locais e remotos.
- `docs/scientific-foundation.md`: política e referências publicadas.
- `docs/internationalization.md`: contrato de equivalência entre idiomas.

Consulte [evidencias-entrega.md](evidencias-entrega.md) para distinguir itens preparados localmente de recursos confirmados no GitHub.
