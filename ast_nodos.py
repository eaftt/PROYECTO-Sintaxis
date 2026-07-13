class ASTnodo: 
    pass

class programa(ASTnodo):
    def __init__(self, declaraciones, sentencias): 
        self.declaraciones = declaraciones
        self.sentencias = sentencias

class Asignacion(ASTnodo):
    def __init__(self, id_nombre, expresion):
        self.id_nombre = id_nombre
        self.expresion = expresion

class Entrada(ASTnodo): 
    def __init__(self, id_nombre):
        self.id_nombre = id_nombre

class Salida(ASTnodo):
    def __init__(self, cadena_texto, expresiones):
        self.cadena_texto = cadena_texto
        self.expresiones = expresiones

class Condicional(ASTnodo):
    def __init__(self, condicion, sentencia_verdadero, sentencia_falso=None):
        self.condicion = condicion
        self.sentencia_verdadero = sentencia_verdadero
        self.sentencia_falso = sentencia_falso 

class Ciclo(ASTnodo):
    def __init__(self, condicion, sentencias):
        self.condicion = condicion
        self.sentencias = sentencias

class OperacionBinaria(ASTnodo):
    def __init__(self, izquierdo, operador, derecho):
        self.izquierdo = izquierdo
        self.operador = operador
        self.derecho = derecho

class NumeroReal(ASTnodo):
    def __init__(self, valor):
        self.valor = float(valor)
    
class VariableID(ASTnodo): 
    def __init__(self, nombre):
        self.nombre = nombre



