grammar MiLenguaje;

//Reglas sintacticas 

programa: declaracion_vars cuerpo_principal EOF ; 

//Declaracion de variables
declaracion_vars: 'loadout' '{' NL declaracion* '}' NL? ;
declaracion: 'real' ':' ID (',' ID)* NL ;

//Cuerpo Principal
cuerpo_principal: 'spawn' '{' NL sentencia* '}' NL? ;

//Tipos de Sentencia
sentencia
    : asignacion
    | lectura
    | escritura
    | condicional
    | repetitiva
    | NL 
    ; 

asignacion: ID '=' expr NL; 
lectura: 'loot' '(' ID ')' NL ;
escritura: 'drop' '(' expr_escritura (',' expr_escritura)* ')' NL ; 

expr_escritura
    : CADENA 
    | expr
    ; 

condicional 
    : 'peek' '(' condicion ')' '{' NL sentencia* '}' ('fallback' '{' NL sentencia* '}')? NL? ; 

repetitiva
    : 'rush' '(' condicion ')' '{' NL sentencia* '}' NL? ; 

//Expresiones aritmeticas
expr
    : '(' expr ')'              # ExprParens 
    | 'raiz' '(' expr ')'       # ExprRaiz
    | expr '^' expr             # ExprPotencia
    | expr ('*' | '/') expr     # ExprMultDiv
    | expr ('+' | '-') expr     # ExprSumaResta
    | ID                        # ExprID
    | NUMERO_REAL               # ExprNumero
    ; 

//Condiciones Logicas y Relacionales
condicion
    : '(' condicion ')'         # CondParens
    | 'no' condicion            # CondNegacion
    | expr OP_REL expr          # CondRelacional
    | condicion 'y' condicion   # CondAnd
    | condicion 'o' condicion   # CondOr
    ;

//Reglas LEXICAS

OP_REL: '>' | '<' | '>=' | '<=' | '==' | '!=' ;
CADENA: '"' ~["]* '"' ;
ID:  [a-zA-Z] [a-zA-Z0-9]*; 
NUMERO_REAL: [0-9]+ '.' [0-9]+ ; 

NL: ('\r'? '\n')+ ; 
WS : [ \t]+ -> skip ; 
COMENTARIO : '//' ~[\r\n]* -> skip; 