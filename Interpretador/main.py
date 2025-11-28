from lexer import Lexer
from parser import Parser
from interp import executar

codigo = """a = 5
b = a + 10
print b
"""

lx = Lexer(codigo)

tks = lx.tokens()

parser = Parser(tks)

arvore = parser.parse()

print("Resultado:")

executar(arvore)