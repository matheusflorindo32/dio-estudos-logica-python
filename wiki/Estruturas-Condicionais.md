# Estruturas Condicionais

## Objetivos de aprendizagem

Ao concluir esta página, você deverá ser capaz de:

- explicar como `if`, `elif` e `else` controlam o fluxo de execução;
- organizar condições da mais específica para a mais geral;
- validar entradas antes de aplicar regras;
- identificar erros comuns em condições;
- testar valores de fronteira.

## 1. O que são estruturas condicionais?

Estruturas condicionais permitem que o programa escolha entre caminhos diferentes. Em Python, a instrução `if` avalia expressões em sequência e executa apenas o primeiro bloco cuja condição seja verdadeira. Quando nenhuma condição anterior é satisfeita, o bloco `else`, se existir, é executado (PYTHON SOFTWARE FOUNDATION, 2026a).

```python
idade = 20

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
```

## 2. Sintaxe básica

```python
if condicao_1:
    bloco_1
elif condicao_2:
    bloco_2
else:
    bloco_final
```

Pontos importantes:

- cada condição deve produzir `True` ou `False`;
- os dois-pontos encerram o cabeçalho;
- a indentação define quais instruções pertencem ao bloco;
- somente um dos blocos da cadeia é executado.

## 3. Exemplo didático: classificação de nota

```python
def classificar_nota(nota: float) -> str:
    """Classifica uma nota válida entre 0 e 10."""
    if not 0 <= nota <= 10:
        raise ValueError("A nota deve estar entre 0 e 10.")

    if nota >= 7:
        return "Aprovado"
    elif nota >= 5:
        return "Recuperação"
    else:
        return "Reprovado"
```

### Leitura passo a passo

1. A primeira condição valida a entrada.
2. Se `nota >= 7`, a função retorna `Aprovado`.
3. Caso contrário, verifica se `nota >= 5`.
4. Se nenhuma condição for verdadeira, retorna `Reprovado`.

## 4. Por que a ordem importa?

As condições são avaliadas de cima para baixo. Veja um erro comum:

```python
if nota >= 5:
    resultado = "Recuperação"
elif nota >= 7:
    resultado = "Aprovado"
```

Para uma nota 8, a primeira condição já é verdadeira. O segundo teste nunca será alcançado. A ordem correta é começar pela faixa mais restritiva:

```python
if nota >= 7:
    resultado = "Aprovado"
elif nota >= 5:
    resultado = "Recuperação"
else:
    resultado = "Reprovado"
```

## 5. Validação antes da regra

Uma condição pode produzir uma resposta tecnicamente executável, mas semanticamente incorreta. Sem validação, uma nota `-3` poderia ser classificada simplesmente como “Reprovado”, ocultando o verdadeiro problema: a entrada é inválida.

```python
if not 0 <= nota <= 10:
    raise ValueError("Nota inválida")
```

Separar validação e regra de negócio melhora a clareza, facilita testes e reduz ambiguidades.

## 6. Operadores lógicos

### `and`

Todas as condições devem ser verdadeiras:

```python
if idade >= 18 and possui_habilitacao:
    print("Pode dirigir")
```

### `or`

Pelo menos uma condição deve ser verdadeira:

```python
if dia == "sábado" or dia == "domingo":
    print("Fim de semana")
```

### `not`

Inverte o valor lógico:

```python
if not usuario_ativo:
    print("Acesso bloqueado")
```

## 7. Erros comuns de iniciantes

Pesquisas em educação em computação mostram que condicionais e laços estão entre os conceitos que mais geram interpretações incorretas entre iniciantes. Entre os problemas recorrentes estão aninhamento desnecessário, uso confuso de `else` e dificuldade de acompanhar qual condição foi satisfeita (ROBINS; ROUNTREE; ROUNTREE, 2003). Um preprint de Naude, Denny e Luxton-Reilly (2024), identificado como não revisado por pares, também descreve anti-patterns recorrentes em condicionais produzidas por estudantes.

### Comparação versus atribuição

```python
# Correto: comparação
if resposta == "sim":
    print("Confirmado")
```

### Evite comparação booleana redundante

```python
# Menos claro
if ativo == True:
    print("Ativo")

# Preferível
if ativo:
    print("Ativo")
```

### Evite aninhamento quando um retorno antecipado resolve

```python
def autorizar(idade: int) -> str:
    if idade < 0:
        raise ValueError("Idade inválida")
    if idade < 18:
        return "Não autorizado"
    return "Autorizado"
```

## 8. Valores de fronteira

Testes devem verificar exatamente os pontos em que o resultado muda.

| Nota | Resultado esperado |
|---:|---|
| `0` | Reprovado |
| `4.9` | Reprovado |
| `5` | Recuperação |
| `6.9` | Recuperação |
| `7` | Aprovado |
| `10` | Aprovado |
| `-0.1` | Erro |
| `10.1` | Erro |

## 9. Atividade guiada

Implemente uma função que receba uma temperatura e retorne:

- `Frio`, quando for menor que 18;
- `Agradável`, entre 18 e 27;
- `Quente`, acima de 27.

Depois escreva testes para `17.9`, `18`, `27` e `27.1`.

## 10. Prática no repositório

Execute:

```bash
python desafios/02_condicionais.py
```

Em seguida, consulte os testes relacionados e observe como cada limite é verificado.

## Referências

NAUDE, Etienne; DENNY, Paul; LUXTON-REILLY, Andrew. Anti-patterns in students' conditional statements. [Preprint]. *arXiv*, 2024. DOI: <https://doi.org/10.48550/arXiv.2410.18989>.

PYTHON SOFTWARE FOUNDATION. *The Python language reference: compound statements*. Versão 3.14. [S. l.], 2026a. Disponível em: <https://docs.python.org/3.14/reference/compound_stmts.html>. Acesso em: 2 ago. 2026.

ROBINS, Anthony; ROUNTREE, Janet; ROUNTREE, Nathan. Learning and teaching programming: a review and discussion. *Computer Science Education*, v. 13, n. 2, p. 137-172, 2003. DOI: <https://doi.org/10.1076/csed.13.2.137.14200>.

[Voltar para Home](Home)
