import tkinter as tk
import random

# Diccionario de emojis
emojis = {
    "🍎": "Manzana",
    "🐶": "Perro",
    "🚗": "Carro",
    "🌞": "Sol",
    "📚": "Libros",
    "⭐": "Estrella",
    "🐌": "Caracol",
    "🥑": "Aguacate",
    "🍍": "Piña"


}

emoji_actual = random.choice(list(emojis.keys()))

# Función para comprobar la respuesta
def comprobar():
    respuesta = entrada.get()

    if respuesta.lower() == emojis[emoji_actual].lower():
        resultado.config(text="🎉 ¡Correcto!", fg="green")
    else:
        resultado.config(text=f"❌ Era: {emojis[emoji_actual]}", fg="red")

# Función para otro emoji
def nuevo():
    global emoji_actual
    emoji_actual = random.choice(list(emojis.keys()))
    etiqueta_emoji.config(text=emoji_actual)
    entrada.delete(0, tk.END)
    resultado.config(text="")

# Ventana
ventana = tk.Tk()
ventana.title("🎮 Adivina el Emoji")
ventana.geometry("800x600")
ventana.configure(bg="#D6EAF8")

titulo = tk.Label(
    ventana,
    text="🎮 ADIVINA EL EMOJI 🎮",
    font=("Arial", 20, "bold"),
    bg="#D6EAF8"
)
titulo.pack(pady=10)

etiqueta_emoji = tk.Label(
    ventana,
    text=emoji_actual,
    font=("Arial", 60),
    bg="#D6EAF8"
)
etiqueta_emoji.pack()

entrada = tk.Entry(ventana, font=("Arial", 20))
entrada.pack(pady=20)

boton = tk.Button(
    ventana,
    text="Comprobar",
    font=("Arial", 22),
    command=comprobar,
    bg="#58D68D"
)
boton.pack(pady=10)

resultado = tk.Label(
    ventana,
    text="",
    font=("Arial", 22),
    bg="#D6EAF8"
)
resultado.pack(pady=10)

boton2 = tk.Button(
    ventana,
    text="Nuevo Emoji",
    font=("Arial", 22),
    command=nuevo,
    bg="#5DADE2"
)
boton2.pack()

ventana.mainloop()