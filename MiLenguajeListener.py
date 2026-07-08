# Generated from MiLenguaje.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiLenguajeParser import MiLenguajeParser
else:
    from MiLenguajeParser import MiLenguajeParser

# This class defines a complete listener for a parse tree produced by MiLenguajeParser.
class MiLenguajeListener(ParseTreeListener):

    # Enter a parse tree produced by MiLenguajeParser#programa.
    def enterPrograma(self, ctx:MiLenguajeParser.ProgramaContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#programa.
    def exitPrograma(self, ctx:MiLenguajeParser.ProgramaContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#declaracion_vars.
    def enterDeclaracion_vars(self, ctx:MiLenguajeParser.Declaracion_varsContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#declaracion_vars.
    def exitDeclaracion_vars(self, ctx:MiLenguajeParser.Declaracion_varsContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#declaracion.
    def enterDeclaracion(self, ctx:MiLenguajeParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#declaracion.
    def exitDeclaracion(self, ctx:MiLenguajeParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#cuerpo_principal.
    def enterCuerpo_principal(self, ctx:MiLenguajeParser.Cuerpo_principalContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#cuerpo_principal.
    def exitCuerpo_principal(self, ctx:MiLenguajeParser.Cuerpo_principalContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#sentencia.
    def enterSentencia(self, ctx:MiLenguajeParser.SentenciaContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#sentencia.
    def exitSentencia(self, ctx:MiLenguajeParser.SentenciaContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#asignacion.
    def enterAsignacion(self, ctx:MiLenguajeParser.AsignacionContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#asignacion.
    def exitAsignacion(self, ctx:MiLenguajeParser.AsignacionContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#lectura.
    def enterLectura(self, ctx:MiLenguajeParser.LecturaContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#lectura.
    def exitLectura(self, ctx:MiLenguajeParser.LecturaContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#escritura.
    def enterEscritura(self, ctx:MiLenguajeParser.EscrituraContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#escritura.
    def exitEscritura(self, ctx:MiLenguajeParser.EscrituraContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#expr_escritura.
    def enterExpr_escritura(self, ctx:MiLenguajeParser.Expr_escrituraContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#expr_escritura.
    def exitExpr_escritura(self, ctx:MiLenguajeParser.Expr_escrituraContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#condicional.
    def enterCondicional(self, ctx:MiLenguajeParser.CondicionalContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#condicional.
    def exitCondicional(self, ctx:MiLenguajeParser.CondicionalContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#repetitiva.
    def enterRepetitiva(self, ctx:MiLenguajeParser.RepetitivaContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#repetitiva.
    def exitRepetitiva(self, ctx:MiLenguajeParser.RepetitivaContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#ExprSumaResta.
    def enterExprSumaResta(self, ctx:MiLenguajeParser.ExprSumaRestaContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#ExprSumaResta.
    def exitExprSumaResta(self, ctx:MiLenguajeParser.ExprSumaRestaContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#ExprPotencia.
    def enterExprPotencia(self, ctx:MiLenguajeParser.ExprPotenciaContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#ExprPotencia.
    def exitExprPotencia(self, ctx:MiLenguajeParser.ExprPotenciaContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#ExprNumero.
    def enterExprNumero(self, ctx:MiLenguajeParser.ExprNumeroContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#ExprNumero.
    def exitExprNumero(self, ctx:MiLenguajeParser.ExprNumeroContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#ExprParens.
    def enterExprParens(self, ctx:MiLenguajeParser.ExprParensContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#ExprParens.
    def exitExprParens(self, ctx:MiLenguajeParser.ExprParensContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#ExprMultDiv.
    def enterExprMultDiv(self, ctx:MiLenguajeParser.ExprMultDivContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#ExprMultDiv.
    def exitExprMultDiv(self, ctx:MiLenguajeParser.ExprMultDivContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#ExprRaiz.
    def enterExprRaiz(self, ctx:MiLenguajeParser.ExprRaizContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#ExprRaiz.
    def exitExprRaiz(self, ctx:MiLenguajeParser.ExprRaizContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#ExprID.
    def enterExprID(self, ctx:MiLenguajeParser.ExprIDContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#ExprID.
    def exitExprID(self, ctx:MiLenguajeParser.ExprIDContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#CondOr.
    def enterCondOr(self, ctx:MiLenguajeParser.CondOrContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#CondOr.
    def exitCondOr(self, ctx:MiLenguajeParser.CondOrContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#CondAnd.
    def enterCondAnd(self, ctx:MiLenguajeParser.CondAndContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#CondAnd.
    def exitCondAnd(self, ctx:MiLenguajeParser.CondAndContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#CondNegacion.
    def enterCondNegacion(self, ctx:MiLenguajeParser.CondNegacionContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#CondNegacion.
    def exitCondNegacion(self, ctx:MiLenguajeParser.CondNegacionContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#CondRelacional.
    def enterCondRelacional(self, ctx:MiLenguajeParser.CondRelacionalContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#CondRelacional.
    def exitCondRelacional(self, ctx:MiLenguajeParser.CondRelacionalContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#CondParens.
    def enterCondParens(self, ctx:MiLenguajeParser.CondParensContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#CondParens.
    def exitCondParens(self, ctx:MiLenguajeParser.CondParensContext):
        pass



del MiLenguajeParser