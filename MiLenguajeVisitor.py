# Generated from MiLenguaje.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiLenguajeParser import MiLenguajeParser
else:
    from MiLenguajeParser import MiLenguajeParser

# This class defines a complete generic visitor for a parse tree produced by MiLenguajeParser.

class MiLenguajeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiLenguajeParser#programa.
    def visitPrograma(self, ctx:MiLenguajeParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#declaracion_vars.
    def visitDeclaracion_vars(self, ctx:MiLenguajeParser.Declaracion_varsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#declaracion.
    def visitDeclaracion(self, ctx:MiLenguajeParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#cuerpo_principal.
    def visitCuerpo_principal(self, ctx:MiLenguajeParser.Cuerpo_principalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#sentencia.
    def visitSentencia(self, ctx:MiLenguajeParser.SentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#asignacion.
    def visitAsignacion(self, ctx:MiLenguajeParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#lectura.
    def visitLectura(self, ctx:MiLenguajeParser.LecturaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#escritura.
    def visitEscritura(self, ctx:MiLenguajeParser.EscrituraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#expr_escritura.
    def visitExpr_escritura(self, ctx:MiLenguajeParser.Expr_escrituraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#condicional.
    def visitCondicional(self, ctx:MiLenguajeParser.CondicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#repetitiva.
    def visitRepetitiva(self, ctx:MiLenguajeParser.RepetitivaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#ExprSumaResta.
    def visitExprSumaResta(self, ctx:MiLenguajeParser.ExprSumaRestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#ExprPotencia.
    def visitExprPotencia(self, ctx:MiLenguajeParser.ExprPotenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#ExprNumero.
    def visitExprNumero(self, ctx:MiLenguajeParser.ExprNumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#ExprParens.
    def visitExprParens(self, ctx:MiLenguajeParser.ExprParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#ExprMultDiv.
    def visitExprMultDiv(self, ctx:MiLenguajeParser.ExprMultDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#ExprRaiz.
    def visitExprRaiz(self, ctx:MiLenguajeParser.ExprRaizContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#ExprID.
    def visitExprID(self, ctx:MiLenguajeParser.ExprIDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#CondOr.
    def visitCondOr(self, ctx:MiLenguajeParser.CondOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#CondAnd.
    def visitCondAnd(self, ctx:MiLenguajeParser.CondAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#CondNegacion.
    def visitCondNegacion(self, ctx:MiLenguajeParser.CondNegacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#CondRelacional.
    def visitCondRelacional(self, ctx:MiLenguajeParser.CondRelacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiLenguajeParser#CondParens.
    def visitCondParens(self, ctx:MiLenguajeParser.CondParensContext):
        return self.visitChildren(ctx)



del MiLenguajeParser