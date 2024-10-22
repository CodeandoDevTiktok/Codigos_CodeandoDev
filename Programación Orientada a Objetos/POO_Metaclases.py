from dataclasses import dataclass

@dataclass
class Persona:
    nombre: str
    edad: int
    profesion: str

# Crear una instancia de la clase Persona
persona = Persona("Juan", 30, "Ingeniero")


# Acceder a los atributos de la instancia
print(persona.nombre)     
print(persona.edad)       
print(persona.profesion)  