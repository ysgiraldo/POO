class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre # no queremos que acceda a esta propiedad
        self._edad = edad

    @property # decoradores
    def nombre(self):
        return self.__nombre
    
    @nombre.setter # cambiar el nombre
    def nombre(self, new_nombre):
        self.__nombre = new_nombre

    @nombre.deleter # eliminar esa propiedad
    def nombre(self):
        del self.__nombre

dalto = Persona('Sofia',21)

nombre = dalto.nombre
print(nombre)

dalto.nombre = 'Pepes'

nombre = dalto.nombre
print(nombre)

del dalto.nombre
# nombre = dalto.nombre
# print(nombre)

print('Hola')



# se encapsula todo el transfondo, es decir, se oculta todo el procedimiento

# dalto.__nombre = 'Pepes'
# nombre = dalto.nombre
# print(nombre)

# se puede ocultar el nombre real de la variable

# permite tener una propiedad encapsula y que al desarrolador le sea más dificil modificarlo