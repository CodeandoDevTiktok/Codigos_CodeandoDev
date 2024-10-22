from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Direcciones(Enum):
    NORTE = 'Norte'
    SUR = 'Sur'
    ESTE = 'Este'
    OESTE = 'Oeste'

# Acceso a los valores del enum
print(Color.RED.value)
print(Direcciones.NORTE.value)