class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        return "¡Guau!"
    

perro = Perro("Firulais")

print(perro.nombre + ": " + perro.hablar())