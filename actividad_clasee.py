import tkinter as tk
 
# Crear ventana
ventana = tk.Tk()
ventana.title("Cambio de colores")
ventana.geometry("400x300")
 
# Lista de colores
colores = ["red","blue","green", "yellow", "orange", "pink",  "purple",   "cyan", "magenta",   "brown",  "black","white", "gray", "gold","silver","navy","skyblue",  "lightblue",   "darkblue",    "lime",    "darkgreen","olive",   "turquoise", "violet","indigo","beige","coral","salmon","khaki","lavender","plum","tan","maroon","teal","aqua","chocolate","crimson","hotpink","deeppink","tomato"]
  
# Variable para saber qué color sigue
posicion = 0
 
def cambiar_color():
    global posicion
 
    ventana.config(bg=colores[posicion])
 
    posicion += 1
 
    if posicion == len(colores):
        posicion = 0
 
# Botón
boton = tk.Button(ventana, text="Cambiar color", command=cambiar_color)
boton.pack(pady=100)
 
ventana.mainloop()