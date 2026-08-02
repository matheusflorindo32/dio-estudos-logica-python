"""Apresenta repetições com for e while de forma segura."""


def gerar_tabuada(numero: int) -> list[str]:
    """Gera as dez linhas da tabuada de um número."""
    return [f"{numero} x {fator} = {numero * fator}" for fator in range(1, 11)]


def contagem_regressiva(inicio: int) -> list[int]:
    """Cria uma contagem regressiva com limite para evitar laço excessivo."""
    if not 0 <= inicio <= 100:
        raise ValueError("O início deve estar entre 0 e 100.")

    valores: list[int] = []
    atual = inicio
    while atual >= 0:
        valores.append(atual)
        atual -= 1  # Garante que o while sempre avance até o fim.
    return valores


def main() -> None:
    """Exibe uma tabuada e uma contagem regressiva."""
    for linha in gerar_tabuada(5):
        print(linha)

    print("Contagem:", *contagem_regressiva(5))


if __name__ == "__main__":
    main()
