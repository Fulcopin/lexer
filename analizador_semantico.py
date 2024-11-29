import os

# Diccionario para almacenar variables y sus tipos
variables = {}

# --- Funciones para el Análisis Semántico ---

def initialize_variable(var_name, value, var_type):
    """
    Inicializa una variable con su tipo y valor.
    """
    variables[var_name] = {"value": value, "type": var_type}

def check_variable_initialized(var_name, line):
    """
    Verifica que una variable haya sido inicializada antes de usarse.
    """
    if var_name not in variables:
        log_error(f"Semantic error: Variable '{var_name}' not initialized (line {line})")

def check_type_compatibility(op, left_type, right_type, line):
    """
    Verifica la compatibilidad de tipos en operaciones.
    """
    compatible_types = {
        "+": ["int", "float", "string"],
        "-": ["int", "float"],
        "*": ["int", "float"],
        "/": ["int", "float"],
    }

    if op in compatible_types:
        if left_type not in compatible_types[op] or right_type not in compatible_types[op]:
            log_error(
                f"Type error: Incompatible types '{left_type}' and '{right_type}' in operation '{op}' (line {line})"
            )

def check_return_type(expected_type, actual_type, line):
    """
    Verifica que el tipo de retorno de una función coincida con el esperado.
    """
    if expected_type != actual_type:
        log_error(
            f"Semantic error: Expected return type '{expected_type}', but got '{actual_type}' (line {line})"
        )

def check_break_usage(context, line):
    """
    Verifica que `break` solo se use dentro de un bucle.
    """
    if context != "loop":
        log_error(f"Semantic error: 'break' used outside of a loop (line {line})")

# --- Registro de Errores ---
def log_error(message):
    """
    Registra errores semánticos en un archivo de log.
    """
    if not os.path.exists("logs"):
        os.makedirs("logs")
    log_name = "logs/errores_semanticos.txt"
    with open(log_name, "a") as f:
        f.write(message + "\n")
    print(message)

def analizar_semantico(codigo_fuente):
    """
    Analiza semánticamente el código fuente y busca errores.
    """
    print("\n=== Análisis Semántico ===")

    # Simulación de análisis línea por línea
    lineas = codigo_fuente.splitlines()  # Separa el código por líneas
    for numero_linea, linea in enumerate(lineas, start=1):
        procesar_linea(linea, numero_linea)

def procesar_linea(linea, numero_linea):
    """
    Procesa cada línea del código fuente para detectar variables no inicializadas,
    operaciones incompatibles y otros errores semánticos.
    """
    # Eliminar espacios en blanco y comentarios
    linea = linea.strip()
    if not linea or linea.startswith("#"):  # Ignorar comentarios y líneas vacías
        return
# --- Ejemplo de Uso ---
if __name__ == "__main__":
    # Ejemplo de inicialización de variables
    initialize_variable("x", 5, "int")
    initialize_variable("y", 10.5, "float")

    # Simulaciones de validaciones
    check_variable_initialized("z", 10)  # Error: no inicializada
    check_type_compatibility("+", "int", "string", 15)  # Error: tipos incompatibles
    check_return_type("int", "float", 20)  # Error: tipo de retorno incorrecto
    check_break_usage("function", 25)  # Error: `break` fuera de un bucle
