class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def mostrar_informacion(self):
        print(f"Libro: {self.titulo} - Autor: {self.autor}")

# Uso de la clase
libro1 = Libro("1984", "George Orwell")
libro1.mostrar_informacion()