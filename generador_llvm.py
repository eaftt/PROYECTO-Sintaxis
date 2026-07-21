from ast_nodos import *

class GeneradorLLVM:
    def __init__(self):
        self.codigo = []
        self.contador_registros = 1
        self.contador_etiquetas = 1
        self.variables_declaradas = set()
        self.strings_constantes = {}
        self.contador_strings = 1

    def nuevo_registro(self):
        reg = f"%{self.contador_registros}"
        self.contador_registros += 1
        return reg

    def nueva_etiqueta(self, prefijo):
        etiq = f"{prefijo}_{self.contador_etiquetas}"
        self.contador_etiquetas += 1
        return etiq

    def _obtener_o_crear_string(self, texto):
        texto_limpio = texto.strip('"\'')
        if texto_limpio in self.strings_constantes:
            return self.strings_constantes[texto_limpio]
        
        nombre_var = f"@.str.{self.contador_strings}"
        self.contador_strings += 1
        
        texto_escapado = texto_limpio + "\\0A\\00"
        bytes_len = len(texto_limpio) + 2
        
        linea_decl = f'{nombre_var} = private unnamed_addr constant [{bytes_len} x i8] c"{texto_escapado}"'
        self.strings_constantes[texto_limpio] = (nombre_var, bytes_len, linea_decl)
        return nombre_var, bytes_len, linea_decl

    def _agregar_br_si_falta(self, etiqueta_destino):
        if self.codigo and not self.codigo[-1].strip().startswith("br "):
            self.codigo.append(f"br label %{etiqueta_destino}")

    def generar(self, nodo_raiz):
        self.codigo.append('declare i32 @system(i8*)')
        self.codigo.append('declare double @llvm.pow.f64(double, double)')
        self.codigo.append('declare i32 @printf(i8*, ...)')
        self.codigo.append('declare i32 @scanf(i8*, ...)')
        self.codigo.append('declare double @llvm.sqrt.f64(double)')
        self.codigo.append('@str_format = private unnamed_addr constant [4 x i8] c"%f\\0A\\00"')
        self.codigo.append('@scan_format = private unnamed_addr constant [4 x i8] c"%lf\\00"')
        self.codigo.append('@pause_cmd = private unnamed_addr constant [6 x i8] c"pause\\00"')

        cuerpo_temp = []
        codigo_original = self.codigo
        self.codigo = cuerpo_temp        
        
        for sentencia in nodo_raiz.sentencias:
            self.visitar(sentencia)                        

        self.codigo = codigo_original
        for _, _, decl in self.strings_constantes.values():
            self.codigo.append(decl)

        self.codigo.append('define i32 @main() {')
        self.codigo.append('entry:')        
        for var in self.variables_declaradas:
            self.codigo.append(f"%{var} = alloca double")                      
            
        self.codigo.extend(cuerpo_temp)    

        reg_ptr_pause = self.nuevo_registro()
        self.codigo.append(f"{reg_ptr_pause} = getelementptr inbounds [6 x i8], [6 x i8]* @pause_cmd, i32 0, i32 0")
        reg_sys = self.nuevo_registro()
        self.codigo.append(f"{reg_sys} = call i32 @system(i8* {reg_ptr_pause})")

        self._agregar_br_si_falta("end_main")
        self.codigo.append('end_main:')
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
            elif nodo.operador == '^':
                self.codigo.append(f"{reg_res} = call double @llvm.pow.f64(double {reg_izq}, double {reg_der})")
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
            if hasattr(nodo, 'cadena_texto') and nodo.cadena_texto:
                for texto in nodo.cadena_texto:
                    nombre_var, bytes_len, _ = self._obtener_o_crear_string(texto)
                    reg_ptr = self.nuevo_registro()
                    self.codigo.append(f"{reg_ptr} = getelementptr inbounds [{bytes_len} x i8], [{bytes_len} x i8]* {nombre_var}, i32 0, i32 0")
                    reg_call = self.nuevo_registro()
                    self.codigo.append(f"{reg_call} = call i32 (i8*, ...) @printf(i8* {reg_ptr})")

            if hasattr(nodo, 'expresiones') and nodo.expresiones:
                for exp in nodo.expresiones:
                    reg_val = self.visitar(exp)
                    reg_ptr = self.nuevo_registro()
                    self.codigo.append(f"{reg_ptr} = getelementptr inbounds [4 x i8], [4 x i8]* @str_format, i32 0, i32 0")
                    reg_call = self.nuevo_registro()
                    self.codigo.append(f"{reg_call} = call i32 (i8*, ...) @printf(i8* {reg_ptr}, double {reg_val})")

        elif isinstance(nodo, Entrada): 
            self.variables_declaradas.add(nodo.id_nombre)
            reg_ptr = self.nuevo_registro()
            self.codigo.append(f"{reg_ptr} = getelementptr inbounds [4 x i8], [4 x i8]* @scan_format, i32 0, i32 0")
            reg_call = self.nuevo_registro()
            self.codigo.append(f"{reg_call} = call i32 (i8*, ...) @scanf(i8* {reg_ptr}, double* %{nodo.id_nombre})")

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
            self._agregar_br_si_falta(label_end)
            
            self.codigo.append(f"{label_false}:")
            if nodo.sentencia_falso:
                if isinstance(nodo.sentencia_falso, list):
                    for s in nodo.sentencia_falso:
                        self.visitar(s)
                else:
                    self.visitar(nodo.sentencia_falso)
            self._agregar_br_si_falta(label_end)
            
            self.codigo.append(f"{label_end}:")

        elif isinstance(nodo, Ciclo):
            label_cond = self.nueva_etiqueta("loop_cond")
            label_body = self.nueva_etiqueta("loop_body")
            label_end = self.nueva_etiqueta("loop_end")
            
            self._agregar_br_si_falta(label_cond)
            self.codigo.append(f"{label_cond}:")
            
            reg_cond = self.visitar(nodo.condicion)
            self.codigo.append(f"br i1 {reg_cond}, label %{label_body}, label %{label_end}")
            
            self.codigo.append(f"{label_body}:")
            if isinstance(nodo.sentencias, list):
                for s in nodo.sentencias:
                    self.visitar(s)
            else:
                self.visitar(nodo.sentencias)
            self._agregar_br_si_falta(label_cond)
            
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
