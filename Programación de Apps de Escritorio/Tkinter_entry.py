from tkinter import *
import tkinter as tk

ventana = Tk()
ventana.geometry("400x500")

etiqueta = tk.Label(ventana, 
                    text="Entradas",
                    height=3, 
                    font=("Arial", 12, "bold"))
etiqueta.pack()


entry = Entry(ventana, width=50)
entry.pack(pady=10)

entry = Entry(ventana, width=50)
entry.insert(0, "Texto predeterminado")
entry.pack(pady=10)

entry = Entry(ventana, state='disabled', width=50)
entry.pack(pady=10)

entry = Entry(ventana, bg='lightblue', width=50)
entry.pack(pady=10)

entry = Entry(ventana, fg='red', width=50)
entry.pack(pady=10)

entry = Entry(ventana, show='*', width=50)
entry.pack(pady=10)

def ejecutar_funcion(event):
    print("Se presionó Enter")

entry = Entry(ventana, width=50)
entry.bind("<Return>", ejecutar_funcion)
entry.pack(pady=10)

def validar_longitud(texto):
    if len(texto) <= 4:  # Longitud máxima permitida
        return True
    else:
        return False

validar_longitud_command = ventana.register(validar_longitud)
entry = tk.Entry(ventana, 
                 validate="key", 
                 validatecommand=(validar_longitud_command, '%P'), 
                 width=50)
entry.pack(pady=10)

def obtener_texto():
    texto = entry.get()
    print(texto)

entry = Entry(ventana, width=50)
entry.pack(pady=10)

button = Button(ventana, text="Obtener texto", command=obtener_texto)
button.pack(pady=10)


ventana.mainloop()
