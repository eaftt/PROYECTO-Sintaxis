# Generated from MiLenguaje.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,31,201,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        1,0,1,0,1,1,1,1,1,1,1,1,5,1,35,8,1,10,1,12,1,38,9,1,1,1,1,1,3,1,
        42,8,1,1,2,1,2,1,2,1,2,1,2,5,2,49,8,2,10,2,12,2,52,9,2,1,2,1,2,1,
        3,1,3,1,3,1,3,5,3,60,8,3,10,3,12,3,63,9,3,1,3,1,3,3,3,67,8,3,1,4,
        1,4,1,4,1,4,1,4,1,4,3,4,75,8,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,
        6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,5,7,93,8,7,10,7,12,7,96,9,7,1,7,1,
        7,1,7,1,8,1,8,3,8,103,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,112,8,
        9,10,9,12,9,115,9,9,1,9,1,9,1,9,1,9,1,9,5,9,122,8,9,10,9,12,9,125,
        9,9,1,9,3,9,128,8,9,1,9,3,9,131,8,9,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,5,10,140,8,10,10,10,12,10,143,9,10,1,10,1,10,3,10,147,8,10,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,
        161,8,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,5,11,172,8,
        11,10,11,12,11,175,9,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,3,12,188,8,12,1,12,1,12,1,12,1,12,1,12,1,12,5,12,
        196,8,12,10,12,12,12,199,9,12,1,12,0,2,22,24,13,0,2,4,6,8,10,12,
        14,16,18,20,22,24,0,2,1,0,18,19,1,0,20,21,215,0,26,1,0,0,0,2,30,
        1,0,0,0,4,43,1,0,0,0,6,55,1,0,0,0,8,74,1,0,0,0,10,76,1,0,0,0,12,
        81,1,0,0,0,14,87,1,0,0,0,16,102,1,0,0,0,18,104,1,0,0,0,20,132,1,
        0,0,0,22,160,1,0,0,0,24,187,1,0,0,0,26,27,3,2,1,0,27,28,3,6,3,0,
        28,29,5,0,0,1,29,1,1,0,0,0,30,31,5,1,0,0,31,32,5,2,0,0,32,36,5,29,
        0,0,33,35,3,4,2,0,34,33,1,0,0,0,35,38,1,0,0,0,36,34,1,0,0,0,36,37,
        1,0,0,0,37,39,1,0,0,0,38,36,1,0,0,0,39,41,5,3,0,0,40,42,5,29,0,0,
        41,40,1,0,0,0,41,42,1,0,0,0,42,3,1,0,0,0,43,44,5,4,0,0,44,45,5,5,
        0,0,45,50,5,27,0,0,46,47,5,6,0,0,47,49,5,27,0,0,48,46,1,0,0,0,49,
        52,1,0,0,0,50,48,1,0,0,0,50,51,1,0,0,0,51,53,1,0,0,0,52,50,1,0,0,
        0,53,54,5,29,0,0,54,5,1,0,0,0,55,56,5,7,0,0,56,57,5,2,0,0,57,61,
        5,29,0,0,58,60,3,8,4,0,59,58,1,0,0,0,60,63,1,0,0,0,61,59,1,0,0,0,
        61,62,1,0,0,0,62,64,1,0,0,0,63,61,1,0,0,0,64,66,5,3,0,0,65,67,5,
        29,0,0,66,65,1,0,0,0,66,67,1,0,0,0,67,7,1,0,0,0,68,75,3,10,5,0,69,
        75,3,12,6,0,70,75,3,14,7,0,71,75,3,18,9,0,72,75,3,20,10,0,73,75,
        5,29,0,0,74,68,1,0,0,0,74,69,1,0,0,0,74,70,1,0,0,0,74,71,1,0,0,0,
        74,72,1,0,0,0,74,73,1,0,0,0,75,9,1,0,0,0,76,77,5,27,0,0,77,78,5,
        8,0,0,78,79,3,22,11,0,79,80,5,29,0,0,80,11,1,0,0,0,81,82,5,9,0,0,
        82,83,5,10,0,0,83,84,5,27,0,0,84,85,5,11,0,0,85,86,5,29,0,0,86,13,
        1,0,0,0,87,88,5,12,0,0,88,89,5,10,0,0,89,94,3,16,8,0,90,91,5,6,0,
        0,91,93,3,16,8,0,92,90,1,0,0,0,93,96,1,0,0,0,94,92,1,0,0,0,94,95,
        1,0,0,0,95,97,1,0,0,0,96,94,1,0,0,0,97,98,5,11,0,0,98,99,5,29,0,
        0,99,15,1,0,0,0,100,103,5,26,0,0,101,103,3,22,11,0,102,100,1,0,0,
        0,102,101,1,0,0,0,103,17,1,0,0,0,104,105,5,13,0,0,105,106,5,10,0,
        0,106,107,3,24,12,0,107,108,5,11,0,0,108,109,5,2,0,0,109,113,5,29,
        0,0,110,112,3,8,4,0,111,110,1,0,0,0,112,115,1,0,0,0,113,111,1,0,
        0,0,113,114,1,0,0,0,114,116,1,0,0,0,115,113,1,0,0,0,116,127,5,3,
        0,0,117,118,5,14,0,0,118,119,5,2,0,0,119,123,5,29,0,0,120,122,3,
        8,4,0,121,120,1,0,0,0,122,125,1,0,0,0,123,121,1,0,0,0,123,124,1,
        0,0,0,124,126,1,0,0,0,125,123,1,0,0,0,126,128,5,3,0,0,127,117,1,
        0,0,0,127,128,1,0,0,0,128,130,1,0,0,0,129,131,5,29,0,0,130,129,1,
        0,0,0,130,131,1,0,0,0,131,19,1,0,0,0,132,133,5,15,0,0,133,134,5,
        10,0,0,134,135,3,24,12,0,135,136,5,11,0,0,136,137,5,2,0,0,137,141,
        5,29,0,0,138,140,3,8,4,0,139,138,1,0,0,0,140,143,1,0,0,0,141,139,
        1,0,0,0,141,142,1,0,0,0,142,144,1,0,0,0,143,141,1,0,0,0,144,146,
        5,3,0,0,145,147,5,29,0,0,146,145,1,0,0,0,146,147,1,0,0,0,147,21,
        1,0,0,0,148,149,6,11,-1,0,149,150,5,10,0,0,150,151,3,22,11,0,151,
        152,5,11,0,0,152,161,1,0,0,0,153,154,5,16,0,0,154,155,5,10,0,0,155,
        156,3,22,11,0,156,157,5,11,0,0,157,161,1,0,0,0,158,161,5,27,0,0,
        159,161,5,28,0,0,160,148,1,0,0,0,160,153,1,0,0,0,160,158,1,0,0,0,
        160,159,1,0,0,0,161,173,1,0,0,0,162,163,10,5,0,0,163,164,5,17,0,
        0,164,172,3,22,11,6,165,166,10,4,0,0,166,167,7,0,0,0,167,172,3,22,
        11,5,168,169,10,3,0,0,169,170,7,1,0,0,170,172,3,22,11,4,171,162,
        1,0,0,0,171,165,1,0,0,0,171,168,1,0,0,0,172,175,1,0,0,0,173,171,
        1,0,0,0,173,174,1,0,0,0,174,23,1,0,0,0,175,173,1,0,0,0,176,177,6,
        12,-1,0,177,178,5,10,0,0,178,179,3,24,12,0,179,180,5,11,0,0,180,
        188,1,0,0,0,181,182,5,22,0,0,182,188,3,24,12,4,183,184,3,22,11,0,
        184,185,5,25,0,0,185,186,3,22,11,0,186,188,1,0,0,0,187,176,1,0,0,
        0,187,181,1,0,0,0,187,183,1,0,0,0,188,197,1,0,0,0,189,190,10,2,0,
        0,190,191,5,23,0,0,191,196,3,24,12,3,192,193,10,1,0,0,193,194,5,
        24,0,0,194,196,3,24,12,2,195,189,1,0,0,0,195,192,1,0,0,0,196,199,
        1,0,0,0,197,195,1,0,0,0,197,198,1,0,0,0,198,25,1,0,0,0,199,197,1,
        0,0,0,20,36,41,50,61,66,74,94,102,113,123,127,130,141,146,160,171,
        173,187,195,197
    ]

class MiLenguajeParser ( Parser ):

    grammarFileName = "MiLenguaje.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'loadout'", "'{'", "'}'", "'real'", "':'", 
                     "','", "'spawn'", "'='", "'loot'", "'('", "')'", "'drop'", 
                     "'peek'", "'fallback'", "'rush'", "'raiz'", "'^'", 
                     "'*'", "'/'", "'+'", "'-'", "'no'", "'y'", "'o'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "OP_REL", "CADENA", "ID", "NUMERO_REAL", 
                      "NL", "WS", "COMENTARIO" ]

    RULE_programa = 0
    RULE_declaracion_vars = 1
    RULE_declaracion = 2
    RULE_cuerpo_principal = 3
    RULE_sentencia = 4
    RULE_asignacion = 5
    RULE_lectura = 6
    RULE_escritura = 7
    RULE_expr_escritura = 8
    RULE_condicional = 9
    RULE_repetitiva = 10
    RULE_expr = 11
    RULE_condicion = 12

    ruleNames =  [ "programa", "declaracion_vars", "declaracion", "cuerpo_principal", 
                   "sentencia", "asignacion", "lectura", "escritura", "expr_escritura", 
                   "condicional", "repetitiva", "expr", "condicion" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    OP_REL=25
    CADENA=26
    ID=27
    NUMERO_REAL=28
    NL=29
    WS=30
    COMENTARIO=31

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracion_vars(self):
            return self.getTypedRuleContext(MiLenguajeParser.Declaracion_varsContext,0)


        def cuerpo_principal(self):
            return self.getTypedRuleContext(MiLenguajeParser.Cuerpo_principalContext,0)


        def EOF(self):
            return self.getToken(MiLenguajeParser.EOF, 0)

        def getRuleIndex(self):
            return MiLenguajeParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = MiLenguajeParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.declaracion_vars()
            self.state = 27
            self.cuerpo_principal()
            self.state = 28
            self.match(MiLenguajeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaracion_varsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(MiLenguajeParser.NL)
            else:
                return self.getToken(MiLenguajeParser.NL, i)

        def declaracion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiLenguajeParser.DeclaracionContext)
            else:
                return self.getTypedRuleContext(MiLenguajeParser.DeclaracionContext,i)


        def getRuleIndex(self):
            return MiLenguajeParser.RULE_declaracion_vars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion_vars" ):
                listener.enterDeclaracion_vars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion_vars" ):
                listener.exitDeclaracion_vars(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion_vars" ):
                return visitor.visitDeclaracion_vars(self)
            else:
                return visitor.visitChildren(self)




    def declaracion_vars(self):

        localctx = MiLenguajeParser.Declaracion_varsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaracion_vars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(MiLenguajeParser.T__0)
            self.state = 31
            self.match(MiLenguajeParser.T__1)
            self.state = 32
            self.match(MiLenguajeParser.NL)
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 33
                self.declaracion()
                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 39
            self.match(MiLenguajeParser.T__2)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 40
                self.match(MiLenguajeParser.NL)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiLenguajeParser.ID)
            else:
                return self.getToken(MiLenguajeParser.ID, i)

        def NL(self):
            return self.getToken(MiLenguajeParser.NL, 0)

        def getRuleIndex(self):
            return MiLenguajeParser.RULE_declaracion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion" ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion" ):
                listener.exitDeclaracion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion" ):
                return visitor.visitDeclaracion(self)
            else:
                return visitor.visitChildren(self)




    def declaracion(self):

        localctx = MiLenguajeParser.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaracion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(MiLenguajeParser.T__3)
            self.state = 44
            self.match(MiLenguajeParser.T__4)
            self.state = 45
            self.match(MiLenguajeParser.ID)
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 46
                self.match(MiLenguajeParser.T__5)
                self.state = 47
                self.match(MiLenguajeParser.ID)
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 53
            self.match(MiLenguajeParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cuerpo_principalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(MiLenguajeParser.NL)
            else:
                return self.getToken(MiLenguajeParser.NL, i)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiLenguajeParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(MiLenguajeParser.SentenciaContext,i)


        def getRuleIndex(self):
            return MiLenguajeParser.RULE_cuerpo_principal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCuerpo_principal" ):
                listener.enterCuerpo_principal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCuerpo_principal" ):
                listener.exitCuerpo_principal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCuerpo_principal" ):
                return visitor.visitCuerpo_principal(self)
            else:
                return visitor.visitChildren(self)




    def cuerpo_principal(self):

        localctx = MiLenguajeParser.Cuerpo_principalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_cuerpo_principal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(MiLenguajeParser.T__6)
            self.state = 56
            self.match(MiLenguajeParser.T__1)
            self.state = 57
            self.match(MiLenguajeParser.NL)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 671134208) != 0):
                self.state = 58
                self.sentencia()
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 64
            self.match(MiLenguajeParser.T__2)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 65
                self.match(MiLenguajeParser.NL)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacion(self):
            return self.getTypedRuleContext(MiLenguajeParser.AsignacionContext,0)


        def lectura(self):
            return self.getTypedRuleContext(MiLenguajeParser.LecturaContext,0)


        def escritura(self):
            return self.getTypedRuleContext(MiLenguajeParser.EscrituraContext,0)


        def condicional(self):
            return self.getTypedRuleContext(MiLenguajeParser.CondicionalContext,0)


        def repetitiva(self):
            return self.getTypedRuleContext(MiLenguajeParser.RepetitivaContext,0)


        def NL(self):
            return self.getToken(MiLenguajeParser.NL, 0)

        def getRuleIndex(self):
            return MiLenguajeParser.RULE_sentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia" ):
                listener.enterSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia" ):
                listener.exitSentencia(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia" ):
                return visitor.visitSentencia(self)
            else:
                return visitor.visitChildren(self)




    def sentencia(self):

        localctx = MiLenguajeParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_sentencia)
        try:
            self.state = 74
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.asignacion()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.lectura()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 70
                self.escritura()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 71
                self.condicional()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 5)
                self.state = 72
                self.repetitiva()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 6)
                self.state = 73
                self.match(MiLenguajeParser.NL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiLenguajeParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(MiLenguajeParser.ExprContext,0)


        def NL(self):
            return self.getToken(MiLenguajeParser.NL, 0)

        def getRuleIndex(self):
            return MiLenguajeParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = MiLenguajeParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(MiLenguajeParser.ID)
            self.state = 77
            self.match(MiLenguajeParser.T__7)
            self.state = 78
            self.expr(0)
            self.state = 79
            self.match(MiLenguajeParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LecturaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiLenguajeParser.ID, 0)

        def NL(self):
            return self.getToken(MiLenguajeParser.NL, 0)

        def getRuleIndex(self):
            return MiLenguajeParser.RULE_lectura

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLectura" ):
                listener.enterLectura(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLectura" ):
                listener.exitLectura(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLectura" ):
                return visitor.visitLectura(self)
            else:
                return visitor.visitChildren(self)




    def lectura(self):

        localctx = MiLenguajeParser.LecturaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_lectura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(MiLenguajeParser.T__8)
            self.state = 82
            self.match(MiLenguajeParser.T__9)
            self.state = 83
            self.match(MiLenguajeParser.ID)
            self.state = 84
            self.match(MiLenguajeParser.T__10)
            self.state = 85
            self.match(MiLenguajeParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EscrituraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_escritura(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiLenguajeParser.Expr_escrituraContext)
            else:
                return self.getTypedRuleContext(MiLenguajeParser.Expr_escrituraContext,i)


        def NL(self):
            return self.getToken(MiLenguajeParser.NL, 0)

        def getRuleIndex(self):
            return MiLenguajeParser.RULE_escritura

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEscritura" ):
                listener.enterEscritura(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEscritura" ):
                listener.exitEscritura(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEscritura" ):
                return visitor.visitEscritura(self)
            else:
                return visitor.visitChildren(self)




    def escritura(self):

        localctx = MiLenguajeParser.EscrituraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_escritura)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(MiLenguajeParser.T__11)
            self.state = 88
            self.match(MiLenguajeParser.T__9)
            self.state = 89
            self.expr_escritura()
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 90
                self.match(MiLenguajeParser.T__5)
                self.state = 91
                self.expr_escritura()
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 97
            self.match(MiLenguajeParser.T__10)
            self.state = 98
            self.match(MiLenguajeParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_escrituraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CADENA(self):
            return self.getToken(MiLenguajeParser.CADENA, 0)

        def expr(self):
            return self.getTypedRuleContext(MiLenguajeParser.ExprContext,0)


        def getRuleIndex(self):
            return MiLenguajeParser.RULE_expr_escritura

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_escritura" ):
                listener.enterExpr_escritura(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_escritura" ):
                listener.exitExpr_escritura(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_escritura" ):
                return visitor.visitExpr_escritura(self)
            else:
                return visitor.visitChildren(self)




    def expr_escritura(self):

        localctx = MiLenguajeParser.Expr_escrituraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_expr_escritura)
        try:
            self.state = 102
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 100
                self.match(MiLenguajeParser.CADENA)
                pass
            elif token in [10, 16, 27, 28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 101
                self.expr(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condicion(self):
            return self.getTypedRuleContext(MiLenguajeParser.CondicionContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(MiLenguajeParser.NL)
            else:
                return self.getToken(MiLenguajeParser.NL, i)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiLenguajeParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(MiLenguajeParser.SentenciaContext,i)


        def getRuleIndex(self):
            return MiLenguajeParser.RULE_condicional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicional" ):
                listener.enterCondicional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicional" ):
                listener.exitCondicional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicional" ):
                return visitor.visitCondicional(self)
            else:
                return visitor.visitChildren(self)




    def condicional(self):

        localctx = MiLenguajeParser.CondicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_condicional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(MiLenguajeParser.T__12)
            self.state = 105
            self.match(MiLenguajeParser.T__9)
            self.state = 106
            self.condicion(0)
            self.state = 107
            self.match(MiLenguajeParser.T__10)
            self.state = 108
            self.match(MiLenguajeParser.T__1)
            self.state = 109
            self.match(MiLenguajeParser.NL)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 671134208) != 0):
                self.state = 110
                self.sentencia()
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 116
            self.match(MiLenguajeParser.T__2)
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 117
                self.match(MiLenguajeParser.T__13)
                self.state = 118
                self.match(MiLenguajeParser.T__1)
                self.state = 119
                self.match(MiLenguajeParser.NL)
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 671134208) != 0):
                    self.state = 120
                    self.sentencia()
                    self.state = 125
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 126
                self.match(MiLenguajeParser.T__2)


            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 129
                self.match(MiLenguajeParser.NL)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RepetitivaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condicion(self):
            return self.getTypedRuleContext(MiLenguajeParser.CondicionContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(MiLenguajeParser.NL)
            else:
                return self.getToken(MiLenguajeParser.NL, i)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiLenguajeParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(MiLenguajeParser.SentenciaContext,i)


        def getRuleIndex(self):
            return MiLenguajeParser.RULE_repetitiva

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepetitiva" ):
                listener.enterRepetitiva(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepetitiva" ):
                listener.exitRepetitiva(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepetitiva" ):
                return visitor.visitRepetitiva(self)
            else:
                return visitor.visitChildren(self)




    def repetitiva(self):

        localctx = MiLenguajeParser.RepetitivaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_repetitiva)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(MiLenguajeParser.T__14)
            self.state = 133
            self.match(MiLenguajeParser.T__9)
            self.state = 134
            self.condicion(0)
            self.state = 135
            self.match(MiLenguajeParser.T__10)
            self.state = 136
            self.match(MiLenguajeParser.T__1)
            self.state = 137
            self.match(MiLenguajeParser.NL)
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 671134208) != 0):
                self.state = 138
                self.sentencia()
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 144
            self.match(MiLenguajeParser.T__2)
            self.state = 146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 145
                self.match(MiLenguajeParser.NL)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiLenguajeParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ExprSumaRestaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiLenguajeParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiLenguajeParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiLenguajeParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprSumaResta" ):
                listener.enterExprSumaResta(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprSumaResta" ):
                listener.exitExprSumaResta(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprSumaResta" ):
                return visitor.visitExprSumaResta(self)
            else:
                return visitor.visitChildren(self)


    class ExprPotenciaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiLenguajeParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiLenguajeParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiLenguajeParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprPotencia" ):
                listener.enterExprPotencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprPotencia" ):
                listener.exitExprPotencia(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprPotencia" ):
                return visitor.visitExprPotencia(self)
            else:
                return visitor.visitChildren(self)


    class ExprNumeroContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiLenguajeParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMERO_REAL(self):
            return self.getToken(MiLenguajeParser.NUMERO_REAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprNumero" ):
                listener.enterExprNumero(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprNumero" ):
                listener.exitExprNumero(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprNumero" ):
                return visitor.visitExprNumero(self)
            else:
                return visitor.visitChildren(self)


    class ExprParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiLenguajeParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MiLenguajeParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprParens" ):
                listener.enterExprParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprParens" ):
                listener.exitExprParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprParens" ):
                return visitor.visitExprParens(self)
            else:
                return visitor.visitChildren(self)


    class ExprMultDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiLenguajeParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiLenguajeParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiLenguajeParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprMultDiv" ):
                listener.enterExprMultDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprMultDiv" ):
                listener.exitExprMultDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprMultDiv" ):
                return visitor.visitExprMultDiv(self)
            else:
                return visitor.visitChildren(self)


    class ExprRaizContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiLenguajeParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MiLenguajeParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprRaiz" ):
                listener.enterExprRaiz(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprRaiz" ):
                listener.exitExprRaiz(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprRaiz" ):
                return visitor.visitExprRaiz(self)
            else:
                return visitor.visitChildren(self)


    class ExprIDContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiLenguajeParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiLenguajeParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprID" ):
                listener.enterExprID(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprID" ):
                listener.exitExprID(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprID" ):
                return visitor.visitExprID(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiLenguajeParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                localctx = MiLenguajeParser.ExprParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 149
                self.match(MiLenguajeParser.T__9)
                self.state = 150
                self.expr(0)
                self.state = 151
                self.match(MiLenguajeParser.T__10)
                pass
            elif token in [16]:
                localctx = MiLenguajeParser.ExprRaizContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 153
                self.match(MiLenguajeParser.T__15)
                self.state = 154
                self.match(MiLenguajeParser.T__9)
                self.state = 155
                self.expr(0)
                self.state = 156
                self.match(MiLenguajeParser.T__10)
                pass
            elif token in [27]:
                localctx = MiLenguajeParser.ExprIDContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 158
                self.match(MiLenguajeParser.ID)
                pass
            elif token in [28]:
                localctx = MiLenguajeParser.ExprNumeroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 159
                self.match(MiLenguajeParser.NUMERO_REAL)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 173
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 171
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        localctx = MiLenguajeParser.ExprPotenciaContext(self, MiLenguajeParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 162
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 163
                        self.match(MiLenguajeParser.T__16)
                        self.state = 164
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = MiLenguajeParser.ExprMultDivContext(self, MiLenguajeParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 165
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 166
                        _la = self._input.LA(1)
                        if not(_la==18 or _la==19):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 167
                        self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = MiLenguajeParser.ExprSumaRestaContext(self, MiLenguajeParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 168
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 169
                        _la = self._input.LA(1)
                        if not(_la==20 or _la==21):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 170
                        self.expr(4)
                        pass

             
                self.state = 175
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CondicionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiLenguajeParser.RULE_condicion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class CondOrContext(CondicionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiLenguajeParser.CondicionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def condicion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiLenguajeParser.CondicionContext)
            else:
                return self.getTypedRuleContext(MiLenguajeParser.CondicionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondOr" ):
                listener.enterCondOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondOr" ):
                listener.exitCondOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondOr" ):
                return visitor.visitCondOr(self)
            else:
                return visitor.visitChildren(self)


    class CondAndContext(CondicionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiLenguajeParser.CondicionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def condicion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiLenguajeParser.CondicionContext)
            else:
                return self.getTypedRuleContext(MiLenguajeParser.CondicionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondAnd" ):
                listener.enterCondAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondAnd" ):
                listener.exitCondAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondAnd" ):
                return visitor.visitCondAnd(self)
            else:
                return visitor.visitChildren(self)


    class CondNegacionContext(CondicionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiLenguajeParser.CondicionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def condicion(self):
            return self.getTypedRuleContext(MiLenguajeParser.CondicionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondNegacion" ):
                listener.enterCondNegacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondNegacion" ):
                listener.exitCondNegacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondNegacion" ):
                return visitor.visitCondNegacion(self)
            else:
                return visitor.visitChildren(self)


    class CondRelacionalContext(CondicionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiLenguajeParser.CondicionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiLenguajeParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiLenguajeParser.ExprContext,i)

        def OP_REL(self):
            return self.getToken(MiLenguajeParser.OP_REL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondRelacional" ):
                listener.enterCondRelacional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondRelacional" ):
                listener.exitCondRelacional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondRelacional" ):
                return visitor.visitCondRelacional(self)
            else:
                return visitor.visitChildren(self)


    class CondParensContext(CondicionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiLenguajeParser.CondicionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def condicion(self):
            return self.getTypedRuleContext(MiLenguajeParser.CondicionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondParens" ):
                listener.enterCondParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondParens" ):
                listener.exitCondParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondParens" ):
                return visitor.visitCondParens(self)
            else:
                return visitor.visitChildren(self)



    def condicion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiLenguajeParser.CondicionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_condicion, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                localctx = MiLenguajeParser.CondParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 177
                self.match(MiLenguajeParser.T__9)
                self.state = 178
                self.condicion(0)
                self.state = 179
                self.match(MiLenguajeParser.T__10)
                pass

            elif la_ == 2:
                localctx = MiLenguajeParser.CondNegacionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 181
                self.match(MiLenguajeParser.T__21)
                self.state = 182
                self.condicion(4)
                pass

            elif la_ == 3:
                localctx = MiLenguajeParser.CondRelacionalContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 183
                self.expr(0)
                self.state = 184
                self.match(MiLenguajeParser.OP_REL)
                self.state = 185
                self.expr(0)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 197
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 195
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                    if la_ == 1:
                        localctx = MiLenguajeParser.CondAndContext(self, MiLenguajeParser.CondicionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_condicion)
                        self.state = 189
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 190
                        self.match(MiLenguajeParser.T__22)
                        self.state = 191
                        self.condicion(3)
                        pass

                    elif la_ == 2:
                        localctx = MiLenguajeParser.CondOrContext(self, MiLenguajeParser.CondicionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_condicion)
                        self.state = 192
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 193
                        self.match(MiLenguajeParser.T__23)
                        self.state = 194
                        self.condicion(2)
                        pass

             
                self.state = 199
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[11] = self.expr_sempred
        self._predicates[12] = self.condicion_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

    def condicion_sempred(self, localctx:CondicionContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 1)
         




