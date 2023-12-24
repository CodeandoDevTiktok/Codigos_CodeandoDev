import random
import time
import sys
import os
import colored
from termcolor import colored

colores = ["red", "yellow", "cyan"]

def limpiar_pantalla():
  if sys.platform == "win32":
    #Windows
    comando = "cls"
  else:
    #Linux / MacOS
    comando = "clear"

  os.system(comando)
  
def obtener_color_luz():
  
  esfera_luz = colored("o",colores[random.randint(0,len(colores)-1)])
  return esfera_luz
  
def imprimir_arbol_navidad():
  for i in range(1,30,2):
    luces_y_hojas = "".join(
      obtener_color_luz()
      if 250 <= random.randint(0,500) <= 750
      else colored("*","green")
      for j in range(i)
    )
    #print(luces_y_hojas)
    arbol = " "*(15- i//2) + luces_y_hojas + " "*(15-i//2)
    print(arbol)

  mensaje_navidad = colored(
    "Feliz Navidad Coders!",
    colores[random.randint(0,len(colores)-1)])
  print(" ")
  print(" ")
  print(" "*6 + mensaje_navidad + " "*6)
  print(" ")

def main():
  while True:
    print("Para salir presiona Ctrl + C")
    limpiar_pantalla()
    imprimir_arbol_navidad()
    time.sleep(0.5)
    limpiar_pantalla()
main()
