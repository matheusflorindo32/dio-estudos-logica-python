# Estruturas Condicionais

Estruturas condicionais controlam qual bloco será executado. Python usa `if` para a primeira condição, `elif` para condições alternativas e `else` quando nenhuma anterior é atendida.

```python
def classificar(nota: float) -> str:
    if not 0 <= nota <= 10:
        raise ValueError("Nota inválida")
    if nota >= 7:
        return "Aprovado"
    if nota >= 5:
        return "Recuperação"
    return "Reprovado"
```

## Ordem das condições

As condições são avaliadas de cima para baixo. Organize faixas sobrepostas da mais restritiva para a mais ampla e teste os valores de fronteira.

## Validação

Valide entradas antes de aplicar regras. Isso impede que uma nota negativa ou maior que 10 gere uma classificação aparentemente válida.

## Prática

Execute `desafios/02_condicionais.py` e experimente 0, 4.9, 5, 6.9, 7, 9 e 10. Depois escreva testes para cada limite.

[Voltar para Home](Home)

