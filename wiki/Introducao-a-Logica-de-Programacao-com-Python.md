# Introdução à Lógica de Programação com Python

## Objetivos de aprendizagem

Ao concluir esta página, você deverá ser capaz de:

- explicar o que são algoritmo, programa e lógica de programação;
- identificar entradas, processamento e saídas de um problema;
- reconhecer variáveis, tipos de dados, operadores e expressões;
- relacionar condições, repetições e funções à construção de algoritmos;
- executar um pequeno programa em Python e analisar seu comportamento.

## 1. Algoritmo, programa e pensamento computacional

Um **algoritmo** é uma sequência finita, ordenada e não ambígua de instruções para resolver um problema. Um **programa** é a implementação de um ou mais algoritmos em uma linguagem que o computador consegue interpretar ou executar.

A programação também desenvolve habilidades associadas ao **pensamento computacional**, como decomposição de problemas, reconhecimento de padrões, abstração e elaboração de procedimentos. Wing (2006) destaca que o pensamento computacional não se limita ao uso de computadores: ele é uma forma de organizar problemas e soluções de modo que possam ser representados e executados sistematicamente.

Na educação básica, a revisão de Lye e Koh (2014) encontrou evidências de que atividades de programação podem apoiar o pensamento computacional quando são acompanhadas por estratégias pedagógicas e ferramentas adequadas.

A literatura sobre ensino de programação mostra que iniciantes não aprendem apenas memorizando comandos. Eles precisam construir modelos mentais sobre como o programa executa cada instrução e como os dados mudam ao longo do tempo (ROBINS; ROUNTREE; ROUNTREE, 2003).

## 2. Decompondo um problema

Antes de escrever código, organize o problema em quatro perguntas:

1. **Entrada:** quais dados serão recebidos?
2. **Processamento:** quais regras ou cálculos serão aplicados?
3. **Saída:** qual resultado deverá ser apresentado?
4. **Validação:** quais valores são permitidos e quais erros podem ocorrer?

### Exemplo: calcular a média de duas notas

```text
Entrada: nota 1 e nota 2
Processamento: (nota 1 + nota 2) / 2
Saída: média calculada
Validação: aceitar apenas notas entre 0 e 10
```

Essa decomposição reduz a carga de memória durante a resolução do problema e facilita a aprendizagem progressiva, princípio coerente com estudos sobre carga cognitiva (SWELLER, 1988).

## 3. Variáveis e tipos de dados

Variáveis associam nomes a valores utilizados pelo programa. Em Python, o tipo é determinado dinamicamente a partir do valor atribuído.

```python
nome = "Ana"          # str: texto
idade = 20            # int: número inteiro
altura = 1.68         # float: número decimal
estudante = True      # bool: verdadeiro ou falso
```

Escolha nomes que expressem o significado do dado. `media_final` comunica melhor a intenção do que `m`.

### Atividade guiada

Analise o código:

```python
nome = "Carlos"
idade = 19
maior_de_idade = idade >= 18

print(nome)
print(maior_de_idade)
```

Responda:

- Qual é o tipo de `nome`?
- Qual é o tipo de `idade`?
- Por que `maior_de_idade` recebe `True`?

## 4. Operadores e expressões

Os operadores mais usados no início da aprendizagem são:

- aritméticos: `+`, `-`, `*`, `/`, `//`, `%` e `**`;
- comparação: `==`, `!=`, `<`, `<=`, `>` e `>=`;
- lógicos: `and`, `or` e `not`.

Uma **expressão** combina valores, variáveis e operadores para produzir um resultado.

```python
media = (8.0 + 7.0) / 2
aprovado = media >= 7
```

## 5. Estruturas fundamentais

### Condições

Condições selecionam caminhos diferentes conforme uma expressão booleana:

```python
if media >= 7:
    print("Aprovado")
else:
    print("Ainda não aprovado")
```

Veja [Estruturas Condicionais](Estruturas-Condicionais).

### Repetições

Repetições executam um bloco várias vezes. `for` percorre elementos de um iterável; `while` repete enquanto uma condição permanecer verdadeira, conforme a referência oficial da linguagem Python (PYTHON SOFTWARE FOUNDATION, 2026a).

Veja [Estruturas de Repetição](Estruturas-de-Repeticao).

### Funções

Funções agrupam uma responsabilidade reutilizável. Parâmetros recebem dados e `return` devolve um resultado.

Veja [Funções em Python](Funcoes-em-Python).

## 6. Primeiro programa completo

```python
def calcular_media(nota_1: float, nota_2: float) -> float:
    """Calcula a média aritmética de duas notas válidas."""
    if not 0 <= nota_1 <= 10 or not 0 <= nota_2 <= 10:
        raise ValueError("As notas devem estar entre 0 e 10.")
    return (nota_1 + nota_2) / 2


media = calcular_media(8.0, 7.0)
print(f"Média: {media:.1f}")
```

### Leitura passo a passo

1. A função recebe duas notas.
2. A condição rejeita valores fora do intervalo permitido.
3. O cálculo produz a média.
4. `return` devolve o resultado.
5. `print` apresenta a média com uma casa decimal.

## 7. Estratégia de estudo recomendada

Para cada conceito:

1. leia o exemplo;
2. preveja o resultado antes de executar;
3. execute o código;
4. altere um valor por vez;
5. explique o comportamento com suas próprias palavras;
6. escreva um teste simples.

A revisão de Robins, Rountree e Rountree (2003) indica que aprender programação envolve desenvolver conhecimento sintático, conceitual e estratégico. Por isso, apenas copiar códigos é insuficiente: é necessário prever, testar, explicar e corrigir.

## 8. Exercício prático

Crie um programa que:

- solicite o nome do estudante;
- receba duas notas;
- calcule a média;
- informe se o estudante foi aprovado;
- rejeite notas menores que 0 ou maiores que 10.

Depois compare sua solução com os arquivos das pastas `desafios/` e `exemplos/`.

## Referências

LYE, Sze Yee; KOH, Joyce Hwee Ling. Review on teaching and learning of computational thinking through programming: what is next for K-12? *Computers in Human Behavior*, v. 41, p. 51-61, 2014. DOI: <https://doi.org/10.1016/j.chb.2014.09.012>.

PYTHON SOFTWARE FOUNDATION. *The Python language reference: compound statements*. Versão 3.14. [S. l.], 2026a. Disponível em: <https://docs.python.org/3.14/reference/compound_stmts.html>. Acesso em: 2 ago. 2026.

ROBINS, Anthony; ROUNTREE, Janet; ROUNTREE, Nathan. Learning and teaching programming: a review and discussion. *Computer Science Education*, v. 13, n. 2, p. 137-172, 2003. DOI: <https://doi.org/10.1076/csed.13.2.137.14200>.

SWELLER, John. Cognitive load during problem solving: effects on learning. *Cognitive Science*, v. 12, n. 2, p. 257-285, 1988. DOI: <https://doi.org/10.1207/s15516709cog1202_4>.

WING, Jeannette M. Computational thinking. *Communications of the ACM*, v. 49, n. 3, p. 33-35, 2006. DOI: <https://doi.org/10.1145/1118178.1118215>.

[Voltar para Home](Home)
