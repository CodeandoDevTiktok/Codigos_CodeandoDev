class Instrumento:
    def tocar(self):
        print("El instrumento se toca")

class Electrico:
    def enchufar(self):
        print("El instrumento eléctrico se enchufa")

class Guitarra(Instrumento, Electrico):
    def afinar(self):
        print("Se afina la guitarra")

g = Guitarra()
g.tocar()      # Salida: El instrumento se toca
g.enchufar()   # Salida: El instrumento eléctrico se enchufa
g.afinar()     # Salida: Se afina la guitarra