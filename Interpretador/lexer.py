class Token:
    def __init__(self, tipo, valor):

        self.tipo = tipo
        
        self.valor = valor

    def __repr__(self):

        return f"{self.tipo}:{self.valor}"


class Lexer:
    def __init__(self, texto):

        self.txt = texto
        self.pos = 0
        self.ch = texto[0] if texto else None

    def avançar(self):

        self.pos += 1

        if self.pos < len(self.txt):

            self.ch = self.txt[self.pos]

        else:

            self.ch = None

    def pular_espacos(self):
        while self.ch == " ":
            self.avançar()

    def numero(self):

        val = ""

        while self.ch and self.ch.isdigit():

            val += self.ch

            self.avançar()

        return Token("NUM", int(val))

    def ident(self):

        val = ""

        while self.ch and self.ch.isalpha():

            val += self.ch

            self.avançar()

        if val == "print":

            return Token("PRINT", val)

        return Token("ID", val)

    def tokens(self):
        tks = []

        while self.ch is not None:

            if self.ch == " ":

                self.pular_espacos()

                continue

            if self.ch == "\n":

                tks.append(Token("EOL", "\\n"))

                self.avançar()

                continue

            if self.ch.isdigit():

                tks.append(self.numero())

                continue

            if self.ch.isalpha():

                tks.append(self.ident())

                continue

            if self.ch in "+-*/=":

                tks.append(Token("OP", self.ch))

                self.avançar()

                continue

            if self.ch in "()":

                tks.append(Token("PAR", self.ch))

                self.avançar()

                continue

            raise Exception("Caractere inválido: " + self.ch)

        return tks
