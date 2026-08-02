"""Demonstra operações frequentes com listas em Python."""


def organizar_topicos(topicos: list[str]) -> list[str]:
    """Normaliza, remove duplicatas e ordena uma lista de tópicos."""
    normalizados = [topico.strip() for topico in topicos if topico.strip()]
    return sorted(set(normalizados), key=str.casefold)


def buscar_topico(topicos: list[str], termo: str) -> list[str]:
    """Busca um termo sem diferenciar maiúsculas de minúsculas."""
    termo_normalizado = termo.strip().casefold()
    return [topico for topico in topicos if termo_normalizado in topico.casefold()]


def remover_topico(topicos: list[str], topico: str) -> bool:
    """Remove um tópico e informa se ele existia na lista."""
    try:
        topicos.remove(topico)
        return True
    except ValueError:
        return False


def main() -> None:
    """Executa criação, inclusão, ordenação, busca e remoção."""
    estudos = ["Variáveis", "Funções", "Listas"]
    estudos.append("Condicionais")
    estudos = organizar_topicos(estudos)
    print("Tópicos:", estudos)
    print("Busca por 'fun':", buscar_topico(estudos, "fun"))
    remover_topico(estudos, "Listas")
    print("Após remoção:", estudos)


if __name__ == "__main__":
    main()
