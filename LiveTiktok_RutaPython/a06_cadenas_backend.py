"""
IDE: REPLIT.COM
Ruta 2024 Python:
Videos grabados en Kick: 
https://kick.com/codeando
6. Cadenas de Texto: Manipulación de Texto
"""

texto = "Hola tiktok"

#Inmutabilidad
print("caracter:", texto[0])
#texto[0] = "J" (Nos da error)

#Creacion textos

texto_1 = "Hola"
texto_2 = 'tiktok'
texto_3 = """
Hola a todos
Este es un parrafo
Saludos
Codeando dev
"""
print(texto_1)
print(texto_2)
print(texto_3)

#Caracteres especiales

texto_4 = "Hola\nTiktok\nSaludos\nCodeando\nDev"
print(texto_4)

texto_5 = "Hola\ttiktok\tSaludos\tCodeando\tDev"
print(texto_5)

texto_6 = "Hola\\tiktok\\Saludos\\Codeando\\Dev"
print(texto_6)

#Operaciones

#Concatenacion
texto_7 = texto_1 + " " + texto_2
print("Concatenacion:", texto_7)

#Repeticion
texto_8 = texto_3 * 3
print("Repeticion:", texto_8)

#Subcadenas
texto_9 = "Hola tiktok"
print("Subcadena:", texto_9[0:4])

#Longitud
print("Longitud:", len(texto_9))

#Iteracion
texto_10 = """
Saludos a todos los seguidores
2024
Tiktok
"""

for posicion, caracter in enumerate(texto_10):
  print(f"Caracter {posicion}: ", caracter)

#Metodos de las cadenas

print("Mayusculas: ", texto_10.upper())
print("Minusculas: ", texto_10.lower())
print("Capitalizar: ", texto_10.capitalize())
print("Titulo: ", texto_10.title())


