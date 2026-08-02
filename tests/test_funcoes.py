"""Testes do desafio de funções."""

import pytest

from tests.helpers import carregar_desafio

FUNCOES = carregar_desafio("04_funcoes.py")


def test_calcular_area_retangulo() -> None:
    assert FUNCOES.calcular_area_retangulo(4, 3) == 12


@pytest.mark.parametrize(("largura", "altura"), [(0, 3), (4, -1)])
def test_calcular_area_rejeita_dimensao_invalida(largura: float, altura: float) -> None:
    with pytest.raises(ValueError, match="maiores que zero"):
        FUNCOES.calcular_area_retangulo(largura, altura)


def test_formatar_saudacao_normaliza_nome_e_periodo() -> None:
    assert FUNCOES.formatar_saudacao("  Ana  ", "tarde") == "Bom tarde, Ana!"


def test_formatar_saudacao_rejeita_nome_vazio() -> None:
    with pytest.raises(ValueError, match="não pode estar vazio"):
        FUNCOES.formatar_saudacao("   ")


def test_main_exibe_saudacao_e_area(capsys: pytest.CaptureFixture[str]) -> None:
    FUNCOES.main()

    saida = capsys.readouterr().out
    assert "Bom dia, Matheus!" in saida
    assert "Área: 12.00" in saida
