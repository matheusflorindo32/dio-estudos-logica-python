"""Calculadora com operações independentes e fáceis de testar."""


def somar(primeiro: float, segundo: float) -> float:
    """Retorna a soma de dois números."""
    return primeiro + segundo


def subtrair(primeiro: float, segundo: float) -> float:
    """Retorna a diferença entre dois números."""
    return primeiro - segundo


def multiplicar(primeiro: float, segundo: float) -> float:
    """Retorna o produto de dois números."""
    return primeiro * segundo


def dividir(dividendo: float, divisor: float) -> float:
    """Retorna a divisão e rejeita divisor igual a zero."""
    if divisor == 0:
        raise ZeroDivisionError("Não é possível dividir por zero.")
    return dividendo / divisor


OPERACOES = {
    "+": somar,
    "-": subtrair,
    "*": multiplicar,
    "/": dividir,
}


def calcular(primeiro: float, operador: str, segundo: float) -> float:
    """Executa uma operação cadastrada na calculadora."""
    try:
        operacao = OPERACOES[operador]
    except KeyError as erro:
        raise ValueError(f"Operador inválido: {operador}") from erro
    return operacao(primeiro, segundo)


def main() -> None:
    """Disponibiliza uma interface mínima de terminal."""
    try:
        primeiro = float(input("Primeiro número: ").replace(",", "."))
        operador = input("Operação (+, -, *, /): ").strip()
        segundo = float(input("Segundo número: ").replace(",", "."))
        print(f"Resultado: {calcular(primeiro, operador, segundo):g}")
    except (ValueError, ZeroDivisionError) as erro:
        print(f"Erro: {erro}")


if __name__ == "__main__":
    main()
