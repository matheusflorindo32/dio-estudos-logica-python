"""Calcula a média e classifica a situação acadêmica."""

import math
from collections.abc import Sequence


def validar_nota(nota: float) -> None:
    """Valida se uma nota é finita e está entre 0 e 10."""
    if not math.isfinite(nota) or not 0 <= nota <= 10:
        raise ValueError("Cada nota deve ser um número entre 0 e 10.")


def calcular_media(notas: Sequence[float]) -> float:
    """Calcula a média aritmética de uma sequência não vazia de notas."""
    if not notas:
        raise ValueError("Informe ao menos uma nota.")
    for nota in notas:
        validar_nota(nota)
    return sum(notas) / len(notas)


def classificar_aprovacao(media: float) -> str:
    """Classifica uma média como aprovado, recuperação ou reprovado."""
    validar_nota(media)
    if media >= 7:
        return "Aprovado"
    if media >= 5:
        return "Recuperação"
    return "Reprovado"


def main() -> None:
    """Solicita notas separadas por espaço e mostra o resultado."""
    try:
        entrada = input("Digite as notas separadas por espaço: ")
        notas = [float(valor.replace(",", ".")) for valor in entrada.split()]
        media = calcular_media(notas)
        print(f"Média: {media:.2f}")
        print(f"Situação: {classificar_aprovacao(media)}")
    except ValueError as erro:
        print(f"Erro: {erro}")


if __name__ == "__main__":
    main()
