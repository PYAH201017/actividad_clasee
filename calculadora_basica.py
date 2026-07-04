import customtkinter as ctk

# Configuración de la ventana directa
app = ctk.CTk()
app.title("Calculadora")
app.geometry("300x400")
ctk.set_appearance_mode("dark")

# Pantalla
pantalla = ctk.CTkEntry(app, width=270, height=50, font=("Arial", 24), justify="right")
pantalla.pack(pady=15)

# Función para los clics
def presionar(valor):
    if valor == 'C':
        pantalla.delete(0, 'end')
    elif valor == '=':
        try:
            resultado = eval(pantalla.get())
            pantalla.delete(0, 'end')
            pantalla.insert(0, str(resultado))
        except:
            pantalla.delete(0, 'end')
            pantalla.insert(0, "Error")
    else:
        pantalla.insert('end', valor)

# Contenedor de botones
frame = ctk.CTkFrame(app, fg_color="transparent")
frame.pack(pady=5, fill="both", expand=True)

botones = [
    ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
    ('C', 3, 0), ('0', 3, 1), ('=', 3, 2), ('+', 3, 3)
]

for texto, fila, col in botones:
    btn = ctk.CTkButton(
        frame, 
        text=texto, 
        font=("Arial", 18, "bold"),
        command=lambda t=texto: presionar(t)
    )
    btn.grid(row=fila, column=col, padx=5, pady=5, sticky="nsew")

for i in range(4):
    frame.rowconfigure(i, weight=1)
    frame.columnconfigure(i, weight=1)

app.mainloop()