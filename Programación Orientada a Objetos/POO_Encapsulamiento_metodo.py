class MiClase:
    def __metodo_privado(self):
        print("Método privado")

    def metodo_publico(self):
        print("Método público")
        self.__metodo_privado()

objeto = MiClase()
# Salida: "Método público" y "Método privado"
objeto.metodo_publico()  
# Generaría un error
objeto.__metodo_privado()  
