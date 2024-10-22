import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi Ventana")
ventana.geometry("400x500")

etiqueta = tk.Label(ventana, 
                    text="Hola, tiktok!",
                    height=3, 
                    font=("Arial", 12, "bold"))
etiqueta.pack()
print(type(etiqueta))

etiqueta = tk.Label(ventana, 
                    text="Gracias por su apoyo",
                    height=3, 
                    bg="yellow", 
                    fg="red")
etiqueta.pack()

etiqueta = tk.Label(ventana, 
                    text="Empieza una nueva secuencia",
                    height=3, 
                    relief="solid", 
                    borderwidth=1, 
                    padx=80, 
                    pady=2)
etiqueta.pack()

etiqueta = tk.Label(ventana, 
                    text="Crear aplicaciones de escritorio",
                    height=3, 
                    fg="blue", 
                    cursor="hand2")
etiqueta.pack()

etiqueta = tk.Label(ventana, 
                    text="Con python obvio...",
                    height=3, 
                    bg="green", 
                    fg="white",  
                    relief="raised")
etiqueta.pack()

etiqueta = tk.Label(ventana, 
                    text="Son todos bienvenidos",
                    height=3, 
                    underline=0)
etiqueta.pack()


ventana.mainloop()