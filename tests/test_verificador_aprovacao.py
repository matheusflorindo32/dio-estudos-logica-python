"""Testes de média, validação de notas e classificação."""

import builtins
import math

import pytest

from exemplos import verificador_aprovacao
from exemplos.verificador_aprovacao import calcular_media, classificar_aprovacao


def test_calcular_media() -> None:
    assert calcular_media([7.0, 8.0, 9.0]) == pytest.approx(8.0)


@pytest.mark.parametrize("notas", [[], [-1.0, 8.0], [7.0, 11.0], [math.nan]])
def test_calcular_media_rejeita_notas_invalidas(notas: list[float]) -> None:
    with pytest.raises(ValueError):
        calcular_media(notas)


@pytest.mark.parametrize(
    ("media", "situacao"),
    [
        (10.0, "Aprovado"),
        (7.0, "Aprovado"),
        (6.9, "Recuperação"),
        (5.0, "Recuperação"),
        (4.9, "Reprovado"),
        (0.0, "Reprovado"),
    ],
)
def test_classificar_aprovacao(media: float, situacao: str) -> None:
    assert classificar_aprovacao(media) == situacao


@pytest.mark.parametrize("media", [-0.1, 10.1, math.inf])
def test_classificar_aprovacao_rejeita_media_invalida(media: float) -> None:
    with pytest.raises(ValueError, match="entre 0 e 10"):
        classificar_aprovacao(media)


def test_main_exibe_media_e_situacao(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setattr(builtins, "input", lambda _mensagem: "7,0 8,0")

    verificador_aprovacao.main()

    saida = capsys.readouterr().out
    assert "Média: 7.50" in saida
    assert "Situação: Aprovado" in saida


def test_main_trata_entrada_invalida(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setattr(builtins, "input", lambda _mensagem: "nota-inválida")

    verificador_aprovacao.main()

    assert "Erro:" in capsys.readouterr().out
