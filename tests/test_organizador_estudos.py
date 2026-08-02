"""Testes da lógica de negócio do organizador de estudos."""

import pytest

from exemplos.organizador_estudos import OrganizadorEstudos


def test_adicionar_e_listar_tarefa() -> None:
    organizador = OrganizadorEstudos()

    tarefa = organizador.adicionar_tarefa("  Estudar funções  ")

    assert tarefa.identificador == 1
    assert tarefa.descricao == "Estudar funções"
    assert organizador.listar_tarefas() == (tarefa,)


def test_adicionar_tarefa_vazia_gera_erro() -> None:
    organizador = OrganizadorEstudos()

    with pytest.raises(ValueError, match="descrição"):
        organizador.adicionar_tarefa("   ")


def test_concluir_tarefa() -> None:
    organizador = OrganizadorEstudos()
    tarefa = organizador.adicionar_tarefa("Revisar listas")

    concluida = organizador.concluir_tarefa(tarefa.identificador)

    assert concluida.concluida is True


def test_remover_tarefa() -> None:
    organizador = OrganizadorEstudos()
    tarefa = organizador.adicionar_tarefa("Praticar condicionais")

    removida = organizador.remover_tarefa(tarefa.identificador)

    assert removida == tarefa
    assert organizador.listar_tarefas() == ()


@pytest.mark.parametrize("acao", ["concluir_tarefa", "remover_tarefa"])
def test_alterar_tarefa_inexistente_gera_erro(acao: str) -> None:
    organizador = OrganizadorEstudos()

    with pytest.raises(ValueError, match="não encontrada"):
        getattr(organizador, acao)(999)


def test_identificadores_nao_sao_reutilizados() -> None:
    organizador = OrganizadorEstudos()
    primeira = organizador.adicionar_tarefa("Primeira")
    organizador.remover_tarefa(primeira.identificador)

    segunda = organizador.adicionar_tarefa("Segunda")

    assert segunda.identificador == 2

