"""
IDE: REPLIT.COM
Ruta 2024 Python:
Videos grabados en Kick: 
SIGUEME: https://kick.com/codeando
4. Bucles While: Repetición Controlada (*)
Suscriptores de tiktok : 30min asesoria personalizada
"""
#Bucle While
#¿Que es un bucle?
#Un bucle es una estructura de control que permite ejecutar un bloque de código repetidamente
#¿Que es un bucle while?
#Un bucle while se ejecuta mientras una condición sea verdadera
"""
while CONDICION:
  BLOQUE DE CODIGO IDENTADO A EJECUTARSE
  SI LA CONDICION ES TRUE
  NO CONOCES EL NUMERO DE VUELTAS DEL BUCLE
"""

#Ejemplo 1


def ejemplo_while_1():

  edad = 10
  while edad < 18:
    print("Bienvenido")
    edad += 2


def ejemplo_while_infinito():

  while True:
    print("Desea continuar? S/N")
    respuesta = input()
    if respuesta == "N":
      break
  print("Salistes del bucle")

  #continue, permite moverte a la siguiete iteracion del bucle


def ejemplo_while_con_condicion_falsa():
  while False:
    if respuesta == "N":
      break
    else:
      print("bien")
    print("Adios")


def ejemplo_while_con_condicion_if_else():
  contador = 0
  limite = 20

  while contador < (limite if contador % 2 == 0 else limite * 2):
    print("ok")
    contador += 5


def ejemplo_login():
  usuario = "codeando"
  password = 123

  while True:
    print("Ingresa tu usuario")
    usuario_entrante = input()
    print("Ingresa tu password")
    password_entrante = int(input())
    if usuario_entrante == usuario and password_entrante == password:
      print("Bienvenido")
      break
    else:
      print("Acceso incorrecto")


def ejemplo_injeccion_en_login():
  while True:
    print("Ingresa password o 'salir'")
    respuesta = input()
    if respuesta == "salir":
      break
    resultado = eval(respuesta)
    print(resultado)
