# son los metodos con los que se puede acceder a las propiedades de las clases privadas
# getters: obtener el valor de una propiedad
# setters: cambiar el valor de una propiedad

# Propiedades privadas
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

# Cambiamos el nombre
dalto.set_nombre('Jacob')

# Mostramos el nuevo nombre
nombre = dalto.get_nombre()
print(nombre)

# Propiedades muy privadas
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self._edad = edad # No es necesario __edad

    def get_nombre(self):
        return self.__nombre

# Cambiamos el nombre
dalto = Persona('Sofia',21)
# Traemos el nombre
nombre = dalto.get_nombre()
print(nombre)
# print(dalto.__nombre) # no me lo muestra directamente

# Ejemplo de getters y setters
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self.edad = edad  # Usamos el setter aquí

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad > 0:
            self._edad = nueva_edad
        else:
            raise ValueError("La edad debe ser un número positivo")

persona = Persona('Sofia', 21)
print(persona.nombre)  # Imprime: 'Sofia'
print(persona.edad)  # Imprime: 21

# Cambiamos el nombre
persona.nombre = 'Jacob'
print(persona.nombre)  # Imprime: 'Jacob'

# Cambiamos la edad
persona.edad = 22
print(persona.edad)  # Imprime: 22

# Intentamos establecer una edad negativa
try:
    persona.edad = -1
except ValueError as e:
    print(e)  # Imprime: 'La edad debe ser un número positivo'