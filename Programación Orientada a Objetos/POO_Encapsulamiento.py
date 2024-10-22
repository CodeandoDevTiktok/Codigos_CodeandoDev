class Coche:
    def __init__(self):
        self.__maxima_velocidad = 200

    def conducir(self):
        print('Conduciendo a v=', self.__maxima_velocidad)

mi_coche = Coche()
mi_coche.conducir()  # Esto está bien
print(mi_coche.__maxima_velocidad)  # Error