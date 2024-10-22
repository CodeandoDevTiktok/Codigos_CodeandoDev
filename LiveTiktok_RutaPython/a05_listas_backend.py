"""
IDE: REPLIT.COM
Ruta 2024 Python:
Videos grabados en Kick: 
https://kick.com/codeando
5. Listas: Tu Primera Estructura de Datos
"""

#Estructura de una lista
#lista = [elemento_1, elemento_2, elemento_3, ...]

import numpy

data = [55, "Hola", True]
seguidores = ["oscar", "gato", "gilber", "juan", "luis", "Rickrapthor"]


def arreglo_numpy():
  print("Arreglo inicial:")
  array = numpy.array([1, 2, 3, 4, 5])
  print(type(array))


def tipo_lista():
  print("Lista inicial", data)
  print("Tipo:", type(data))


def acceder_elementos():
  # Acceder a un elemento de la lista
  print("Posicion 0:", data[0])
  print("Posicion 1:", data[1])
  print("Posicion 2:", data[2])
  print("Posicion -1:", data[-1])


def crud():
  #CRUD
  #Create - Crear
  edades = [20, 18, 25, 30, 22, 19]
  print("CREAR:")
  print("Lista inicial:", edades)

  #Read - Leer
  print("LEER:")
  print("Posicion 0:", edades[0])
  print("Posicion -1:", edades[-1])

  #Update - Actualizar
  edades[0] = 21
  print("ACTUALIZAR:")
  print("Posicion 0:", edades[0])
  print("Lista modificada:", edades)

  #Delete - Eliminar
  print("ELIMINAR:")
  print("Posicion 0:", edades[0])
  del edades[0]
  print("Lista modificada:", edades)


def modificar_lista_seguidores():

  print("Lista inicial:", seguidores)

  seguidores.append("juan")
  print("Append:", seguidores)
  seguidores.insert(0, "sergio")
  print("Insert:", seguidores)
  seguidores.remove("gilber")
  print("Remove:", seguidores)
  seguidores.pop(0)
  print("Pop:", seguidores)
  seguidores_1 = sorted(seguidores)
  print("Sort seguidores 1:", seguidores_1)
  print("Sort seguidores:", seguidores)
  seguidores.sort()
  print("Sort:", seguidores)
  seguidores.reverse()
  print("Reverse:", seguidores)
  seguidores_tiktok = ["jessenia", "cr7"]
  seguidores.extend(seguidores_tiktok)
  print("Extend:", seguidores)


def eliminar_lista_seguidores():
  while seguidores:
    print("Eliminando:", seguidores.pop())
    print(seguidores)
  print("Lista vacia:", seguidores)


def compresion_lista():
  # Compresiones de listas
  #Ejemplo 1
  numeros = [1, 2, 3, 4, 5]
  cuadrados = [numero**2 for numero in numeros]

  print("Compresion de listas:", cuadrados)


def slicing_lista():
  #Slicing de listas
  #Ejemplo 2
  puntajes = [1, 2, 3, 4, 5]
  print("Slicing de listas:", puntajes[1:3])


def concatenacion_lista():
  #Concatenacion de listas
  #Ejemplo 3
  lista_1 = [1, 2, 3]
  lista_2 = [4, 5, 6]
  lista_concatenada = lista_1 + lista_2
  print("Concatenacion de listas:", lista_concatenada)


def funciones_lista():
  #funciones utiles:
  datos = [89, 21, 314, 42, 5, 6, 7, 8, 9, 10]
  longitud = len(datos)
  print("Longitud:", longitud)
  minimo = min(datos)
  print("Minimo:", minimo)
  maximo = max(datos)
  print("Maximo:", maximo)
  suma = sum(datos)
  print("Suma:", suma)


def lista_de_listas():
  #listas multidimensionales
  #Ejemplo 4
  matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  print("Matriz:", matriz)
