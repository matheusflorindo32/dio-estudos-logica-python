"""Smoke tests que confirmam a execução direta dos oito scripts educacionais."""

import builtins
import runpy
from pathlib import Path

import pytest


@pytest.mark.parametrize(
    ("caminho_relativo", "entradas"),
    [
        ("desafios/01_variaveis.py", ["Ana", "20"]),
        ("desafios/02_condicionais.py", ["8"]),
        ("desafios/03_repeticoes.py", []),
        ("desafios/04_funcoes.py", []),
        ("desafios/05_listas.py", []),
        ("exemplos/calculadora.py", ["12", "+", "3"]),
        ("exemplos/organizador_estudos.py", ["0"]),
        ("exemplos/verificador_aprovacao.py", ["7 8"]),
    ],
)
def test_script_executa_como_programa_principal(
    caminho_relativo: str,
    entradas: list[str],
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    caminho = Path(__file__).parents[1] / caminho_relativo
    iterador_entradas = iter(entradas)
    monkeypatch.setattr(builtins, "input", lambda _mensagem: next(iterador_entradas))

    runpy.run_path(str(caminho), run_name="__main__")

    assert capsys.readouterr().out.strip()
