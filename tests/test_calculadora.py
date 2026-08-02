"""Testes das operações da calculadora."""

import builtins

import pytest

from exemplos import calculadora
from exemplos.calculadora import calcular, dividir, multiplicar, somar, subtrair


@pytest.mark.parametrize(
    ("operacao", "primeiro", "segundo", "esperado"),
    [
        (somar, 2, 3, 5),
        (subtrair, 7, 4, 3),
        (multiplicar, 2.5, 4, 10),
        (dividir, 9, 2, 4.5),
    ],
)
def test_operacoes_basicas(operacao, primeiro, segundo, esperado) -> None:
    assert operacao(primeiro, segundo) == esperado


def test_divisao_por_zero_gera_erro() -> None:
    with pytest.raises(ZeroDivisionError, match="dividir por zero"):
        dividir(10, 0)


def test_calcular_seleciona_operacao() -> None:
    assert calcular(8, "*", 3) == 24


def test_calcular_rejeita_operador_desconhecido() -> None:
    with pytest.raises(ValueError, match="Operador inválido"):
        calcular(8, "%", 3)


def test_main_exibe_resultado(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    entradas = iter(["12", "/", "4"])
    monkeypatch.setattr(builtins, "input", lambda _mensagem: next(entradas))

    calculadora.main()

    assert "Resultado: 3" in capsys.readouterr().out


def test_main_trata_divisao_por_zero(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    entradas = iter(["12", "/", "0"])
    monkeypatch.setattr(builtins, "input", lambda _mensagem: next(entradas))

    calculadora.main()

    assert "Erro: Não é possível dividir por zero." in capsys.readouterr().out
