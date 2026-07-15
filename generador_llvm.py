from ast_nodos import *

class GeneradorLLVM:
    def __init__(self):
        self.codigo = []
        self.contador_registros = 1
        self.variables_declaradas = set()

    def nuevo_registro(self):
        reg = f"%{self.contador_registros}"
        self.contador_registros += 1
        return reg

    def generar(self, nodo_raiz):
        self.codigo.append('declare i32 @printf(i8*, ...)')
        self.codigo.append('@str_format = private unnamed_addr constant [4 x i8] c"%f\\0A\\00"')
        self.codigo.append('define i32 @main() {')
        self.codigo.append('entry:')
        
        cuerpo_temp = []
        codigo_original = self.codigo
        self.codigo = cuerpo_temp
        
        for sentencia in nodo_raiz.sentencias:
            self.visitar(sentencia)
            
        self.codigo = codigo_original
        
        for var in self.variables_declaradas:
            self.codigo.append(f"%{var} = alloca double")
            
        self.codigo.extend(cuerpo_temp)
        
        self.codigo.append('ret i32 0')
        self.codigo.append('}')
        return "\n".join(self.codigo)

    def visitar(self, nodo):
        if isinstance(nodo, NumeroReal):
            reg = self.nuevo_registro()
            self.codigo.append(f"{reg} = fadd double 0.0, {nodo.valor}")
            return reg
            
        elif isinstance(nodo, VariableID):
            self.variables_declaradas.add(nodo.nombre)
            reg = self.nuevo_registro()
            self.codigo.append(f"{reg} = load double, double* %{nodo.nombre}")
            return reg
            
        elif isinstance(nodo, OperacionBinaria):
            reg_izq = self.visitar(nodo.izquierdo)
            reg_der = self.visitar(nodo.derecho)
            reg_res = self.nuevo_registro()
            
            if nodo.operador == '+':
                self.codigo.append(f"{reg_res} = fadd double {reg_izq}, {reg_der}")
            elif nodo.operador == '-':
                self.codigo.append(f"{reg_res} = fsub double {reg_izq}, {reg_der}")
            elif nodo.operador == '*':
                self.codigo.append(f"{reg_res} = fmul double {reg_izq}, {reg_der}")
            elif nodo.operador == '/':
                self.codigo.append(f"{reg_res} = fdiv double {reg_izq}, {reg_der}")
            return reg_res
            
        elif isinstance(nodo, Asignacion):
            self.variables_declaradas.add(nodo.id_nombre)
            reg_val = self.visitar(nodo.expresion)
            self.codigo.append(f"store double {reg_val}, double* %{nodo.id_nombre}")
            
        elif isinstance(nodo, Salida):
            for exp in nodo.expresiones:
                reg_val = self.visitar(exp)
                reg_ptr = self.nuevo_registro()
                self.codigo.append(f"{reg_ptr} = getelementptr inbounds [4 x i8], [4 x i8]* @str_format, i32 0, i32 0")
                reg_call = self.nuevo_registro()
                self.codigo.append(f"{reg_call} = call i32 (i8*, ...) @printf(i8* {reg_ptr}, double {reg_val})")