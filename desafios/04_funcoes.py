"""Demonstra funções com parâmetros, retornos, docstrings e type hints."""


def calcular_area_retangulo(largura: float, altura: float) -> float:
    """Retorna a área de um retângulo com dimensões positivas."""
    if largura <= 0 or altura <= 0:
        raise ValueError("Largura e altura devem ser maiores que zero.")
    return largura * altura


def formatar_saudacao(nome: str, periodo: str = "dia") -> str:
    """Monta uma saudação sem imprimir efeitos colaterais."""
    nome_limpo = nome.strip()
    if not nome_limpo:
        raise ValueError("O nome não pode estar vazio.")
    return f"Bom {periodo}, {nome_limpo}!"


def main() -> None:
    """Executa exemplos de chamada das funções."""
    print(formatar_saudacao("Matheus"))
    print(f"Área: {calcular_area_retangulo(4, 3):.2f}")


if __name__ == "__main__":
    main()

