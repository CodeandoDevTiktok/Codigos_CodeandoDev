class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def mostrar_marca(self):
        print("Marca:", self.marca)

class Coche(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca)  # Llamada al constructor de la clase base
        self.modelo = modelo

    def mostrar_info(self):
        super().mostrar_marca()  # Llamada a un método de la clase base
        print("Modelo:", self.modelo)

coche = Coche("Ford", "Fiesta")
coche.mostrar_info()