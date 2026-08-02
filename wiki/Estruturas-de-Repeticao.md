# Estruturas de Repetição

Repetições evitam duplicar instruções.

## `for`

Use `for` quando houver uma sequência ou intervalo definido:

```python
for numero in range(1, 6):
    print(numero)
```

## `while`

Use `while` quando a repetição depender de uma condição:

```python
contador = 5
while contador >= 0:
    print(contador)
    contador -= 1
```

## Evitando loops infinitos

Confirme que algo dentro do `while` aproxima o estado da condição de parada. Ao processar entrada externa, também defina limites, cancelamento ou quantidade máxima de tentativas quando isso fizer sentido.

## Prática

Execute `desafios/03_repeticoes.py`, altere o número da tabuada e acompanhe o valor da variável do `while` a cada iteração.

[Voltar para Home](Home)

