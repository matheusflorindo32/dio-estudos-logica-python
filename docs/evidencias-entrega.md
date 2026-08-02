# Evidências da entrega

> Este documento registra somente resultados verificados em 2 de agosto de 2026.

| Item | Evidência ou status |
|---|---|
| Repositório | `dio-estudos-logica-python` |
| URL do repositório | <https://github.com/matheusflorindo32/dio-estudos-logica-python> |
| URL da Issue | <https://github.com/matheusflorindo32/dio-estudos-logica-python/issues/1> |
| URL do Pull Request | <https://github.com/matheusflorindo32/dio-estudos-logica-python/pull/2> |
| Status do merge | CONCLUÍDO — merge commit `2dc87bd`, em 2026-08-02 12:01:40 UTC |
| Status da Issue | ENCERRADA automaticamente pelo `Closes #1` do Pull Request |
| Status da Wiki | PENDENTE — configuração habilitada, mas a Wiki ainda não foi inicializada |
| Status do GitHub Actions | APROVADO — Python 3.11 e 3.12 |
| Execução após o merge | <https://github.com/matheusflorindo32/dio-estudos-logica-python/actions/runs/30746960378> |
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
```

## Validações executadas

```text
python -m pip install -r requirements-dev.txt
python -m compileall .
python -m pytest -v
```

Resultado final local: `39 passed in 0.07s`. No GitHub Actions, os jobs de Python 3.11 e 3.12 passaram no push da branch, no Pull Request e no commit de merge.

## Situação da Wiki

A opção de Wiki está habilitada no repositório. Entretanto, a tentativa real de clonar `https://github.com/matheusflorindo32/dio-estudos-logica-python.wiki.git` retornou `Repository not found`, porque nenhuma primeira página foi criada pela interface. As cinco fontes permanecem preservadas em `wiki/`.

## Publicação manual da Wiki

Se a Wiki não puder ser inicializada automaticamente:

1. abra a aba **Wiki** do repositório no GitHub;
2. crie a primeira página com o título `Home` para inicializar o repositório da Wiki;
3. clone `https://github.com/matheusflorindo32/dio-estudos-logica-python.wiki.git`;
4. copie os arquivos Markdown de `wiki/` para a raiz do clone, sem excluir conteúdo existente;
5. revise os links, faça commit e push;
6. abra a Wiki e confirme cada página antes de marcar a entrega como concluída.

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
- [x] pendência manual da Wiki explicitada sem afirmar publicação;
- [x] URL exata do repositório pronta para “Entregar Projeto”.
