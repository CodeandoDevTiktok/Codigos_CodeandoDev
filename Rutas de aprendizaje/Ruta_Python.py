#Practicando Python v3 desde 0
#IDE : www.replit.com
#CodeForces
"""
Parte I
-Logica de programación (ok)
-Variables (ok)
-Tipos de datos (ok)
"""

#Logica de programacion

#1. Entradas
#2. Salidas
#3. Restricciones
#4. Objetivo

#Crea un calculadora
#Entradas : numeros 0 al 9, operacion: +.., enter/=
#Salidas :impresion resultado +,-,*,...
#Restricciones: max digitos
#Objetivo: imprimir respuesta


print("----Parte I-----")
# Variables
numero = 8  #Integer
decimal = 18.9  #Float
texto = "hola"  #String
logica = True  #Bool

#Ejemplos de impresiones
print("El numero es: ", numero)
print(texto, " a todos")
print("La logica", logica, "es la rpta.")

#Validacion de tipo de datos
print("---------")
print(type(decimal))
print(type(logica))
print(type(texto))
print("---------")


"""
Parte II
- Listas (ok)
- Metodos de listas (ok)
- Errores en listas (ok)
"""

print("----Parte II-----")
#Posicion 0->x
#Posicion  <- -3
bicicleta = ["trek", "especial", "campo"]

print(f"Mi lista es: {bicicleta[1]}")
print(type(bicicleta[0]))
print(bicicleta[0].title())
print(type(bicicleta))

#Operaciones:
#Agregar al final
bicicleta.append("montañera")
print(bicicleta)
#Insertar
bicicleta.insert(1, "xtreme")
print(bicicleta)
#Eliminar
bicicleta.remove("trek")
print(bicicleta)
#Ordenar
bicicleta.sort()
print(bicicleta)

#Errores:
bicicleta2 = ["trek", "especial", "campo"]
print(bicicleta2[2])
"""
Parte III
-Declaraciones If Simple (ok)
-Declaraciones If Multiple / Anidado (ok)
"""

print("----Parte III-----")
#Si condicional
#(Condicion = True / False)
x = "Si"
if x == "Si":
  print("Me quedo a ver")

carros = ["audi", "bmw", "toyota"]
#If (Condicion = True / False)
if carros[2] == "toyota":
  print(carros[0].title())
  print(carros[1].title())
  print(carros[2].title())

if carros[0] != "toyota":
  print(carros[0].upper())

if True:
  print("Siempre imprime")

if carros[0] == "toyota" and carros[1] == "toyota":
  print("Hola!")

if "toyota" in carros:
  print("esta incluido Toyota")
else:
  print("no esta incluido Toyota")

if "abc" not in carros:
  print("No esta incluido abc")

respuesta = carros[2].title() if carros[0] == 'toyota' else carros[2].upper()
print(respuesta)

import random

numero = random.randint(10, 60)
if numero < 20:  #>, >=, <, <=
  print(f"Mi numero: {numero}, costo es 5")
elif numero < 30:
  print(f"Mi numero: {numero}, Tu costo es 10")
elif numero < 40:
  print(f"Mi numero: {numero}, Tu costo es 15")
elif numero < 50:
  print(f"Mi numero: {numero}, Tu costo es 20")
else:
  print(f"Mi numero: {numero}, Tu costo es 30")

if numero < 20:  #>, >=, <, <=
  print(f"Mi numero: {numero}, costo es 5")
if numero < 30:
  print(f"Mi numero: {numero}, Tu costo es 10")
if numero < 40:
  print(f"Mi numero: {numero}, Tu costo es 15")
if numero < 50:
  print(f"Mi numero: {numero}, Tu costo es 20")
else:
  print(f"Mi numero: {numero}, Tu costo es 30")
"""
Parte IV
-Diccionarios simple (ok)
-Operaciones diccionarios (ok)
-Introducción a bucles <-- For
"""

print("----Parte IV-----")
#API : Interfaz compartimos datos
#JSON : Notacion
#Diccionarios:
persona = {"nombre": "jorge", "edad": 17, "profesion": "ingeniero"}

print(persona["nombre"])
print(persona["edad"])
print(persona["profesion"])

#Operaciones:
#Agregado
persona["redes_sociales"] = ["tiktok", "instagram"]
print(persona)

#Comparacion
if persona["edad"] > 15:
  print("Mayor a 15")

#Eliminar
del persona["redes_sociales"]
#persona.clear()
persona.pop("edad")
print(persona)
print(persona["profesion"].upper())

#Obtener valores
print(persona.get("direccion", "No existe campo: Direccion"))

#Bucles: repeticiones
#Recorridos de listas/diccionarios

#For
lista = [1, 2, 3, 4, 5]

for iterador in lista:
  print(iterador)

for x in range(1, 6):
  print(x)

persona2 = {"nombre": "jorge", "edad": 17, "profesion": "ingeniero"}

for clave in persona2.keys():
  print("clave:", clave.title())

for clave, valor in persona2.items():
  print("clave:", clave.title())
  print("valor:", valor)
"""
Parte V :
Ingreso de datos del usuario (ok)
Bucles While (ok)
While y listas (ok)
While y diccionarios (revisar)
"""

print("----Parte V-----")

#mensaje = int(input("Cual es tu edad?"))
#print(mensaje)
#print(type(mensaje))

#Python
#mensaje2 = input("Cual es tu nombre?")
#print(f"Bienvenido, {mensaje2}")

#Bucles While
#Repeticion

numero = 1
#True/False
while numero <= 5:
  #bloque de codigo
  numero = numero + 1
  if numero % 2 == 0:
    continue
  print(numero)
"""
mensaje = ""
while mensaje != "cerrar":
  mensaje = input("Ingresa un numero").lower()
  print("Escribe 'cerrar' si deseas salir")
  print(mensaje)
"""

activo = False
while activo:
  mensaje = input("Ingresa valor")

  if mensaje == "q":
    activo = False
  else:
    print(mensaje)

while True:
  break

estado = False
while estado:
  jugador_vivo = True
  while jugador_vivo:
    print("Jugador en combate")
    jugador_vivo = False
  print("Juego en funcionamiento")
  estado = False

#Listas

nombres_suscrito = ["Brian", "Jose", "Ana"]
nombres_no_suscrito = []

while nombres_suscrito:
  persona = nombres_suscrito.pop()
  print("Verificando :")
  nombres_no_suscrito.append(persona)
  print(nombres_no_suscrito)

#Diccionarios

nombres_suscrito = {}
lista_diccionarios = []
estado = False
while estado:
  nombre = input("Tu nombre:")
  edad = int(input("Tu edad:"))
  profesion = input("Tu profesion:")

  nombres_suscrito["nombre"] = nombre
  nombres_suscrito["edad"] = edad
  nombres_suscrito["profesion"] = profesion
  lista_diccionarios.append(nombres_suscrito)
  print(lista_diccionarios)
  pregunta = input("Desea continuar S/N").upper()
  if pregunta == "N":
    estado = False

print(lista_diccionarios)
"""
Parte VI
- Funciones (ok)
- Modulos
"""

print("----Parte VI-----")


def calculadora(num1, num2):
  #Bloque de la funcion
  print(f"Operacion entre {num1} y {num2}")


calculadora(9, 5)
calculadora(15, 76)
calculadora(20, 36)
calculadora(num1=10, num2=8)
calculadora(num2=5, num1=6)
#calculadora()


def formatea_nombres(nombre, apellido, nick=""):
  nombre_completo = f"{nombre} {apellido} {nick}"
  return print(nombre_completo.title())


formatea_nombres("michael", "jackson")
formatea_nombres("leonel", "messi", "goat")

#Diccionarios {"nombre":"Jorge","edad":43}


def registra_persona(nombre, apellido, profesion=None):
  persona = {"nombre": nombre, "apellido": apellido}
  if profesion:
    persona["profesion"] = profesion
  return print(persona)


registra_persona("chris", "ronaldo")
registra_persona("leonel", "messi", "futbolista")

#While

while False:
  print("Ingresa nombres: ")
  print("Si deseas salir presiona 'cerrar': ")
  nombre = input("Ingresa nombre: ")
  if nombre == 'cerrar':
    break
  apellido = input("Ingresa apellido: ")
  if apellido == 'cerrar':
    break
  print(registra_persona(nombre, apellido))

#listas


def obtener_nombres(nombres_1):
  for iterador in nombres_1:
    print(iterador.title())


personas = ["pedro", "ana", "felipe"]
obtener_nombres(personas)


#Pizza
def hacer_pizza(tamanio, *ingredientes):
  print("Pizza de tamaño:", tamanio)
  for iterador in ingredientes:
    print(iterador.title())


hacer_pizza(12, "queso")
hacer_pizza(20, "tomate", "aceituna", "queso")
print(type(hacer_pizza))
print(type(hacer_pizza("queso")))


def contruir_perfil(nombre, apellido, **perfiles):
  perfiles["nombre"] = nombre
  perfiles["apellido"] = apellido
  return print(perfiles)


contruir_perfil("albert",
                "einstein",
                edad=60,
                especialidad="fisico",
                nacionalidad="USA")
"""
import random
from "nombre_modulo" import "funcion1"
from pizza import hacer_pizza as hp
from pizza as p
from pizza import *

hp(12, "queso")
p.hacer_pizza(12, "queso")
"""
"""
Parte VII
- POO
- Clases
- Herencia
"""

print("----Parte VII-----")

#Que es un objeto:
#Laptop
#Persona
#Archivo
#Libro

#Serpiente: posicion,color,funcionalidad
#Alimentarse, Moverse, Crecer

#Manzana: posicion, color
#Tiempo de vida

#Objeto = Perro


class Perro:
  #metodos -> funciones
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad
    self.color = "Marron"  #Seteo

  def ladrar(self):
    print(
      f"Mi perro {self.nombre} cuya edad es {self.edad} dice guau guau! y es de color {self.color}"
    )

  def modifica_color(self, color_nuevo):
    self.color = color_nuevo

  #variables


#Instancia
p1 = Perro("fido", 1)
print(p1.nombre)
print(p1.edad)
p1.ladrar()
#Instancia
p2 = Perro("Rex", 0.5)
p2.ladrar()
p2.modifica_color("Verde")
p2.ladrar()


#Herencia:
class Carro:

  def __init__(self, modelo, anio):
    self.modelo = modelo
    self.anio = anio

  def obtener_nombre(self):
    print(f"El auto es {self.modelo} y del año: {self.anio}")


class CarroElectrico(Carro):

  def __init__(self, modelo, anio):
    super().__init__(modelo, anio)

  def obtener_nombre2(self):
    print(f"Mi auto:  {self.modelo}\nAño: {self.anio}\n")


#instanciar el objeto de Carro electrico:

carro1 = CarroElectrico("nisan leaf", 2024)
carro1.obtener_nombre()
"""
Parte VIII
- Lectura de Archivos (ok)
- Escritura de Archivos (ok)
- Excepciones
"""
print("----Parte VIII-----")
from pathlib import Path

ruta = Path("ejemplo.txt")
contenido = ruta.read_text()
print(contenido)

contenido_nuevo = "Hola a todos. \n"
contenido_nuevo += "Me encanta hacer lives de progra \n"
contenido_nuevo += "Saludooos!! \n"

ruta.write_text(contenido_nuevo)
contenido = ruta.read_text()
print(contenido)

#Excepciones -> Manejo de errores en ejecucion de un programa

try:
  #Bloque de codigo identado
  print("Ejecutando...")
  lista = [1, 2, 3]
  print(lista[9])
except IndexError:
  print("Haz ingresado un indice no valido")

try:
  print(1 / 0)
except ZeroDivisionError:
  print("Division entre cero no es posible")

