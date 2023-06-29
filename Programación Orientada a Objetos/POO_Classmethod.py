class MiClase:
    contador = 0

    @classmethod
    def incrementar_contador(cls):
        cls.contador += 1

    def __init__(self, nombre):
        self.nombre = nombre
        MiClase.incrementar_contador()

# Crear objetos
objeto1 = MiClase("Objeto 1")
objeto2 = MiClase("Objeto 2")

print("Contador:", MiClase.contador)  