"""Demonstra if, elif e else por meio da classificação de uma nota."""


def classificar_nota(nota: float) -> str:
    """Classifica uma nota de 0 a 10 em faixas de desempenho."""
    if not 0 <= nota <= 10:
        raise ValueError("A nota deve estar entre 0 e 10.")

    # As condições são avaliadas de cima para baixo, da maior faixa para a menor.
    if nota >= 9:
        return "Excelente"
    elif nota >= 7:
        return "Bom"
    elif nota >= 5:
        return "Regular"
    else:
        return "Precisa melhorar"


def gerar_feedback_desempenho(nota: float) -> str:
    """Retorna uma orientação curta a partir da classificação validada."""
    classificacao = classificar_nota(nota)
    orientacoes = {
        "Excelente": "Continue aprofundando e compartilhe o que aprendeu.",
        "Bom": "Ótimo progresso; revise os pontos em que ainda tem dúvidas.",
        "Regular": "Reforce os fundamentos e pratique novos exercícios.",
        "Precisa melhorar": "Retome o conteúdo básico e peça apoio quando necessário.",
    }
    return f"{classificacao}: {orientacoes[classificacao]}"


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
    print(f"Feedback: {gerar_feedback_desempenho(nota)}")


if __name__ == "__main__":
    main()
