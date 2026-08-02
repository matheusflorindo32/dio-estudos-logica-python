"""Testes do desafio de estruturas condicionais."""

import pytest

from tests.helpers import carregar_desafio

CONDICIONAIS = carregar_desafio("02_condicionais.py")


@pytest.mark.parametrize(
    ("nota", "classificacao"),
    [
        (10, "Excelente"),
        (9, "Excelente"),
        (8.9, "Bom"),
        (7, "Bom"),
        (6.9, "Regular"),
        (5, "Regular"),
        (4.9, "Precisa melhorar"),
        (0, "Precisa melhorar"),
    ],
)
def test_classificar_nota(nota: float, classificacao: str) -> None:
    assert CONDICIONAIS.classificar_nota(nota) == classificacao


@pytest.mark.parametrize("nota", [-0.1, 10.1])
def test_classificar_nota_rejeita_valor_invalido(nota: float) -> None:
    with pytest.raises(ValueError, match="entre 0 e 10"):
        CONDICIONAIS.classificar_nota(nota)


def test_gerar_feedback_reutiliza_classificacao() -> None:
    feedback = CONDICIONAIS.gerar_feedback_desempenho(9)

    assert feedback.startswith("Excelente:")
    assert "aprofundando" in feedback


def test_ler_nota_repete_ate_receber_valor_valido(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    entradas = iter(["texto", "11", "8,5"])
    monkeypatch.setattr("builtins.input", lambda _mensagem: next(entradas))

    assert CONDICIONAIS.ler_nota() == 8.5
    assert capsys.readouterr().out.count("Entrada inválida") == 2


def test_main_exibe_classificacao_e_feedback(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setattr(CONDICIONAIS, "ler_nota", lambda: 9.0)

    CONDICIONAIS.main()

    saida = capsys.readouterr().out
    assert "Classificação: Excelente" in saida
    assert "Feedback: Excelente" in saida
