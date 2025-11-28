Mini Linguagem – Analisador Léxico, Sintático e Interpretador
Projeto acadêmico desenvolvido para a disciplina de Compiladores (4º Período)
<p align="center"> <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge"> <img src="https://img.shields.io/badge/Projeto-Acad%C3%AAmico-green?style=for-the-badge"> <img src="https://img.shields.io/badge/Compiladores-Parser%20%7C%20Lexer-orange?style=for-the-badge"> </p>
✨ Visão Geral

Este projeto implementa uma mini linguagem de programação com:

✔ Analisador Léxico (Lexer)

✔ Analisador Sintático (Parser)

✔ Árvore Sintática Abstrata (AST)

✔ Interpretador capaz de executar o código

Tudo foi construído em Python puro, sem bibliotecas externas, com foco total em aprendizado dos conceitos fundamentais de compiladores.

🔤 Como é a linguagem?

A linguagem possui apenas três construções:

🟦 Atribuições
x = 10
y = x + 2

🟩 Impressão
print y

🟪 Expressões aritméticas
+   -   *   /

🟨 Parênteses
a = (10 + 2) * 3


Simples, clara e didática — ideal para entender os fundamentos.

📁 Estrutura do Projeto
📦 mini_linguagem_compiladores
│
├── ast.py        # Estruturas da AST
├── lexer.py      # Tokenizador
├── parser.py     # Analisador sintático
├── interp.py     # Interpretador da AST
└── main.py       # Arquivo principal para testes

⚙ Como Funciona o Sistema
🔹 1. Lexer

Lê o texto caractere por caractere e transforma em tokens como:

ID:x
OP:=
NUM:10

🔹 2. Parser

Recebe os tokens e monta a AST usando a gramática:

linha  ::= print expr
linha  ::= ID "=" expr
expr   ::= termo ( ("+"|"-") termo )*
termo  ::= fator ( ("*"|"/") fator )*
fator  ::= NUM | ID | "(" expr ")"

🔹 3. AST

Representação interna do programa, por exemplo:

Atrib(y, Bin(Variavel(x), '+', Bin(Numero(3), '*', Numero(2))))

🔹 4. Interpretador

Executa a árvore, armazenando variáveis em uma "memória" (dicionário Python).

📌 Exemplo:

Código:

x = 10
y = x + 3 * 2
print y


Saída:

16

▶ Como Executar o Projeto
1️⃣ Instale o Python

https://www.python.org/downloads/

Marque:

[✓] Add Python to PATH

2️⃣ Rode o projeto
python main.py

3️⃣ Personalize o código de teste no main.py
🧪 Exemplos de Programas
➤ Exemplo 1
a = 5
b = a + 10
print b


Saída:

15

➤ Exemplo 2
x = (10 + 2) * 3
print x


Saída:

36

🧱 Desafios e Aprendizado

O principal desafio foi a falta de familiaridade com linguagens além do T-SQL, especialmente em relação à sintaxe do Python, indentação e estrutura de código.
Para superar isso, foram consultados:

vídeos no YouTube

documentação básica de Python

apoio do ChatGPT para dúvidas específicas

Playlist usada durante o projeto:
📌 https://www.youtube.com/playlist?list=PLnzT8EWpmbkbhjiGmqGh0lbpZLsLpBeLY

Esse processo ajudou a entender o funcionamento de um compilador básico e fortaleceu conceitos de estruturas de linguagem.
