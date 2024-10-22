"""
IDE: REPLIT.COM
Ruta 2024 Python:
Videos grabados en Kick: 
https://kick.com/codeando
9. Diccionarios: Almacenamiento de Datos Clave-Valor
"""
asistentes_live = [{
    "id": 1,
    "nombre": "Red",
    "apellido": "point",
    "edad": 25
}, {
    "id": 2,
    "nombre": "lo",
    "apellido": "pez",
    "edad": 25
}, {
    "id": 3,
    "nombre": "fantastic",
    "apellido": "mantic",
    "edad": 25
}]

print(type(asistentes_live))
print(asistentes_live)


#create
seguidor = {"nombre": "Robert", "edad": 20, "ciudad": "Mexico"}

#read
print(seguidor)
print(seguidor["edad"])

if seguidor["edad"] > 18:
  print(f"{seguidor['nombre']} es mayor de edad")

#update
seguidor["edad"] = 30
print(seguidor)

#delete
del seguidor["ciudad"]
print(seguidor)

print("Claves:", seguidor.keys())
print("Valores:", seguidor.values())

for key in seguidor:
  print(key, seguidor[key])

for key, value in seguidor.items():
  print(key, value)

