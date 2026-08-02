"""Testes do desafio de listas."""

import pytest

from tests.helpers import carregar_desafio

LISTAS = carregar_desafio("05_listas.py")


def test_organizar_topicos_normaliza_remove_duplicatas_e_ordena() -> None:
    resultado = LISTAS.organizar_topicos(
        ["  Variáveis", "funções", "", "Variáveis", " Listas "]
    )

    assert resultado == ["funções", "Listas", "Variáveis"]


def test_buscar_topico_ignora_maiusculas() -> None:
    topicos = ["Variáveis", "Funções", "Listas"]

    assert LISTAS.buscar_topico(topicos, "FUN") == ["Funções"]


def test_remover_topico_informa_resultado() -> None:
    topicos = ["Variáveis", "Listas"]

    assert LISTAS.remover_topico(topicos, "Listas") is True
    assert LISTAS.remover_topico(topicos, "Inexistente") is False
    assert topicos == ["Variáveis"]


def test_main_exibe_operacoes_com_lista(capsys: pytest.CaptureFixture[str]) -> None:
    LISTAS.main()

    saida = capsys.readouterr().out
    assert "Tópicos:" in saida
    assert "Funções" in saida
    assert "Após remoção:" in saida
