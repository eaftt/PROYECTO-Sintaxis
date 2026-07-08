from antlr4 import *
from MiLenguajeLexer import MiLenguajeLexer
from MiLenguajeParser import MiLenguajeParser

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

if __name__ == '__main__':
    probar_archivo('nombre.txt') # cambiar nombre por alguno de los archivos txt para probar