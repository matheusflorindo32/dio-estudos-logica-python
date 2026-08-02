# Como contribuir

Obrigado pelo interesse em melhorar este material educacional. Toda participação deve respeitar o [Código de Conduta](CODE_OF_CONDUCT.md).

## Fluxo de contribuição

1. Faça um fork pelo botão **Fork** no GitHub.
2. Clone o seu fork e entre no diretório:

   ```bash
   git clone https://github.com/SEU_USUARIO_GITHUB/dio-estudos-logica-python.git
   cd dio-estudos-logica-python
   ```

3. Crie uma branch curta e descritiva:

   ```bash
   git switch -c feat/nome-da-melhoria
   ```

4. Implemente uma mudança focada e documente comportamentos novos.
5. Instale as dependências e valide:

   ```bash
   python -m pip install -r requirements-dev.txt
   python -m compileall .
   python -m pytest -v
   ```

6. Faça commits claros. Exemplos de convenção:

   - `feat: adiciona exemplo de dicionários`
   - `fix: corrige validação de nota`
   - `docs: detalha execução no Linux`
   - `test: cobre limite de aprovação`

7. Envie a branch e abra um Pull Request para `main`, preenchendo a template e vinculando a Issue correspondente.

## Padrões esperados

- Preserve o objetivo didático e use português do Brasil na documentação.
- Escreva funções pequenas, com nomes claros, type hints e docstrings.
- Não inclua credenciais, dados pessoais ou dependências desnecessárias.
- Inclua testes para toda alteração de regra de negócio.
- Seja respeitoso ao propor, revisar ou discutir mudanças.

