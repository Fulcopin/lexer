import ply.lex as lex
import datetime
import os

# Fulco Pincay
tokens = (
    'ID', 'INSTANCE_VAR', 'CLASS_VAR', 'GLOBAL_VAR',  # Identificadores y variables
    'NUMBER', 'STRING',                               # Números y strings
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',               # Operadores aritméticos
    'AND', 'OR', 'NOT',                               # Operadores lógicos
    'EQ', 'NEQ', 'GT', 'LT', 'GTE', 'LTE',            # Comparadores
    'ASSIGN', 'PLUS_ASSIGN', 'MINUS_ASSIGN',          # Asignación
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',           # Delimitadores
    'COMMA', 'DOT', 'COLON', 'SEMICOLON',             # Otros
    'LBRACKET', 'RBRACKET', 'AMPERSAND',
    'MOD', 'EXP',                                     #Operadores de modulo y exponenciacion
     'TIMES_ASSIGN', 'DIVIDE_ASSIGN', 'MOD_ASSIGN',    # Más operadores de asignación
    'FLECHA'                                
)


reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'do': 'DO',
    'end': 'END',
    'def': 'DEF',
    'class': 'CLASS',
    'module': 'MODULE',
    'true': 'TRUE',
    'false': 'FALSE',
    'nil': 'NIL',
    'next': 'NEXT'
}


tokens += tuple(reserved.values())

# Fulco Pincay
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQ = r'=='
t_NEQ = r'!='
t_GT = r'>'
t_LT = r'<'
t_GTE = r'>='
t_LTE = r'<='
t_ASSIGN = r'='
t_PLUS_ASSIGN = r'\+='
t_MINUS_ASSIGN = r'-='
#Adrian Salamea \
t_TIMES_ASSIGN = r'\*='
t_DIVIDE_ASSIGN = r'\='
t_MOD_ASSIGN = r'\%='

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_DOT = r'\.'
t_COLON = r':'
t_SEMICOLON = r';'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'


t_AND = r'&&'
t_AMPERSAND = r'&'

#Adrian Salamea 
t_MOD = r'%'
t_EXP = r'\*\*'
t_FLECHA = r'=>'

# Fulco Pincay
def t_INSTANCE_VAR(t):
    r'@[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_CLASS_VAR(t):
    r'@@[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_GLOBAL_VAR(t):
    r'\$[a-zA-Z_][a-zA-Z_0-9]*'
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    return t


t_ignore = ' \t'


def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
#Adrian Salamea 
def t_COMMENT(t):
    r'\#.*'
    pass

lexer = lex.lex()


def generate_log(input_data, user_name):
    lexer.input(input_data)

    if not os.path.exists("logs"):
        os.makedirs("logs")

    log_name = f'logs/lexico-{user_name}-{datetime.datetime.now().strftime("%d%m%Y-%Hh%M")}.txt'
    with open(log_name, 'w') as log_file:
        while True:
            tok = lexer.token()
            if not tok:
                break
            log_file.write(f"{tok.type} - {tok.value} - Linea {tok.lineno} - Posicion {tok.lexpos}\n")

if __name__ == "__main__":
   
    print("Directorio actual:", os.getcwd())

   
    print("Archivos en el directorio especificado:", os.listdir("C:/Users/DETPC/OneDrive - Escuela Superior Politécnica del Litoral/LP/Proyectos/lexer"))

    try:
        with open("C:/Users/DETPC/OneDrive - Escuela Superior Politécnica del Litoral/LP/Proyectos/lexer/algoritmo2.rb", "r") as f:
            data = f.read()
            generate_log(data, "Adrianlsq2000")  
    except FileNotFoundError:
        print("Error: archivo de prueba 'algoritmo2.rb' no encontrado. Verifica la ruta.")
