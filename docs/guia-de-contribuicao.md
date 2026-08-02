# Guia didático de contribuição

Este guia complementa o arquivo [CONTRIBUTING.md](../CONTRIBUTING.md) com a lógica por trás do fluxo.

## Por que começar por uma Issue?

A Issue registra problema, contexto e critérios de aceitação antes do código. Ela reduz ambiguidades e mantém decisões rastreáveis.

## Por que usar uma branch?

Uma branch isola o trabalho em andamento da versão estável. Use um nome que revele a intenção, como `feat/novo-exemplo` ou `fix/validacao-nota`.

## Por que abrir um Pull Request?

O Pull Request reúne diferenças, discussão e resultado da automação. Mesmo em um projeto individual, ele cria uma trilha verificável e permite revisar a própria mudança antes do merge, sem simular outro revisor.

## Sequência prática

```bash
git switch main
git pull --ff-only
git switch -c feat/nova-atividade
# altere arquivos e execute os controles de qualidade
python -m compileall .
python -m ruff check .
python -m ruff format --check .
python -m mypy exemplos desafios
python -m pytest --cov=exemplos --cov=desafios --cov-branch --cov-report=term-missing
git add caminho/do/arquivo tests/test_correspondente.py
git commit -m "feat: adiciona nova atividade"
git push -u origin feat/nova-atividade
```

Depois, abra o Pull Request no GitHub, relacione a Issue com `Closes #NUMERO` e aguarde os checks. Faça o merge apenas quando a automação estiver aprovada.

## Revisão antes do envio

- a solução realmente atende aos critérios da Issue;
- nomes, docstrings e mensagens estão claros;
- entradas inválidas são tratadas;
- testes cobrem sucesso, fronteiras, erro e branches relevantes;
- cobertura combinada permanece acima do mínimo de 90%;
- Ruff, mypy, compilação e pytest passam;
- README inglês e português permanecem equivalentes quando aplicável;
- referências acadêmicas possuem publicação formal, metadados e DOI verificável;
- nenhuma credencial ou informação privada foi incluída.

Consulte [quality.md](quality.md) para a finalidade de cada controle e [scientific-foundation.md](scientific-foundation.md) para a política de fontes.
