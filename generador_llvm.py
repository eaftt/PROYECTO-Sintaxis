from ast_nodos import *

class GeneradorLLVM:
    def __init__(self):
        self.codigo = []
        self.contador_registros = 1
        self.contador_etiquetas = 1
        self.variables_declaradas = set()

    def nuevo_registro(self):
        reg = f"%{self.contador_registros}"
        self.contador_registros += 1
        return reg

    def nueva_etiqueta(self, prefijo):
        etiq = f"{prefijo}_{self.contador_etiquetas}"
        self.contador_etiquetas += 1
        return etiq

    def generar(self, nodo_raiz):
        self.codigo.append('declare i32 @printf(i8*, ...)')
        self.codigo.append('declare double @llvm.sqrt.f64(double)')
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

        elif isinstance(nodo, Raiz):
            reg_val = self.visitar(nodo.expresion)
            reg_res = self.nuevo_registro()
            self.codigo.append(f"{reg_res} = call double @llvm.sqrt.f64(double {reg_val})")
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

        elif isinstance(nodo, Comparacion):
            reg_izq = self.visitar(nodo.izquierda)
            reg_der = self.visitar(nodo.derecha)
            reg_bool = self.nuevo_registro()
            mapa_ops = {'<': 'olt', '>': 'ogt', '<=': 'ole', '>=': 'oge', '==': 'oeq', '!=': 'one'}
            op_llvm = mapa_ops.get(nodo.operador, 'oeq')    
            self.codigo.append(f"{reg_bool} = fcmp {op_llvm} double {reg_izq}, {reg_der}")
            return reg_bool

        elif isinstance(nodo, Condicional):
            label_true = self.nueva_etiqueta("if_true")
            label_false = self.nueva_etiqueta("if_false")
            label_end = self.nueva_etiqueta("if_end")
            reg_cond = self.visitar(nodo.condicion)
            self.codigo.append(f"br i1 {reg_cond}, label %{label_true}, label %{label_false}")
            self.codigo.append(f"{label_true}:")
            if isinstance(nodo.sentencia_verdadero, list):
                for s in nodo.sentencia_verdadero:
                    self.visitar(s)
            else:
                self.visitar(nodo.sentencia_verdadero)
            self.codigo.append(f"br label %{label_end}")
            self.codigo.append(f"{label_false}:")
            if nodo.sentencia_falso:
                if isinstance(nodo.sentencia_falso, list):
                    for s in nodo.sentencia_falso:
                        self.visitar(s)
                else:
                    self.visitar(nodo.sentencia_falso)
            self.codigo.append(f"br label %{label_end}")
            self.codigo.append(f"{label_end}:")

        elif isinstance(nodo, Ciclo):
            label_cond = self.nueva_etiqueta("loop_cond")
            label_body = self.nueva_etiqueta("loop_body")
            label_end = self.nueva_etiqueta("loop_end")
            self.codigo.append(f"br label %{label_cond}")
            self.codigo.append(f"{label_cond}:")
            reg_cond = self.visitar(nodo.condicion)
            self.codigo.append(f"br i1 {reg_cond}, label %{label_body}, label %{label_end}")
            self.codigo.append(f"{label_body}:")
            if isinstance(nodo.sentencias, list):
                for s in nodo.sentencias:
                    self.visitar(s)
            else:
                self.visitar(nodo.sentencias)
            self.codigo.append(f"br label %{label_cond}")
            self.codigo.append(f"{label_end}:")

        elif isinstance(nodo, Negacion):
            reg_cond = self.visitar(nodo.condicion)
            reg_res = self.nuevo_registro()
            self.codigo.append(f"{reg_res} = xor i1 {reg_cond}, true")
            return reg_res

        elif isinstance(nodo, And):
            reg_izq = self.visitar(nodo.izquierda)
            reg_der = self.visitar(nodo.derecha)
            reg_res = self.nuevo_registro()
            self.codigo.append(f"{reg_res} = and i1 {reg_izq}, {reg_der}")
            return reg_res

        elif isinstance(nodo, Or):
            reg_izq = self.visitar(nodo.izquierda)
            reg_der = self.visitar(nodo.derecha)
            reg_res = self.nuevo_registro()
            self.codigo.append(f"{reg_res} = or i1 {reg_izq}, {reg_der}")
            return reg_res
