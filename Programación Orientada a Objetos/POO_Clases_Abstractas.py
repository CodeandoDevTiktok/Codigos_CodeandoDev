from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.14159 * self.radio * self.radio
    
# Intentar instanciar una clase abstracta genera un error
# figura = Figura()  # Generaría un TypeError

rectangulo = Rectangulo(5, 3)
print(rectangulo.calcular_area())  # Resultado: 15

circulo = Circulo(4)
print(circulo.calcular_area())  # Resultado: 50.26544