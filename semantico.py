from ast_nodos import *

class ErrorSemantico(Exception):
    pass

class AnalizadorSemantico:

    def __init__(self):
        self.variables = set()

    def analizar(self, ast):
        self.visitar_programa(ast)

    def visitar_programa(self, nodo):
        for declaracion in nodo.declaraciones:
            self.visitar_declaracion(declaracion)
        for sentencia in nodo.sentencias:
            self.visitar_sentencia(sentencia)

    def visitar_declaracion(self, nodo):
        for variable in nodo.variables:
            if variable in self.variables:
                raise ErrorSemantico(
                    f"La variable '{variable}' ya fue declarada."
                )
            self.variables.add(variable)
    
    def visitar_sentencia(self, nodo):

        if isinstance(nodo, Asignacion):
            self.visitar_asignacion(nodo)
            print("Asignación encontrada:", nodo.id_nombre)
        elif isinstance(nodo, Entrada):
            self.visitar_entrada(nodo)

        elif isinstance(nodo, Salida):
            self.visitar_salida(nodo)

        elif isinstance(nodo, Condicional):
            self.visitar_condicional(nodo)

        elif isinstance(nodo, Ciclo):
            self.visitar_ciclo(nodo)

        
    def visitar_asignacion(self, nodo):

        if nodo.id_nombre not in self.variables:
            raise ErrorSemantico(
                f"La variable '{nodo.id_nombre}' no fue declarada."
            )

        self.visitar_expresion(nodo.expresion)

    def visitar_entrada(self, nodo):

        if nodo.id_nombre not in self.variables:
            raise ErrorSemantico(
                f"La variable '{nodo.id_nombre}' no fue declarada."
            )
        
    def visitar_salida(self, nodo):

        for expresion in nodo.expresiones:
            self.visitar_expresion(expresion)

    def visitar_condicional(self, nodo):

        self.visitar_condicion(nodo.condicion)

        for sentencia in nodo.sentencia_verdadero:
            self.visitar_sentencia(sentencia)

        if nodo.sentencia_falso is not None:
            for sentencia in nodo.sentencia_falso:
                self.visitar_sentencia(sentencia)

    def visitar_ciclo(self, nodo):

        self.visitar_condicion(nodo.condicion)

        for sentencia in nodo.sentencias:
            self.visitar_sentencia(sentencia)

    def visitar_condicion(self, nodo):

        if isinstance(nodo, Comparacion):
            self.visitar_expresion(nodo.izquierda)
            self.visitar_expresion(nodo.derecha)

        elif isinstance(nodo, Negacion):
            self.visitar_condicion(nodo.condicion)

        elif isinstance(nodo, And):
            self.visitar_condicion(nodo.izquierda)
            self.visitar_condicion(nodo.derecha)

        elif isinstance(nodo, Or):
            self.visitar_condicion(nodo.izquierda)
            self.visitar_condicion(nodo.derecha)

    def visitar_expresion(self, nodo):
        print(type(nodo).__name__)
        if isinstance(nodo, NumeroReal):
            return

        elif isinstance(nodo, VariableID):

            if nodo.nombre not in self.variables:
                raise ErrorSemantico(
                    f"La variable '{nodo.nombre}' no fue declarada."
                )

        elif isinstance(nodo, OperacionBinaria):

            self.visitar_expresion(nodo.izquierdo)
            self.visitar_expresion(nodo.derecho)

        elif isinstance(nodo, Raiz):

            self.visitar_expresion(nodo.expresion)
