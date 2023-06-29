#Clase
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return print("Area:",math.pi * self.radio ** 2)

    def calcular_perimetro(self):
        return print("Perimetro:",2 * math.pi * self.radio)

#Llamar a Clase y utilizar método
Circulo(5).calcular_area()
Circulo(5).calcular_perimetro()