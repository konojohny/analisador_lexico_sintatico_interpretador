class Numero:

    def __init__(self, valor):

        self.valor = valor

    def __repr__(self):

        return f"Numero({self.valor})"

class Variavel:

    def __init__(self, nome):

        self.nome = nome

    def __repr__(self):

        return f"Variavel({self.nome})"

class Binaria:

    def __init__(self, esquerda, op, direita):

        self.esq = esquerda
        self.op = op
        self.dir = direita

    def __repr__(self):

        return f"Bin({self.esq}, '{self.op}', {self.dir})"

class Atrib:
    def __init__(self, nome, expr):

        self.nome = nome
        self.expr = expr

    def __repr__(self):

        return f"Atrib({self.nome}, {self.expr})"

class CmdPrint:
    def __init__(self, expr):
        
        self.expr = expr

    def __repr__(self):
        
        return f"Print({self.expr})"