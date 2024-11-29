import tkinter as tk
from tkinter import filedialog
from analizador_lexico import analizar_lexicamente
from analizador_sintactico import analizar_sintacticamente
from analizador_semantico import analizar_semantico

def cargar_archivo():
    filepath = filedialog.askopenfilename(filetypes=[("Ruby Files", "*.rb")])
    if filepath:
        with open(filepath, "r") as f:
            data = f.read()

            # Llamar a los analizadores
            analizar_lexicamente(data)  # Análisis léxico
            resultado_sintaxis = analizar_sintacticamente(data)  # Análisis sintáctico
            if resultado_sintaxis:
                # Si el análisis sintáctico es exitoso, realiza el análisis semántico
                analizar_semantico(data)

                # Mostrar los resultados del análisis semántico
                
            else:
                resultado.set("Errores sintácticos detectados. Revisa los logs.")
                mostrar_resultados.set("Errores sintácticos encontrados.")

app = tk.Tk()
app.title("Analizador de Código Ruby")

# Variables para mostrar resultados
resultado = tk.StringVar()
resultado.set("Cargue un archivo para analizar.")

# Caja de texto para mostrar los resultados del análisis semántico
mostrar_resultados = tk.StringVar()
mostrar_resultados.set("Esperando archivo...")

# Elementos de la interfaz
tk.Label(app, text="Analizador de Código Ruby").pack()
tk.Button(app, text="Cargar archivo", command=cargar_archivo).pack()
tk.Label(app, textvariable=resultado).pack()

# Caja de texto para mostrar los errores semánticos
tk.Label(app, text="Errores Semánticos:").pack()
text_resultados = tk.Text(app, height=10, width=50)
text_resultados.pack()

# Función para actualizar la caja de texto con los resultados
def actualizar_resultados():
    text_resultados.delete(1.0, tk.END)  # Limpiar el contenido
    text_resultados.insert(tk.END, mostrar_resultados.get())  # Insertar nuevos resultados

# Actualizar los resultados después de procesar el archivo
mostrar_resultados.trace("w", lambda *args: actualizar_resultados())

# Main loop de la interfaz gráfica
app.mainloop()
