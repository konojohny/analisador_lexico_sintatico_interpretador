def executar(ast):

    memoria = {} 

    for comando in ast:
        executar_comando(
            comando, 
            memoria
        )


def executar_comando(cmd, memoria):

    tipo = cmd.__class__.__name__

    if tipo == "Atrib":
        valor = avaliar_expr(
            cmd.expr, 
            memoria
        )

        memoria[cmd.nome] = valor

    elif tipo == "CmdPrint":
        valor = avaliar_expr(
            cmd.expr, 
            memoria
        )

        print(valor)

    else:

        raise Exception("Comando desconhecido: " + tipo)


def avaliar_expr(expr, memoria):

    tipo = expr.__class__.__name__

    if tipo == "Numero":

        return expr.valor

    if tipo == "Variavel":

        return memoria.get(
            expr.nome, 
            0
        )

    if tipo == "Binaria":

        esquerda = avaliar_expr(
            expr.esq, 
            memoria
        )

        direita = avaliar_expr(
            expr.dir, 
            memoria
        )

        if expr.op == "+":

            return esquerda + direita
        elif expr.op == "-":

            return esquerda - direita
        elif expr.op == "*":

            return esquerda * direita
        elif expr.op == "/":

            return esquerda / direita
        else:
            
            raise Exception("Operador desconhecido: " + expr.op)

    raise Exception("Expressão inválida: " + tipo)