from ast import Numero, Variavel, Binaria, Atrib, CmdPrint

class Parser:
    def __init__(self, tokens):

        self.tks = tokens
        self.pos = 0

    def atual(self):

        return self.tks[self.pos] if self.pos < len(self.tks) else None

    def comer_tipo(self, tipo):

        if self.atual().tipo == tipo:

            self.pos += 1

        else:

            raise Exception("Esperado tipo " + tipo)

    def comer_val(self, v):

        if self.atual().valor == v:

            self.pos += 1

        else:

            raise Exception("Esperado valor " + v)

    def parse(self):

        linhas = []

        while self.atual():

            linhas.append(self.linha())

            if self.atual() and self.atual().tipo == "EOL":

                self.pos += 1

        return linhas

    def linha(self):

        tk = self.atual()

        if tk.tipo == "PRINT":

            return self.cmd_print()

        if tk.tipo == "ID":

            return self.cmd_atrib()

        raise Exception("Linha inválida")

    def cmd_print(self):

        self.comer_tipo("PRINT")

        expr = self.expr()

        return CmdPrint(expr)

    def cmd_atrib(self):

        nome = self.atual().valor

        self.comer_tipo("ID")

        self.comer_val("=")

        val = self.expr()

        return Atrib(nome, val)

    def expr(self):

        node = self.termo()

        while self.atual() and self.atual().valor in ("+", "-"):

            op = self.atual().valor

            self.pos += 1

            node = Binaria(node, op, self.termo())

        return node

    def termo(self):

        node = self.fator()
        
        while self.atual() and self.atual().valor in ("*", "/"):

            op = self.atual().valor

            self.pos += 1

            node = Binaria(node, op, self.fator())

        return node

    def fator(self):

        tk = self.atual()

        if tk.tipo == "NUM":

            self.pos += 1

            return Numero(tk.valor)

        if tk.tipo == "ID":

            self.pos += 1

            return Variavel(tk.valor)

        if tk.tipo == "PAR" and tk.valor == "(":

            self.pos += 1

            no = self.expr()

            self.comer_val(")")
            
            return no

        raise Exception("Fator inválido")