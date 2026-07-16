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
    def __repr__(self):
        return f"({self.izquierdo} {self.operador} {self.derecho})"

class NumeroReal(ASTnodo):
    def __init__(self, valor):
        self.valor = float(valor)
    def __repr__(self):
        return f"NumeroReal({self.valor})"
    
class VariableID(ASTnodo): 
    def __init__(self, nombre):
        self.nombre = nombre
    def __repr__(self):
        return f"VariableID('{self.nombre}')"

class Declaracion(ASTnodo):
    def __init__(self, variables):
        self.variables = variables

class Comparacion(ASTnodo):
    def __init__(self, izquierda, operador, derecha):
        self.izquierda = izquierda
        self.operador = operador
        self.derecha = derecha
    def __repr__(self):
        return f"({self.izquierda} {self.operador} {self.derecha})"

class Negacion(ASTnodo):
    def __init__(self, condicion):
        self.condicion = condicion

class And(ASTnodo):
    def __init__(self, izquierda, derecha):
        self.izquierda = izquierda
        self.derecha = derecha

class Or(ASTnodo):
    def __init__(self, izquierda, derecha):
        self.izquierda = izquierda
        self.derecha = derecha

class Raiz(ASTnodo):
    def __init__(self, expresion):
        self.expresion = expresion




