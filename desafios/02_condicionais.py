"""Demonstra if, elif e else por meio da classificação de uma nota."""


def classificar_nota(nota: float) -> str:
    """Classifica uma nota de 0 a 10 em faixas de desempenho."""
    if not 0 <= nota <= 10:
        raise ValueError("A nota deve estar entre 0 e 10.")

    if nota >= 9:
        return "Excelente"
    if nota >= 7:
        return "Bom"
    if nota >= 5:
        return "Regular"
    return "Precisa melhorar"


def ler_nota() -> float:
    """Solicita uma nota até que o usuário informe um valor válido."""
    while True:
        entrada = input("Digite uma nota de 0 a 10: ").strip().replace(",", ".")
        try:
            nota = float(entrada)
            classificar_nota(nota)
            return nota
        except ValueError:
            print("Entrada inválida. Informe um número entre 0 e 10.")


def main() -> None:
    """Executa o exemplo no terminal."""
    nota = ler_nota()
    print(f"Classificação: {classificar_nota(nota)}")


if __name__ == "__main__":
    main()

