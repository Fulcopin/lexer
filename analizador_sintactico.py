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
                 | control_structure'''
    pass

def p_variable_declaration(p):
    '''variable_declaration : ID ASSIGN expression'''
    pass

def p_print_statement(p):
    '''print_statement : PUTS LPAREN argument_list RPAREN
                       | PUTS STRING'''
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
