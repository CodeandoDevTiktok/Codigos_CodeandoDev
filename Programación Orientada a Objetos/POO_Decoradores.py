def decorador(funcion):
    def wrapper():
        print("Antes de ejecutar la función")
        funcion()
        print("Después de ejecutar la función")
    return wrapper

@decorador
def saludar():
    print("Hola, soy una función decorada")

saludar()
