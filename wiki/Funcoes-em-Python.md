# Funções em Python

Funções nomeiam uma operação e favorecem reutilização, testes e manutenção.

```python
def calcular_area(largura: float, altura: float) -> float:
    """Retorna a área de um retângulo válido."""
    if largura <= 0 or altura <= 0:
        raise ValueError("Dimensões inválidas")
    return largura * altura
```

## Componentes

- `def` inicia a definição;
- parâmetros recebem valores;
- type hints comunicam tipos esperados e retornados;
- docstrings explicam o contrato;
- `return` entrega o resultado ao chamador;
- exceções representam entradas ou estados inválidos.

## Funções testáveis

Uma função que retorna um valor é mais simples de testar que uma função que depende diretamente de `input()` e `print()`. Separe regras de negócio da interface do terminal.

## Prática

Leia `desafios/04_funcoes.py` e os arquivos em `exemplos/`. Depois compare as funções aos testes em `tests/`.

[Voltar para Home](Home)
