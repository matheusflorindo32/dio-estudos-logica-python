"""Testes da lógica de negócio do organizador de estudos."""

import builtins

import pytest

from exemplos.organizador_estudos import (
    OrganizadorEstudos,
    exibir_tarefas,
    main,
)


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


def test_localizar_tarefa_percorre_itens_anteriores() -> None:
    organizador = OrganizadorEstudos()
    organizador.adicionar_tarefa("Primeira")
    segunda = organizador.adicionar_tarefa("Segunda")

    concluida = organizador.concluir_tarefa(segunda.identificador)

    assert concluida == segunda
    assert concluida.concluida is True


def test_exibir_tarefas_cobre_estado_vazio_e_concluido(
    capsys: pytest.CaptureFixture[str],
) -> None:
    organizador = OrganizadorEstudos()
    exibir_tarefas(organizador)
    tarefa = organizador.adicionar_tarefa("Estudar testes")
    organizador.concluir_tarefa(tarefa.identificador)
    exibir_tarefas(organizador)

    saida = capsys.readouterr().out
    assert "Nenhuma tarefa cadastrada." in saida
    assert "[x] Estudar testes" in saida


def test_main_percorre_fluxo_completo_do_menu(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    entradas = iter(
        [
            "inválida",
            "2",
            "1",
            "Estudar funções",
            "2",
            "3",
            "1",
            "2",
            "4",
            "1",
            "4",
            "1",
            "0",
        ]
    )
    monkeypatch.setattr(builtins, "input", lambda _mensagem: next(entradas))

    main()

    saida = capsys.readouterr().out
    assert "Opção inválida." in saida
    assert "Nenhuma tarefa cadastrada." in saida
    assert "[ ] Estudar funções" in saida
    assert "[x] Estudar funções" in saida
    assert "Tarefa 1 não encontrada." in saida
