"""
IDE: REPLIT.COM
Ruta 2024 Python:
Videos grabados en Kick: 
https://kick.com/codeando
3. Estructuras de Control: Decisiones con Condicionales ()
"""

from a03_estructuras_control_backend import (
    ejemplo_if_1,
    ejemplo_if_2,
    ejemplo_if_3,
    ejemplo_if_4,
    ejemplo_if_elif_else,
    ejemplo_if_else,
    ejemplo_if_else_en_1_linea,
)

while True:
  print("============================")
  print("Menu: estructuras de control")
  print("============================")
  print("Ejecuta estructuras de control")
  print("1. Ejecuta if con condicional True")
  print("2. Ejecuta if con condicional False")
  print("3. Ejecuta if con condicional que compara cantidades")
  print("4. Ejecuta if con muchas condicionales")
  print("5. Ejecuta if-else")
  print("6. Ejecuta if_elif_else")
  print("7. Ejecuta if_else_en_1_linea")
  print("============================")
  print("Elija numero del menu o 'salir' ")

  ingreso = input()

  if ingreso.lower() == "salir":
    break

  numero = int(ingreso)

  if numero == 1:
    print("Respuesta:")
    ejemplo_if_1()
  elif numero == 2:
    print("Respuesta:")
    ejemplo_if_2()
  elif numero == 3:
    print("Respuesta:")
    ejemplo_if_3()
  elif numero == 4:
    print("Respuesta:")
    ejemplo_if_4()
  elif numero == 5:
    print("Respuesta:")
    ejemplo_if_else()
  elif numero == 6:
    print("Respuesta:")
    ejemplo_if_elif_else()
  elif numero == 7:
    print("Respuesta:")
    ejemplo_if_else_en_1_linea()
  else:
    print("Numero no valido")
