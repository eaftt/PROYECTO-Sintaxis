from MiLenguajeVisitor import MiLenguajeVisitor
from ast_nodos import *

class ConstructorAST(MiLenguajeVisitor):

    def visitPrograma(self, ctx):
        declaraciones = self.visit(ctx.declaracion_vars())
        sentencias = self.visit(ctx.cuerpo_principal())
        return programa(declaraciones, sentencias)

    def visitCuerpo_principal(self, ctx):
        lista_sentencias = []
        for sent_ctx in ctx.sentencia():
            nodo_sentencia = self.visit(sent_ctx)
            if nodo_sentencia is not None: 
                lista_sentencias.append(nodo_sentencia)
        return lista_sentencias

    def visitDeclaracion_vars(self, ctx):
        declaraciones = []
        for decl in ctx.declaracion():
            declaraciones.append(self.visit(decl))
        return declaraciones
    
    def visitDeclaracion(self, ctx):
        variables = []
        for identificador in ctx.ID():
            variables.append(identificador.getText())
        return Declaracion(variables)


    def visitAsignacion(self, ctx):
        nombre_var = ctx.ID().getText()
        nodo_expr = self.visit(ctx.expr())
        return Asignacion(nombre_var, nodo_expr)

    def visitExprNumero(self, ctx):
        texto_numero = ctx.NUMERO_REAL().getText()
        return NumeroReal(texto_numero)

    def visitExprID(self, ctx):
        nombre_var = ctx.ID().getText()
        return VariableID(nombre_var)

    def visitExprSumaResta(self, ctx):
        nodo_izq = self.visit(ctx.expr(0))
        nodo_der = self.visit(ctx.expr(1))
        operador = ctx.getChild(1).getText()
        return OperacionBinaria(nodo_izq, operador, nodo_der)

    def visitExprMultDiv(self, ctx):
        nodo_izq = self.visit(ctx.expr(0))
        nodo_der = self.visit(ctx.expr(1))
        operador = ctx.getChild(1).getText()
        return OperacionBinaria(nodo_izq, operador, nodo_der)
    
    def visitExprPotencia(self, ctx):
        izquierda = self.visit(ctx.expr(0))
        derecha = self.visit(ctx.expr(1))
        operador = ctx.getChild(1).getText()
        return OperacionBinaria(
            izquierda,
            operador,
            derecha
        )

    def visitExprRaiz(self, ctx):
        expresion = self.visit(ctx.expr())
        return Raiz(expresion)

    
    def visitExprParens(self, ctx):
        return self.visit(ctx.expr())
        
    def visitLectura(self, ctx):
        nombre_var = ctx.ID().getText()
        return Entrada(nombre_var)

    def visitExpr_escritura(self, ctx):
        if ctx.CADENA():
            return ctx.CADENA().getText()
        else:
            return self.visit(ctx.expr())

    def visitEscritura(self, ctx):
        cadenas = []
        expresiones = []

        for elemento in ctx.expr_escritura():
            resultado = self.visit(elemento)

            if isinstance(resultado, str):
                cadenas.append(resultado)
            else:
                expresiones.append(resultado)

        return Salida(cadenas, expresiones)


    def visitCondRelacional(self, ctx):
        izquierda = self.visit(ctx.expr(0))
        derecha = self.visit(ctx.expr(1))
        operador = ctx.OP_REL().getText()
        return Comparacion(izquierda, operador, derecha)


    def visitCondNegacion(self, ctx):
        condicion = self.visit(ctx.condicion())
        return Negacion(condicion)


    def visitCondAnd(self, ctx):
        izquierda = self.visit(ctx.condicion(0))
        derecha = self.visit(ctx.condicion(1))
        return And(izquierda, derecha)


    def visitCondOr(self, ctx):
        izquierda = self.visit(ctx.condicion(0))
        derecha = self.visit(ctx.condicion(1))
        return Or(izquierda, derecha)


    def visitCondParens(self, ctx):
        return self.visit(ctx.condicion())

    def visitRepetitiva(self, ctx):
        nodo_condicion = self.visit(ctx.condicion())

        sentencias = []

        for sentencia_ctx in ctx.sentencia():
            nodo = self.visit(sentencia_ctx)
            if nodo is not None:
                sentencias.append(nodo)

        return Ciclo(nodo_condicion, sentencias)
    
    def visitCondicional(self, ctx):
        nodo_condicion = self.visit(ctx.condicion())

        sentencias = []
        sentencias_else = []

        indice_fallback = -1
        for i in range(ctx.getChildCount()):
            if "fallback" in ctx.getChild(i).getText():
                indice_fallback = i
                break

        if indice_fallback != -1:
            for s in ctx.sentencia():
                nodo = self.visit(s)
                if nodo is not None:
                    posicion_sentencia = -1
                    for i in range(ctx.getChildCount()):
                        if ctx.getChild(i) == s:
                            posicion_sentencia = i
                            break
                    
                    if posicion_sentencia < indice_fallback:
                        sentencias.append(nodo)
                    else:
                        sentencias_else.append(nodo)
        else:
            for s in ctx.sentencia():
                nodo = self.visit(s)
                if nodo is not None:
                    sentencias.append(nodo)

        return Condicional(
            nodo_condicion,
            sentencias,
            sentencias_else
        )
