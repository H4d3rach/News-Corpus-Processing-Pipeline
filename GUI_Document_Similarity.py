import tkinter as tk
from tkinter import filedialog
import Vector
import numpy as np

txt = None
def comparar():
    vecs = ["TF-IDF", "Frecuencia", "Binarizado"]
    ngrams = ["Unigrama", "Bigrama"]
    compares = ["Titulo", "Contenido", "Titulo+Contenido"]
    vectorizador_elegido = vecs.index(vectorizador.get())
    ngramas_elegido = ngrams.index(ngramas.get())
    comparacion_elegida = compares.index(comparacion.get())
    a = {"vectorizados": vectorizador_elegido, "ngramas": ngramas_elegido, "comparaciones": comparacion_elegida}
    values = Vector.compare_text(txt, a)
    print(values)
    Vector.list_comparations(values, a)
    # mensaje.config("Comparaciones: " + str(values))

def seleccionar_archivo():
    archivo = filedialog.askopenfilename(title="Seleccionar Archivo")
    if archivo:
        with open(archivo, 'r', encoding="utf-8") as file:
            global txt
            txt = file.read()
            print(txt)

# Crear ventana principal
root = tk.Tk()
root.title("Comparador de Textos")

# Contenedor principal para las secciones
contenedor_principal = tk.Frame(root)
contenedor_principal.pack()

# Sección de Vectorizador
frame_vectorizador = tk.Frame(contenedor_principal, padx=10, pady=10)
frame_vectorizador.pack(side=tk.LEFT)

tk.Label(frame_vectorizador, text="Vectorizador").grid(row=0, column=0, sticky=tk.W)
vectorizador = tk.StringVar()
vectorizador.set("TF-IDF")  # Valor predeterminado
for i, option in enumerate(["TF-IDF", "Frecuencia", "Binarizado"]):
    tk.Radiobutton(frame_vectorizador, text=option, variable=vectorizador, value=option).grid(row=i+1, column=0, sticky=tk.W)

# Sección de N-gramas
frame_ngramas = tk.Frame(contenedor_principal, padx=10, pady=10)
frame_ngramas.pack(side=tk.LEFT)

tk.Label(frame_ngramas, text="N-gramas").grid(row=0, column=0, sticky=tk.W)
ngramas = tk.StringVar()
ngramas.set("Unigrama")  # Valor predeterminado
for i, option in enumerate(["Unigrama", "Bigrama"]):
    tk.Radiobutton(frame_ngramas, text=option, variable=ngramas, value=option).grid(row=i+1, column=0, sticky=tk.W)

# Sección de Comparación
frame_comparacion = tk.Frame(contenedor_principal, padx=10, pady=10)
frame_comparacion.pack(side=tk.LEFT)

tk.Label(frame_comparacion, text="Comparación").grid(row=0, column=0, sticky=tk.W)
comparacion = tk.StringVar()
comparacion.set("Titulo")  # Valor predeterminado
for i, option in enumerate(["Titulo", "Contenido", "Titulo+Contenido"]):
    tk.Radiobutton(frame_comparacion, text=option, variable=comparacion, value=option).grid(row=i+1, column=0, sticky=tk.W)

# Selector de archivos
selector_archivos = tk.Button(root, text="Seleccionar Archivo", command=seleccionar_archivo)
selector_archivos.pack()

# Botón de Comparar
boton_comparar = tk.Button(root, text="Comparar", command=comparar)
boton_comparar.pack()

# Etiqueta para mostrar mensaje
mensaje = tk.Label(root, text="")
mensaje.pack()

root.mainloop()