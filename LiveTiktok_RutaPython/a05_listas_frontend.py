"""
IDE: REPLIT.COM
Ruta 2024 Python:
Videos grabados en Kick: 
https://kick.com/codeando
4. Listas: Tu Primera Estructura de Datos
"""
from a05_listas_backend import (
  acceder_elementos,
  arreglo_numpy,
  compresion_lista,
  concatenacion_lista,
  crud,
  eliminar_lista_seguidores,
  funciones_lista,
  lista_de_listas,
  modificar_lista_seguidores,
  slicing_lista,
  tipo_lista,
)

while True:
  print("============================")
  print("Menu: listas")
  print("============================")
  print("Ejecuta ejemplos:")
  print("1. Crea un arreglo(array)")
  print("2. Crea una lista")
  print("3. Muestra elementos de una lista")
  print("4. Crea un CRUD con listas")
  print("5. Modifica lista de seguidores")
  print("6. Elimina lista de seguidores con bucle")
  print("7. Compresiones de listas ")
  print("8. Slicing de listas ")
  print("9. Concatenacion de listas")
  print("10. Funciones utiles")
  print("11. Listas de listas")
  print("============================")
  print("Elija numero del menu o 'salir' ")

  ingreso = input()

  if ingreso.lower() == "salir":
    break

  numero = int(ingreso)

  if numero == 1:
    print("Respuesta:")
    arreglo_numpy()
  elif numero == 2:
    print("Respuesta:")
    tipo_lista()
  elif numero == 3:
    print("Respuesta:")
    acceder_elementos()
  elif numero == 4:
    print("Respuesta:")
    crud()
  elif numero == 5:
    print("Respuesta:")
    modificar_lista_seguidores()
  elif numero == 6:
    print("Respuesta:")
    eliminar_lista_seguidores()
  elif numero == 7:
    print("Respuesta:")
    compresion_lista()
  elif numero == 8:
    print("Respuesta:")
    slicing_lista()
  elif numero == 9:
    print("Respuesta:")
    concatenacion_lista()
  elif numero == 10:
    print("Respuesta:")
    funciones_lista()
  elif numero == 11:
    print("Respuesta:")
    lista_de_listas()
  else:
    print("Numero no valido")
  