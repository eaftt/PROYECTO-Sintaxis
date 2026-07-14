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
    
    def visitExprParens(self, ctx):
        return self.visit(ctx.expr())
        
    def visitLectura(self, ctx):
        nombre_var = ctx.ID().getText()
        return Entrada(nombre_var)

    def visitEscritura(self, ctx):
        return Salida("Texto de salida", [])

    def visitRepetitiva(self, ctx):
        nodo_condicion = self.visit(ctx.condicion())
        
        sentencias_ciclo = []
        for sent_ctx in ctx.sentencia():
            nodo = self.visit(sent_ctx)
            if nodo is not None:
                sentencias_ciclo.append(nodo)
        return Ciclo(nodo_condicion, sentencias_ciclo)

    def visitCondicional(self, ctx):
        nodo_condicion = self.visit(ctx.condicion())    
        return Condicional(nodo_condicion, [], [])
