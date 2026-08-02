# Estudos de Lógica de Programação com Python

Bem-vindo à Wiki do projeto. Este espaço organiza conceitos fundamentais, exemplos e caminhos de estudo para quem está começando a programar com Python. A proposta combina leitura, previsão, execução e teste — práticas que ajudam a transformar comandos isolados em estratégias de resolução de problemas (ROBINS; ROUNTREE; ROUNTREE, 2003).

## Objetivos de aprendizagem

Ao percorrer a Wiki, você deverá ser capaz de:

- decompor um problema em entrada, processamento, validação e saída;
- reconhecer variáveis, condições, repetições e funções;
- prever a execução de pequenos algoritmos antes de rodá-los;
- aplicar os conceitos nos desafios do repositório;
- usar testes para verificar comportamentos esperados e entradas inválidas.

## Pré-requisitos

- Python 3.11 ou superior instalado;
- um terminal e um editor de texto;
- disposição para executar, observar e modificar exemplos pequenos.

Não é necessário conhecimento prévio de programação.

## Índice

- [Introdução à Lógica de Programação com Python](Introducao-a-Logica-de-Programacao-com-Python)
- [Estruturas Condicionais](Estruturas-Condicionais)
- [Estruturas de Repetição](Estruturas-de-Repeticao)
- [Funções em Python](Funcoes-em-Python)

## Como usar esta Wiki

Comece pela introdução e avance na ordem do índice. Os exemplos completos ficam nas pastas `desafios/` e `exemplos/` do repositório principal.

1. Leia os objetivos da página.
2. Analise os exemplos linha por linha.
3. Preveja o resultado antes de executar.
4. Modifique uma entrada ou regra por vez.
5. Resolva a atividade proposta e escreva ao menos um teste.

## Exemplo inicial comentado

```python
nome = "Ana"  # Armazena um texto em uma variável.

if nome:  # Uma string não vazia é avaliada como verdadeira.
    print(f"Olá, {nome}!")
```

### Leitura passo a passo

1. a variável `nome` recebe uma string;
2. `if nome` verifica se a string não está vazia;
3. a f-string insere o valor na mensagem;
4. `print` produz a saída observável no terminal.

## Aplicação prática

Use esta Wiki junto com o [repositório principal](https://github.com/matheusflorindo32/dio-estudos-logica-python). Cada página indica um desafio executável e conceitos que podem ser verificados pelos testes automatizados.

## Erros comuns de estudo

- copiar um exemplo sem prever seu resultado;
- alterar várias partes do código ao mesmo tempo;
- ignorar mensagens de erro em vez de interpretá-las;
- testar somente o caso de sucesso;
- avançar sem conseguir explicar como as variáveis mudam.

## Boas práticas de aprendizagem

- execute um exemplo antes e depois de modificá-lo;
- altere apenas uma variável por tentativa;
- anote a saída prevista antes de observar a saída real;
- trate mensagens de erro como evidência para investigação;
- valide também limites e entradas inválidas.

## Exercício guiado

Escolha uma página do índice, execute o desafio correspondente e registre: entrada utilizada, resultado previsto, resultado observado e uma mudança que você conseguiu explicar.

## Exercício independente

Escolha um problema cotidiano simples, descreva suas entradas, regras e saídas e indique se cada regra exige uma condição, uma repetição ou uma função. Depois implemente a menor versão executável e escreva um teste para um caso de fronteira.

## Referências

ROBINS, Anthony; ROUNTREE, Janet; ROUNTREE, Nathan. Learning and teaching programming: a review and discussion. *Computer Science Education*, v. 13, n. 2, p. 137-172, 2003. DOI: <https://doi.org/10.1076/csed.13.2.137.14200>.

[Voltar para Home](Home)
