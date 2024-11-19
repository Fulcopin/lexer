import ply.yacc as yacc
from analizador_lexico import tokens
import os
import datetime

# --- Reglas Sintácticas ---
def p_program(p):
    '''program : statement_list'''
    pass

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    pass

def p_statement(p):
    '''statement : variable_declaration
                 | print_statement
                 | control_structure
                 | array_declaration
                 | hash_declaration
                 | input_statement'''
    pass
#Solicitud de datos por teclado
def p_input_statement(p):
    '''input_statement : ID ASSIGN GETS'''
    pass

def p_variable_declaration(p):
    '''variable_declaration : ID ASSIGN expression'''
    pass

def p_print_statement(p):
    '''print_statement : PUTS LPAREN argument_list RPAREN
                       | PUTS LPAREN RPAREN
                       | PUTS STRING
                       | PUTS'''
    pass

def p_argument_list(p):
    '''argument_list : argument_list COMMA expression
                     | expression'''
    pass

def p_control_structure(p):
    '''control_structure : if_statement
                         | while_statement'''
    pass

def p_if_statement(p):
    '''if_statement : IF expression statement_list END'''
    pass

def p_while_statement(p):
    '''while_statement : WHILE expression statement_list END'''
    pass

def p_expression(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | NUMBER
                  | STRING
                  | ID'''
    pass

# Reglas para arrays
def p_array_declaration(p):
    '''array_declaration : ID ASSIGN LBRACKET array_elements RBRACKET
                         | ID ASSIGN LBRACKET RBRACKET'''
    pass

def p_array_elements(p):
    '''array_elements : array_elements COMMA expression
                      | expression'''
    pass

# Reglas para hashes
def p_hash_declaration(p):
    '''hash_declaration : ID ASSIGN LBRACE hash_elements RBRACE
                        | ID ASSIGN LBRACE RBRACE'''
    pass

def p_hash_elements(p):
    '''hash_elements : hash_elements COMMA hash_pair
                     | hash_pair'''
    pass

def p_hash_pair(p):
    '''hash_pair : expression COLON expression
                 | STRING COLON expression
                 | expression HASHROCKET expression'''
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

# --- Log de Errores ---
def log_error(message):
    """Guarda los errores en un archivo de log."""
    if not os.path.exists("logs"):
        os.makedirs("logs")
    log_name = f'logs/sintactico-Fulcopin-{datetime.datetime.now().strftime("%d%m%Y-%Hh%M")}.txt'
    with open(log_name, 'a') as log_file:
        log_file.write(message + '\n')

# Construcción del parser
parser = yacc.yacc()

# --- Pruebas ---
if __name__ == "__main__":
    try:
        with open("algoritmo2.rb", "r") as f:
            data = f.read()
            parser.parse(data)
            print("Análisis sintáctico completado. Sin errores.")
    except FileNotFoundError:
        error_message = "Error: archivo de prueba 'algoritmo2.rb' no encontrado."
        print(error_message)
        log_error(error_message)
