import ply.yacc as yacc
from analizador_lexico import tokens
import os
import datetime

# --- Reglas Sintácticas ---
def p_program(p):
    '''program : statement_list'''
    p[0] = p[1]  # Retorna la lista de declaraciones

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 3:  # Si hay múltiples declaraciones
        p[0] = p[1] + [p[2]]
    else:  # Una única declaración
        p[0] = [p[1]]

def p_statement(p):
    '''statement : variable_declaration
                 | print_statement
                 | control_structure
                 | array_declaration
                 | hash_declaration
                 | input_statement'''
    p[0] = p[1]  # Retorna el nodo correspondiente

# Solicitud de datos por teclado
def p_input_statement(p):
    '''input_statement : ID ASSIGN GETS'''
    p[0] = ('input', p[1])  # Representación: input(variable)

# Declaración de variables
def p_variable_declaration(p):
    '''variable_declaration : ID ASSIGN expression'''
    p[0] = ('assign', p[1], p[3])  # Representación: asignación

# Impresión
def p_print_statement(p):
    '''print_statement : PUTS LPAREN argument_list RPAREN
                       | PUTS LPAREN RPAREN
                       | PUTS STRING
                       | PUTS'''
    if len(p) == 5:  # `puts(argument_list)`
        p[0] = ('print', p[3])
    elif len(p) == 4:  # `puts()`
        p[0] = ('print', None)
    elif len(p) == 3:  # `puts "string"`
        p[0] = ('print', p[2])
    else:  # `puts`
        p[0] = ('print', None)

def p_argument_list(p):
    '''argument_list : argument_list COMMA expression
                     | expression'''
    if len(p) == 4:  # Lista con múltiples expresiones
        p[0] = p[1] + [p[3]]
    else:  # Una sola expresión
        p[0] = [p[1]]

# Estructuras de control
def p_control_structure(p):
    '''control_structure : if_statement
                         | while_statement'''
    p[0] = p[1]

def p_if_statement(p):
    '''if_statement : IF expression statement_list END'''
    p[0] = ('if', p[2], p[3])  # Representación: if(condición, cuerpo)

def p_while_statement(p):
    '''while_statement : WHILE expression statement_list END'''
    p[0] = ('while', p[2], p[3])  # Representación: while(condición, cuerpo)

# Expresiones
def p_expression(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | NUMBER
                  | STRING
                  | ID'''
    if len(p) == 4: 
        p[0] = (p[2], p[1], p[3])
    else:  # Valor único (literal o variable)
        p[0] = p[1]

# Declaración de arrays
def p_array_declaration(p):
    '''array_declaration : ID ASSIGN LBRACKET array_elements RBRACKET
                         | ID ASSIGN LBRACKET RBRACKET'''
    if len(p) == 6:  # Array con elementos
        p[0] = ('array', p[1], p[4])
    else:  # Array vacío
        p[0] = ('array', p[1], [])

def p_array_elements(p):
    '''array_elements : array_elements COMMA expression
                      | expression'''
    if len(p) == 4:  # Múltiples elementos
        p[0] = p[1] + [p[3]]
    else:  # Un solo elemento
        p[0] = [p[1]]

# Declaración de hashes
def p_hash_declaration(p):
    '''hash_declaration : ID ASSIGN LBRACE hash_elements RBRACE
                        | ID ASSIGN LBRACE RBRACE'''
    if len(p) == 6:  # Hash con elementos
        p[0] = ('hash', p[1], p[4])
    else:  # Hash vacío
        p[0] = ('hash', p[1], {})

def p_hash_elements(p):
    '''hash_elements : hash_elements COMMA hash_pair
                     | hash_pair'''
    if len(p) == 4:  # Múltiples pares
        p[0] = {**p[1], **p[3]}
    else:  # Un solo par
        p[0] = p[1]

def p_hash_pair(p):
    '''hash_pair : expression COLON expression
                 | STRING COLON expression
                 | expression HASHROCKET expression'''
    if p[2] == ':':  # Representación estilo Ruby moderno
        p[0] = {p[1]: p[3]}
    else: 
        p[0] = {p[1]: p[3]}

# Producción vacía
def p_empty(p):
    '''empty :'''
    pass

# Manejo de errores
def p_error(p):
    if p:
        error_message = f"Error sintáctico en token '{p.value}' línea {p.lineno}"
        print(error_message)
        log_error(error_message)
    else:
        error_message = "Error sintáctico: fin de archivo inesperado"
        print(error_message)
        log_error(error_message)

# --- Registro de errores ---
def log_error(message):
    """Guarda los errores en un archivo de log."""
    if not os.path.exists("logs"):
        os.makedirs("logs")
    log_name = f'logs/sintactico-{datetime.datetime.now().strftime("%d%m%Y-%Hh%M")}.txt'
    with open(log_name, 'a') as log_file:
        log_file.write(message + '\n')

# Construcción del parser
parser = yacc.yacc()

def analizar_sintacticamente(codigo_fuente):
    print("\n=== Análisis Sintáctico ===")
    result = parser.parse(codigo_fuente)
    if result:
        print("Análisis sintáctico completado correctamente.")
    else:
        print("Se encontraron errores sintácticos.")
