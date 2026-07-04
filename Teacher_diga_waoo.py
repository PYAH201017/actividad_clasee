import tkinter as tk

def mostrar_mensaje(texto):
    ventana = tk.Toplevel()
    ventana.title("Resultado")
    ventana.geometry("400x200")
    ventana.configure(bg="white")

    mensaje = tk.Label(
        ventana,
        text=texto,
        font=("Arial", 16),
        bg="white"
    )
    mensaje.pack(expand=True)


screen = tk.Tk()
screen.title("Teacher")
screen.geometry("400x300")
screen.configure(bg="white")

titulo = tk.Label(screen,text="Teacher",font=("Arial", 20, "bold"),bg="white")
titulo.pack(pady=30)
 
boton_waoooo= tk.Button(screen,text="Waoo",bg="blue",fg="white",width=15,command=lambda: mostrar_mensaje("waozzzzzzzzzz"))
boton_waoooo.pack(pady=10)

boton_no = tk.Button(screen,text="No, guácala",bg="blue",fg="white",width=15,command=lambda: mostrar_mensaje("Namb teacher dele Waoooo"))
boton_no.pack(pady=10)

screen.mainloop()
