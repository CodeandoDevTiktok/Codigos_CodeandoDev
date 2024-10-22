"""
IDE: REPLIT.COM
Ruta 2024 Python:
Videos grabados en Kick: 
https://kick.com/codeando
8. Funciones: Organizando y Reutilizando Código
"""


def nombre_funcion():
  print("Hola desde una funcion")
  for i in range(1, 11):
    print(i)


#Argumento : influencer
def seguidores_tiktok(red_social, influencer="Codeando"):
  print(f"Seguidores {influencer}")
  print(f"Red Social {red_social}")
  print("Jessenia")
  print("Juan")
  print("Gilber")
  print("Sergio")

def suma(a, b):
  return a + b

def resta(a, b):
  return a - b

def multiplicacion(a, b):
  return a * b

nombre_funcion()
nombre_funcion()
nombre_funcion()
nombre_funcion()
#Parametro : codeando
seguidores_tiktok("Tiktok", "Julian Arroyave")

resultado = suma(7,8)
print(resultado)

#Funcion anonima de 1 sola linea
suma_2 = lambda num1, num2: num1 + num2
print(suma_2(7,9))
