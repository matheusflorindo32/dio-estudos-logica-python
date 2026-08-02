"""Testes do desafio de estruturas de repetição."""

import pytest

from tests.helpers import carregar_desafio

REPETICOES = carregar_desafio("03_repeticoes.py")


def test_gerar_tabuada() -> None:
    tabuada = REPETICOES.gerar_tabuada(3)

    assert len(tabuada) == 10
    assert tabuada[0] == "3 x 1 = 3"
    assert tabuada[-1] == "3 x 10 = 30"


def test_contagem_regressiva_inclui_zero() -> None:
    assert REPETICOES.contagem_regressiva(3) == [3, 2, 1, 0]


@pytest.mark.parametrize("inicio", [-1, 101])
def test_contagem_regressiva_rejeita_limite_invalido(inicio: int) -> None:
    with pytest.raises(ValueError, match="entre 0 e 100"):
        REPETICOES.contagem_regressiva(inicio)


def test_main_exibe_tabuada_e_contagem(
    capsys: pytest.CaptureFixture[str],
) -> None:
    REPETICOES.main()

    saida = capsys.readouterr().out
    assert "5 x 10 = 50" in saida
    assert "Contagem: 5 4 3 2 1 0" in saida
