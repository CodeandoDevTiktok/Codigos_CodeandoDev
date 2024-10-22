"""
IDE: REPLIT.COM
Ruta 2024 Python:
Videos grabados en Kick: 
https://kick.com/codeando
10. Tuplas: Colecciones Inmutables
"""

redesSociales = ("x", "facebook", "instagram", "x", "tiktok")

#frecuencia
print(redesSociales.count("x"))

#indice del elemento
print(redesSociales.index("tiktok"))

for posicion, iterador in enumerate(redesSociales):
  print(posicion, iterador)