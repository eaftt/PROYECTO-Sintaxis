from antlr4 import *
from MiLenguajeLexer import MiLenguajeLexer
from MiLenguajeParser import MiLenguajeParser
from visitor import ConstructorAST
from semantico import AnalizadorSemantico

def probar_archivo(nombre_archivo):
    print(f"--- Iniciando compilador para: {nombre_archivo} ---\n")
    
    input_stream = FileStream(nombre_archivo, encoding='utf-8')
    
    lexer = MiLenguajeLexer(input_stream)
    stream_tokens = CommonTokenStream(lexer)
    
    parser = MiLenguajeParser(stream_tokens)
    
    arbol = parser.programa()
    
    print("¡Análisis sintáctico terminado sin errores!")
    print("Árbol generado:")
    print(arbol.toStringTree(recog=parser))
    print("\n---------------------------------------------------\n")
    
    print("Construyendo el AST")
    visitor = ConstructorAST()
    ast = visitor.visit(arbol)

    print("\n===== DECLARACIONES =====")
    for d in ast.declaraciones:
        print(type(d).__name__, vars(d))

    print("\n===== SENTENCIAS =====")
    for s in ast.sentencias:
        print(type(s).__name__, vars(s))

    print("AST construido con exito")
    print("Sentencias encontradas:", len(ast.sentencias))

    print("\nIniciando análisis semántico...")

    analizador = AnalizadorSemantico()
    analizador.analizar(ast)

    print("Análisis semántico terminado sin errores.")


if __name__ == '__main__':
    probar_archivo('estadisticas.txt')
