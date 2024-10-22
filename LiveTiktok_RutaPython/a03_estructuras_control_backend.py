"""
IDE: REPLIT.COM
Ruta 2024 Python:
Videos grabados en Kick: 
SEGUIR: https://kick.com/codeando
3. Estructuras de Control: Decisiones con Condicionales ()
"""

from a02_operadores_backend import (
    cantidad_tienda_mexico,
    cantidad_tienda_peru,
    cantidad_total,
)

#Estructuras de control
#Toma de decisiones
#If (Si condicional)
"""
if (CONDICION):
  BLOQUE DE CODIGO IDENTADO A EJECUTARSE
  SI LA CONDICION ES TRUE
CODIGO DESPUES DEL IF
"""


def ejemplo_if_1():
  if True:
    print("Ejecutando el if con condicional True")


def ejemplo_if_2():
  if False:
    print("Ejecutando el if con condicional false")


def ejemplo_if_3():
  
  if cantidad_total > cantidad_tienda_peru:
    print("hola")
    print("Cantidad total es mayor que cantidad peru")
  print("Fin del if")

def ejemplo_if_4():
  
  if ((cantidad_total > cantidad_tienda_peru)
      or (cantidad_total < cantidad_tienda_mexico)
      or (cantidad_total < cantidad_tienda_mexico)
      or (cantidad_total < cantidad_tienda_mexico)
      or (cantidad_total < cantidad_tienda_mexico)):
    print(
        "Cantidad total es mayor que cantidad peru OR menor que cantidad mexico"
    )


#If condicional con else
"""
if (CONDICION):
  BLOQUE DE CODIGO IDENTADO A EJECUTARSE
  SI LA CONDICION ES TRUE
else:
  BLOQUE DE CODIGO IDENTADO A EJECUTARSE
  SI LA CONDICION ES FALSE
  
CODIGO DESPUES DEL IF-ELSE
"""


def ejemplo_if_else():
  if cantidad_total > cantidad_tienda_peru:
    print("Cantidad total es mayor que cantidad peru")
  else:
    print("Cantidad peru es mayor que cantidad total")


#If condicional con elif
"""
If (CONDICION):
  BLOQUE DE CODIGO IDENTADO A EJECUTARSE
  SI LA CONDICION ES TRUE
ELIF (CONDICION):
  BLOQUE DE CODIGO IDENTADO A EJECUTARSE
  SI LA CONDICION ES TRUE
ELIF (CONDICION):
  BLOQUE DE CODIGO IDENTADO A EJECUTARSE
  SI LA CONDICION ES TRUE
ELSE:
  BLOQUE DE CODIGO IDENTADO A EJECUTARSE
  SI LAS CONDICIONES SON FALSE
CODIGO DESPUES DEL IF-ELIF-ELSE
"""


def ejemplo_if_elif_else():
  if cantidad_total > cantidad_tienda_peru:
    print("Cantidad total es mayor que cantidad peru")
  elif cantidad_total > cantidad_tienda_mexico:
    print("Cantidad total es mayor que cantidad mexico")
  else:
    print("Cantidad peru y mexico es mayor que cantidad total")


# If else de una linea
# <valor_si_verdadero> if <condición> else <valor_si_falso>


def ejemplo_if_else_en_1_linea():
  contador = 0
  limite = 20
  respuesta = limite if contador % 2 == 0 else limite * 2
  print(respuesta)
