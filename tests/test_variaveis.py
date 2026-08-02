"""Testes do desafio de variáveis e tipos de dados."""

import builtins

import pytest

from tests.helpers import carregar_desafio

VARIAVEIS = carregar_desafio("01_variaveis.py")


def test_calcular_ano_nascimento() -> None:
    assert VARIAVEIS.calcular_ano_nascimento(20, 2026) == 2006


def test_calcular_ano_nascimento_rejeita_idade_negativa() -> None:
    with pytest.raises(ValueError, match="não pode ser negativa"):
        VARIAVEIS.calcular_ano_nascimento(-1)


def test_ler_idade_repete_ate_receber_inteiro_valido(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    entradas = iter(["texto", "-1", "20"])
    monkeypatch.setattr(builtins, "input", lambda _mensagem: next(entradas))

    assert VARIAVEIS.ler_idade() == 20
    assert capsys.readouterr().out.count("Informe uma idade") == 2


@pytest.mark.parametrize(
    ("entrada_nome", "nome_exibido"), [("Ana", "Ana"), ("   ", "Estudante")]
)
def test_main_exibe_apresentacao_formatada(
    entrada_nome: str,
    nome_exibido: str,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    monkeypatch.setattr(builtins, "input", lambda _mensagem: entrada_nome)
    monkeypatch.setattr(VARIAVEIS, "ler_idade", lambda: 20)

    VARIAVEIS.main()

    saida = capsys.readouterr().out
    assert f"Olá, {nome_exibido}!" in saida
    assert "2006" in saida
    assert "str" in saida and "int" in saida
