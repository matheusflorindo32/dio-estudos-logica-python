"""Utilitários compartilhados pelos testes dos desafios numerados."""

import importlib.util
from pathlib import Path
from types import ModuleType


def carregar_desafio(nome_arquivo: str) -> ModuleType:
    """Carrega um desafio cujo nome de arquivo não é um identificador Python."""
    caminho = Path(__file__).parents[1] / "desafios" / nome_arquivo
    nome_modulo = f"desafio_{caminho.stem}"
    especificacao = importlib.util.spec_from_file_location(nome_modulo, caminho)
    if especificacao is None or especificacao.loader is None:
        raise RuntimeError(f"Não foi possível carregar {nome_arquivo}.")

    modulo = importlib.util.module_from_spec(especificacao)
    especificacao.loader.exec_module(modulo)
    return modulo
