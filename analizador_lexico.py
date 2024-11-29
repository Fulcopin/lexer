import ply.lex as lex

# --- Lista de tokens ---
tokens = (
    'ID', 'INSTANCE_VAR', 'CLASS_VAR', 'GLOBAL_VAR',  # Identificadores y variables
    'NUMBER', 'STRING',                               # Números y strings
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',               # Operadores aritméticos
    'EQ', 'NEQ', 'GT', 'LT', 'GTE', 'LTE',            # Comparadores
    'ASSIGN', 'PLUS_ASSIGN', 'MINUS_ASSIGN',          # Asignación
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',           # Delimitadores
    'COMMA', 'COLON',                                 # Otros delimitadores
    'LBRACKET', 'RBRACKET',                           # Más delimitadores
    'HASHROCKET',                                     # Para hashes
)

# Palabras reservadas
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'do': 'DO',
    'end': 'END',
    'puts': 'PUTS',
    'gets': 'GETS',
}

# Agregar palabras reservadas a tokens
tokens += tuple(reserved.values())

# --- Definición de reglas para los tokens ---
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
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r','
t_COLON = r':'
t_HASHROCKET = r'=>'

# Identificadores y palabras reservadas
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Verificar palabras reservadas
    return t

# Variables
def t_INSTANCE_VAR(t):
    r'@[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_CLASS_VAR(t):
    r'@@[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_GLOBAL_VAR(t):
    r'\$[a-zA-Z_][a-zA-Z_0-9]*'
    return t

# Números
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Strings
def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    return t

# Ignorar comentarios
def t_COMMENT(t):
    r'\#.*'
    pass

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Nueva línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

# Construcción del lexer
lexer = lex.lex()
def analizar_lexicamente(codigo_fuente):
    lexer.input(codigo_fuente)
    print("=== Análisis Léxico ===")
    while True:
        token = lexer.token()
        if not token:
            break
        print(f"Token: {token.type}, Valor: {token.value}, Línea: {token.lineno}")