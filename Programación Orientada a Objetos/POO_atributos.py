class Persona:
    especie = "Humano"  # Atributo de clase

    def __init__(self, nombre):
        self.nombre = nombre  # Atributo de instancia

# Uso de los atributos
persona1 = Persona("Juan")

print(persona1.especie)  # Humano
print(persona1.nombre)  # Robot
