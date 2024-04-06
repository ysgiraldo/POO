# son los metodos con los que se puede acceder a las propiedades de las clases privadas

class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, new_nombre):
        self._nombre = new_nombre


dalto = Persona('Sofia',21)
print(dalto._nombre)

dalto.set_nombre('Jacob')

nombre = dalto.get_nombre()
print(nombre)

# completamente privado
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre

dalto = Persona('Sofia',21)

nombre = dalto.get_nombre()
print(nombre)
# print(dalto.__nombre) # no me lo muestra directamente