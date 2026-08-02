# Estruturas de Repetição

## Objetivos de aprendizagem

Ao concluir esta página, você deverá ser capaz de:

- diferenciar os usos de `for` e `while`;
- explicar o papel de condição, estado e atualização em um laço;
- usar `range()`, `break` e `continue` conscientemente;
- prevenir laços infinitos;
- acompanhar a execução de um laço por meio de uma tabela de rastreamento.

## 1. O que são estruturas de repetição?

Estruturas de repetição, também chamadas de **laços** ou **loops**, permitem executar um bloco de instruções várias vezes. Elas reduzem duplicação de código e ajudam a representar processos iterativos.

Na referência oficial do Python, `while` repete um bloco enquanto uma expressão for verdadeira, enquanto `for` percorre os elementos produzidos por um objeto iterável (PYTHON SOFTWARE FOUNDATION, 2026a).

## 2. Quando usar `for`?

Use `for` quando o programa precisa percorrer uma coleção, uma sequência ou um intervalo conhecido.

```python
for numero in range(1, 6):
    print(numero)
```

Saída:

```text
1
2
3
4
5
```

O valor final de `range()` não é incluído. Assim, `range(1, 6)` produz `1, 2, 3, 4, 5`.

### Percorrendo uma lista

```python
nomes = ["Ana", "Bruno", "Carla"]

for nome in nomes:
    print(f"Olá, {nome}!")
```

## 3. Quando usar `while`?

Use `while` quando a repetição depende de uma condição cujo número de iterações pode não ser conhecido antecipadamente.

```python
contador = 5

while contador >= 0:
    print(contador)
    contador -= 1
```

Nesse exemplo existem três elementos essenciais:

1. **estado inicial:** `contador = 5`;
2. **condição:** `contador >= 0`;
3. **atualização:** `contador -= 1`.

Sem a atualização, a condição permaneceria verdadeira e o laço poderia não terminar.

## 4. Rastreamento passo a passo

Para compreender um laço, registre como as variáveis mudam a cada iteração.

```python
soma = 0

for numero in range(1, 4):
    soma += numero
```

| Iteração | `numero` | `soma` antes | `soma` depois |
|---:|---:|---:|---:|
| 1 | 1 | 0 | 1 |
| 2 | 2 | 1 | 3 |
| 3 | 3 | 3 | 6 |

Acompanhar o estado das variáveis é uma estratégia útil para iniciantes, pois reduz a necessidade de manter mentalmente várias mudanças simultâneas. Isso é coerente com princípios de redução de carga cognitiva durante a resolução de problemas (SWELLER, 1988).

## 5. `break` e `continue`

### `break`

Interrompe o laço imediatamente:

```python
for numero in range(1, 11):
    if numero == 5:
        break
    print(numero)
```

### `continue`

Ignora o restante da iteração atual e avança para a próxima:

```python
for numero in range(1, 6):
    if numero == 3:
        continue
    print(numero)
```

Use essas instruções com clareza. Muitos desvios dentro de um laço podem dificultar a leitura do fluxo.

## 6. Evitando laços infinitos

Um laço infinito ocorre quando a condição do `while` nunca se torna falsa.

```python
# Problema: contador nunca muda
contador = 1
while contador <= 5:
    print(contador)
```

Correção:

```python
contador = 1
while contador <= 5:
    print(contador)
    contador += 1
```

Ao processar entradas externas, também considere:

- número máximo de tentativas;
- opção de cancelamento;
- tratamento de entrada inválida;
- condição explícita de encerramento.

## 7. Exemplo aplicado: tentativas limitadas

```python
def verificar_senha(senha_correta: str, tentativas: list[str]) -> bool:
    """Retorna True se a senha correta aparecer em até três tentativas."""
    for tentativa in tentativas[:3]:
        if tentativa == senha_correta:
            return True
    return False
```

A função é testável porque recebe os dados diretamente e devolve um valor, sem depender de `input()`.

## 8. Erros comuns de iniciantes

A literatura em educação em programação relata dificuldades frequentes para compreender o fluxo de execução, os limites do intervalo, a atualização de variáveis e a condição de parada (ROBINS; ROUNTREE; ROUNTREE, 2003). Um preprint recente organiza erros de interpretação relacionados a seleção e iteração, mostrando que estudantes podem confundir a quantidade de execuções ou o momento em que a condição é avaliada (ECKERT; KAUTZ, 2026); esse trabalho ainda não deve ser apresentado como artigo revisado por pares.

Erros comuns incluem:

- esquecer de atualizar a variável do `while`;
- usar limites incorretos em `range()`;
- alterar a coleção durante a iteração;
- criar aninhamentos desnecessários;
- usar `while True` sem saída segura;
- confundir `break` com `continue`.

## 9. Atividade guiada

Crie uma função que receba uma lista de notas e calcule a média apenas das notas válidas entre 0 e 10.

Requisitos:

- use `for` para percorrer a lista;
- ignore valores inválidos com `continue`;
- retorne `None` quando não houver nenhuma nota válida;
- escreva pelo menos três testes.

## 10. Prática no repositório

Execute:

```bash
python desafios/03_repeticoes.py
```

Depois:

1. altere o número da tabuada;
2. acompanhe o valor das variáveis a cada iteração;
3. teste os limites do `range()`;
4. modifique o exemplo para impedir mais de três tentativas.

## Referências

ECKERT, Dimitri; KAUTZ, Christian. How students (mis)understand conditionals and loops: a taxonomy. [Preprint]. *arXiv*, 2026. DOI: <https://doi.org/10.48550/arXiv.2605.26966>.

PYTHON SOFTWARE FOUNDATION. *The Python language reference: compound statements*. Versão 3.14. [S. l.], 2026a. Disponível em: <https://docs.python.org/3.14/reference/compound_stmts.html>. Acesso em: 2 ago. 2026.

ROBINS, Anthony; ROUNTREE, Janet; ROUNTREE, Nathan. Learning and teaching programming: a review and discussion. *Computer Science Education*, v. 13, n. 2, p. 137-172, 2003. DOI: <https://doi.org/10.1076/csed.13.2.137.14200>.

SWELLER, John. Cognitive load during problem solving: effects on learning. *Cognitive Science*, v. 12, n. 2, p. 257-285, 1988. DOI: <https://doi.org/10.1207/s15516709cog1202_4>.

[Voltar para Home](Home)
