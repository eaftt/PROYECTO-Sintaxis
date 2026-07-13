from MiLenguajeVisitor import MiLenguajeVisitor
from ast_nodos import *

class ConstructorAST(MiLenguajeVisitor):

    def visitPrograma(self, ctx):
        declaraciones = self.visit(ctx.declaracion_vars())
        sentencias = self.visit(ctx.cuerpo_principal())
        return programa(declaraciones, sentencis)

    def visitCuerpo_principal(self, ctx):
        lista_sentencias = []
        for sent_ctx in ctx.sentencia():
            nodo_sentencia = self.visit(sent_ctx)
            if nodo_sentencia is not None: 
                lista_sentencias.append(nodo_sentencia)
        return lista_sentencias


