# Funções em Python

## Objetivos de aprendizagem

Ao concluir esta página, você deverá ser capaz de:

- explicar por que funções favorecem reutilização e manutenção;
- definir funções com parâmetros e retorno;
- usar type hints e docstrings;
- separar regras de negócio da interface de entrada e saída;
- escrever funções pequenas, previsíveis e testáveis.

## Pré-requisitos

- variáveis, condições, repetições e tipos básicos;
- execução de módulos Python pelo terminal;
- noções de entrada, processamento, validação e saída.

## 1. O que é uma função?

Uma **função** é um bloco nomeado de instruções criado para executar uma responsabilidade específica. Em Python, funções são definidas com `def`, podem receber parâmetros e podem devolver resultados com `return` (PYTHON SOFTWARE FOUNDATION, 2026b).

```python
def saudacao(nome: str) -> str:
    return f"Olá, {nome}!"
```

Uso:

```python
mensagem = saudacao("Ana")
print(mensagem)
```

## 2. Componentes de uma função

```python
def calcular_area(largura: float, altura: float) -> float:
    """Calcula a área de um retângulo com dimensões positivas."""
    if largura <= 0 or altura <= 0:
        raise ValueError("As dimensões devem ser positivas.")
    return largura * altura
```

| Elemento | Função |
|---|---|
| `def` | inicia a definição |
| `calcular_area` | nome da função |
| `largura`, `altura` | parâmetros de entrada |
| `float` | anotação de tipo |
| docstring | explica o contrato da função |
| `raise` | sinaliza entrada inválida |
| `return` | devolve o resultado |

### Leitura passo a passo

1. a assinatura declara nome, parâmetros e tipo de retorno;
2. a docstring registra o contrato esperado;
3. a condição protege o domínio válido;
4. `raise` encerra a chamada com um erro útil quando necessário;
5. `return` entrega um valor reutilizável no caminho de sucesso.

## 3. Parâmetros e argumentos

**Parâmetros** aparecem na definição da função. **Argumentos** são os valores fornecidos na chamada.

```python
def somar(a: float, b: float) -> float:
    return a + b


resultado = somar(2, 3)
```

Nesse exemplo, `a` e `b` são parâmetros; `2` e `3` são argumentos.

## 4. `return` não é `print`

`print()` exibe algo na tela. `return` devolve um valor para quem chamou a função.

```python
# Menos reutilizável
def mostrar_dobro(numero: float) -> None:
    print(numero * 2)


# Mais reutilizável e testável
def calcular_dobro(numero: float) -> float:
    return numero * 2
```

Com `return`, o resultado pode ser testado, armazenado, combinado com outros cálculos ou apresentado por qualquer interface.

## 5. Type hints

Type hints documentam os tipos esperados, mas não impedem automaticamente que valores de outros tipos sejam passados durante a execução.

```python
def calcular_media(notas: list[float]) -> float:
    return sum(notas) / len(notas)
```

Eles melhoram a legibilidade e ajudam ferramentas de análise estática, editores e revisores humanos.

## 6. Docstrings

Uma docstring descreve o propósito e o contrato da função.

```python
def dividir(dividendo: float, divisor: float) -> float:
    """Divide dois números e rejeita divisor igual a zero.

    Args:
        dividendo: Número que será dividido.
        divisor: Número pelo qual será feita a divisão.

    Returns:
        Resultado da divisão.

    Raises:
        ZeroDivisionError: Se o divisor for zero.
    """
    if divisor == 0:
        raise ZeroDivisionError("Não é possível dividir por zero.")
    return dividendo / divisor
```

## 7. Funções pequenas e responsabilidade única

Uma função deve, preferencialmente, representar uma responsabilidade clara. Dividir um problema em funções menores reduz a complexidade de cada etapa e facilita compreensão, teste e manutenção.

```python
def validar_nota(nota: float) -> None:
    if not 0 <= nota <= 10:
        raise ValueError("Nota inválida")


def calcular_media(nota_1: float, nota_2: float) -> float:
    validar_nota(nota_1)
    validar_nota(nota_2)
    return (nota_1 + nota_2) / 2


def classificar_media(media: float) -> str:
    return "Aprovado" if media >= 7 else "Reprovado"
```

## 8. Separando lógica e interface

Misturar `input()`, cálculo e `print()` na mesma função dificulta testes automatizados. Prefira separar a lógica de negócio da interface.

```python
def converter_celsius_para_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32


def main() -> None:
    celsius = float(input("Temperatura em Celsius: "))
    fahrenheit = converter_celsius_para_fahrenheit(celsius)
    print(f"Temperatura em Fahrenheit: {fahrenheit:.1f}")


if __name__ == "__main__":
    main()
```

A função de conversão pode ser testada sem simular teclado ou capturar saída do terminal.

## 9. Funções puras e efeitos colaterais

Uma função é considerada **pura** quando, para as mesmas entradas, produz sempre a mesma saída e não altera estado externo.

```python
def aplicar_desconto(preco: float, percentual: float) -> float:
    return preco * (1 - percentual / 100)
```

Funções puras tendem a ser mais previsíveis e simples de testar. Nem toda função precisa ser pura, mas separar cálculos de efeitos colaterais costuma melhorar o projeto.

## 10. Testes de funções

```python
def test_calcular_area() -> None:
    assert calcular_area(3, 4) == 12
```

Também é importante testar entradas inválidas:

```python
import pytest


def test_calcular_area_rejeita_dimensao_invalida() -> None:
    with pytest.raises(ValueError):
        calcular_area(0, 4)
```

A revisão de Robins, Rountree e Rountree (2003) mostra que iniciantes precisam integrar conhecimento sintático, modelos mentais e estratégias de resolução. Funções pequenas e exemplos testáveis ajudam a tornar essas relações explícitas.

## 11. Erros comuns

- esquecer de usar `return`;
- misturar entrada, regra e saída na mesma função;
- criar funções longas com várias responsabilidades;
- usar nomes vagos como `funcao1` ou `processar_coisa`;
- não validar parâmetros;
- depender de variáveis globais sem necessidade;
- escrever docstrings que apenas repetem o nome da função.

## 12. Atividade guiada

Implemente uma função chamada `calcular_imc` que:

- receba peso em quilogramas e altura em metros;
- rejeite valores menores ou iguais a zero;
- retorne o IMC calculado;
- possua type hints e docstring;
- seja acompanhada por testes para casos válidos e inválidos.

## 13. Boas práticas

- escolha um nome que descreva a ação ou o resultado;
- mantenha uma responsabilidade principal por função;
- documente parâmetros, retorno e erros que fazem parte do contrato;
- evite estado global quando os dados podem ser parâmetros;
- faça a lógica retornar valores e deixe a interface apresentá-los.

## 14. Exercício independente

Crie funções separadas para validar um preço, calcular um desconto percentual e formatar o valor final. Escreva type hints, docstrings e testes para desconto zero, desconto máximo permitido e entradas inválidas.

## 15. Prática no repositório

Leia:

```text
desafios/04_funcoes.py
exemplos/calculadora.py
exemplos/organizador_estudos.py
exemplos/verificador_aprovacao.py
```

Depois compare as funções com os testes existentes em `tests/`.

## Referências

PYTHON SOFTWARE FOUNDATION. *The Python tutorial: defining functions*. Versão 3.14. [S. l.], 2026b. Disponível em: <https://docs.python.org/3.14/tutorial/controlflow.html#defining-functions>. Acesso em: 2 ago. 2026.

ROBINS, Anthony; ROUNTREE, Janet; ROUNTREE, Nathan. Learning and teaching programming: a review and discussion. *Computer Science Education*, v. 13, n. 2, p. 137-172, 2003. DOI: <https://doi.org/10.1076/csed.13.2.137.14200>.

SWELLER, John. Cognitive load during problem solving: effects on learning. *Cognitive Science*, v. 12, n. 2, p. 257-285, 1988. DOI: <https://doi.org/10.1207/s15516709cog1202_4>.

[Voltar para Home](Home)
