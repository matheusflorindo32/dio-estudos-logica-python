"""Organizador de estudos com lógica de negócio separada do terminal."""

from dataclasses import dataclass


@dataclass(slots=True)
class Tarefa:
    """Representa uma tarefa de estudo."""

    identificador: int
    descricao: str
    concluida: bool = False


class OrganizadorEstudos:
    """Gerencia tarefas em memória durante a execução do programa."""

    def __init__(self) -> None:
        self._tarefas: list[Tarefa] = []
        self._proximo_identificador = 1

    def adicionar_tarefa(self, descricao: str) -> Tarefa:
        """Adiciona e retorna uma tarefa com identificador único."""
        descricao_limpa = descricao.strip()
        if not descricao_limpa:
            raise ValueError("A descrição não pode estar vazia.")

        tarefa = Tarefa(self._proximo_identificador, descricao_limpa)
        self._proximo_identificador += 1
        self._tarefas.append(tarefa)
        return tarefa

    def listar_tarefas(self) -> tuple[Tarefa, ...]:
        """Retorna uma visão imutável da sequência de tarefas."""
        return tuple(self._tarefas)

    def concluir_tarefa(self, identificador: int) -> Tarefa:
        """Marca uma tarefa existente como concluída."""
        tarefa = self._localizar_tarefa(identificador)
        tarefa.concluida = True
        return tarefa

    def remover_tarefa(self, identificador: int) -> Tarefa:
        """Remove e retorna uma tarefa existente."""
        tarefa = self._localizar_tarefa(identificador)
        self._tarefas.remove(tarefa)
        return tarefa

    def _localizar_tarefa(self, identificador: int) -> Tarefa:
        """Localiza uma tarefa ou gera um erro útil."""
        for tarefa in self._tarefas:
            if tarefa.identificador == identificador:
                return tarefa
        raise ValueError(f"Tarefa {identificador} não encontrada.")


def exibir_tarefas(organizador: OrganizadorEstudos) -> None:
    """Exibe as tarefas na interface de terminal."""
    tarefas = organizador.listar_tarefas()
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for tarefa in tarefas:
        estado = "x" if tarefa.concluida else " "
        print(f"{tarefa.identificador}. [{estado}] {tarefa.descricao}")


def main() -> None:
    """Executa um menu interativo sem misturar entrada com regras de negócio."""
    organizador = OrganizadorEstudos()
    opcoes = {"1", "2", "3", "4", "0"}

    while True:
        print("\n1 Adicionar | 2 Listar | 3 Concluir | 4 Remover | 0 Sair")
        opcao = input("Escolha: ").strip()
        if opcao not in opcoes:
            print("Opção inválida.")
            continue
        if opcao == "0":
            break

        try:
            if opcao == "1":
                organizador.adicionar_tarefa(input("Descrição: "))
            elif opcao == "2":
                exibir_tarefas(organizador)
            else:
                identificador = int(input("Identificador: "))
                if opcao == "3":
                    organizador.concluir_tarefa(identificador)
                else:
                    organizador.remover_tarefa(identificador)
        except ValueError as erro:
            print(f"Erro: {erro}")


if __name__ == "__main__":
    main()
