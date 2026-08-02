"""Testes do desafio de estruturas condicionais."""

import importlib.util
from pathlib import Path
from types import ModuleType

import pytest


def carregar_modulo_condicionais() -> ModuleType:
    """Carrega o desafio cujo nome começa com número."""
    caminho = Path(__file__).parents[1] / "desafios" / "02_condicionais.py"
    especificacao = importlib.util.spec_from_file_location("condicionais", caminho)
    if especificacao is None or especificacao.loader is None:
        raise RuntimeError("Não foi possível carregar o desafio de condicionais.")
    modulo = importlib.util.module_from_spec(especificacao)
    especificacao.loader.exec_module(modulo)
    return modulo


CONDICIONAIS = carregar_modulo_condicionais()


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

