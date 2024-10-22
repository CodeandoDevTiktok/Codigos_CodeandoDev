"""
IDE: REPLIT.COM
Ruta 2024 Python:
Videos grabados en Kick: 
https://kick.com/codeando
4. Bucles While: Repetición Controlada (*)
"""
from a04_bucles_while_backend import (
    ejemplo_injeccion_en_login,
    ejemplo_login,
    ejemplo_while_1,
    ejemplo_while_con_condicion_falsa,
    ejemplo_while_con_condicion_if_else,
    ejemplo_while_infinito,
)

while True:
  print("============================")
  print("Menu: bucles while")
  print("============================")
  print("Ejecuta ejemplos:")
  print("1. Ejecuta while con condicional True")
  print("2. Ejecuta while con condicional False")
  print("3. Ejecuta while con condicional If-else")
  print("4. Ejecuta while infinito")
  print("5. Ejecuta login con while")
  print("6. Ejecuta Inyeccion de codigo con while")
  print("============================")
  print("Elija numero del menu o 'salir' ")

  ingreso = input()

  if ingreso.lower() == "salir":
    break

  numero = int(ingreso)

  if numero == 1:
    print("Respuesta:")
    ejemplo_while_1()
  elif numero == 2:
    print("Respuesta:")
    ejemplo_while_con_condicion_falsa()
  elif numero == 3:
    print("Respuesta:")
    ejemplo_while_con_condicion_if_else()
  elif numero == 4:
    print("Respuesta:")
    ejemplo_while_infinito()
  elif numero == 5:
    print("Respuesta:")
    ejemplo_login()
  elif numero == 6:
    print("Respuesta:")
    ejemplo_injeccion_en_login()
  else:
    print("Numero no valido")
