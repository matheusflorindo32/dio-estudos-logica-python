"""Demonstra variáveis, tipos de dados e uma operação aritmética simples."""


def calcular_ano_nascimento(idade: int, ano_atual: int = 2026) -> int:
    """Calcula uma estimativa do ano de nascimento."""
    if idade < 0:
        raise ValueError("A idade não pode ser negativa.")
    return ano_atual - idade


def ler_idade() -> int:
    """Solicita uma idade válida ao usuário."""
    while True:
        entrada = input("Digite sua idade: ").strip()
        try:
            idade = int(entrada)
            if idade < 0:
                raise ValueError
            return idade
        except ValueError:
            print("Informe uma idade usando um número inteiro não negativo.")


def main() -> None:
    """Executa o exemplo no terminal."""
    nome = input("Digite seu nome: ").strip() or "Estudante"
    idade = ler_idade()
    ano_nascimento = calcular_ano_nascimento(idade)

    print(f"Olá, {nome}! Você tem {idade} anos.")
    print(f"Seu ano de nascimento estimado é {ano_nascimento}.")
    print("Tipos usados: nome é str; idade e ano de nascimento são int.")


if __name__ == "__main__":
    main()

