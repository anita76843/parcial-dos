import tkinter as tk
from tkinter import messagebox
import random

def respuesta_si():
    messagebox.showinfo("Respuesta", "¡Sabía que sí querías!")

def mover_boton_no(event):
    # Genera una nueva posición aleatoria para el botón "No"
    nuevo_x = random.randint(0, ventana.winfo_width() - boton_no.winfo_width())
    nuevo_y = random.randint(0, ventana.winfo_height() - boton_no.winfo_height())
    boton_no.place(x=nuevo_x, y=nuevo_y)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("¿Quieres ser mi novio?")
ventana.geometry("400x200")

# Crear el botón "Sí"
boton_si = tk.Button(ventana, text="Sí", command=respuesta_si)
boton_si.place(x=100, y=100)

# Crear el botón "No" y asignarle el evento de movimiento
boton_no = tk.Button(ventana, text="No")
boton_no.place(x=200, y=100)
boton_no.bind("<Enter>", mover_boton_no)

# Iniciar el bucle de la ventana
ventana.mainloop()





