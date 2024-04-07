# Decorador property
'''
property: es un decorador que permite encapsular una propiedad, es decir, 
permite que una propiedad no sea accesible desde fuera de la clase, pero 
si se puede acceder a ella a través de un método.

El decorador property se usa para definir métodos getter, setter y deleter, es decir,
métodos que se ejecutan al intentar acceder, modificar o eliminar una propiedad de un objeto.

RECORDAR -> permite que los atributos sean de una clase sean privados, pero se puedan acceder a través de métodos.

@property, @nombre.setter, @nombre.deleter
'''

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

dalto.nombre = 'Pepe'

nombre = dalto.nombre
print(nombre)

del dalto.nombre
# nombre = dalto.nombre
print('Prueba de que funciona del')

# se encapsula todo el transfondo, es decir, se oculta todo el procedimiento
# se puede ocultar el nombre real de la variable
# permite tener una propiedad encapsula y que al desarrolador le sea más dificil modificarlo


'''
El polimorfismo es un principio fundamental de la programación orientada a objetos (OOP) que 
permite que un objeto pueda tomar muchas formas. En términos más simples, el polimorfismo permite 
que una interfaz única represente a una clase general de acciones.

La sobrecarga de métodos es una característica de algunos lenguajes de programación que permite 
crear varios métodos con el mismo nombre pero con diferentes parámetros. Dependiendo de los argumentos 
proporcionados al llamar al método, se seleccionará y ejecutará la versión correcta del método.

Sin embargo, es importante mencionar que Python no soporta la sobrecarga de métodos en el sentido 
tradicional. No puedes definir múltiples métodos con el mismo nombre y diferentes números o tipos 
de parámetros como en otros lenguajes como Java o C++. En Python, si defines múltiples métodos con 
el mismo nombre, el último sobrescribirá a los anteriores.

Aunque Python no soporta la sobrecarga de métodos directamente, puedes lograr un comportamiento similar 
usando argumentos con valores por defecto, argumentos variables o la inspección de los argumentos proporcionados.
'''