import tkinter as tk
from tkinter import filedialog
from analizador_sintactico import parser

def cargar_archivo():
    filepath = filedialog.askopenfilename(filetypes=[("Ruby Files", "*.rb")])
    if filepath:
        with open(filepath, "r") as f:
            data = f.read()
            result = parser.parse(data)
            resultado.set("Análisis completado sin errores." if result else "Errores detectados. Revisa los logs.")

app = tk.Tk()
app.title("Analizador de Código Ruby")

resultado = tk.StringVar()
resultado.set("Cargue un archivo para analizar.")

tk.Label(app, text="Analizador de Código Ruby").pack()
tk.Button(app, text="Cargar archivo", command=cargar_archivo).pack()
tk.Label(app, textvariable=resultado).pack()

app.mainloop()
