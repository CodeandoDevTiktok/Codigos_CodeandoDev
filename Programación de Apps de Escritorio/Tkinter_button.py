from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.geometry("400x500")


def mostrar_mensaje():
    print("¡Hola, Tkinter!")

def mostrar_mensaje_check():
    print("¡Check!")

def cerrar_ventana():
    print("¡Bye!")
    ventana.destroy()

def cambiar_texto():
    boton_cambiar.config(text="¡Clicado!")

def mostrar_cuadro_dialogo():
    messagebox.showinfo("Cuadro de diálogo", "¡Has hecho clic en el botón!")

def deshabilitar_otro_boton():
    otro_boton.config(state=DISABLED)

def abrir_nueva_ventana():
    nueva_ventana = Toplevel(ventana)
    nueva_ventana.title("Nueva ventana")
    nueva_ventana.geometry("200x200")

# Botones

boton_texto = Button(ventana, 
                     text="Haz clic y mira el terminal", 
                     command=mostrar_mensaje, 
                     padx=80, 
                     pady=2, 
                     width=20)
boton_texto.pack(pady=10)

imagen = PhotoImage(file="image.png").subsample(10, 10)
boton_imagen = Button(ventana, 
                      image=imagen, 
                      command=mostrar_mensaje_check, 
                      padx=80, 
                      pady=2)
boton_imagen.pack(pady=10)

boton_cerrar = Button(ventana, 
                      text="Cerrar ventana", 
                      command=cerrar_ventana, 
                      padx=80, 
                      pady=2, 
                      width=20)
boton_cerrar.pack(pady=10)

boton_cambiar = Button(ventana, 
                       text="Haz clic", 
                       command=cambiar_texto, 
                       padx=80, 
                       pady=2, 
                       width=20)
boton_cambiar.pack(pady=10)

boton_mensaje = Button(ventana, 
                       text="Muestra mensaje", 
                       command=mostrar_cuadro_dialogo, 
                       padx=80, 
                       pady=2, 
                       width=20)
boton_mensaje.pack(pady=10)

boton_deshabilitar = Button(ventana, 
                            text="Haz clic para deshabilitar boton", 
                            command=deshabilitar_otro_boton, 
                            padx=80, 
                            pady=2, 
                            width=20)
boton_deshabilitar.pack(pady=10)

otro_boton = Button(ventana, 
                    text="Botón deshabilitado", 
                    state=ACTIVE, 
                    padx=80, 
                    pady=2, 
                    width=20)
otro_boton.pack(pady=10)

boton_abrir = Button(ventana, 
                     text="Abrir ventana", 
                     command=abrir_nueva_ventana, 
                     padx=80, 
                     pady=2, 
                     width=20)
boton_abrir.pack(pady=10)

ventana.mainloop()

