'''
Es una clase que no podemos instanciar, es como una clase de plantilla para
poder crear clases a traves de esta. Se puede definir metodos abstractos
que deben ser implementados por las subclases.

RECORDAR -> instanciar una clase es crear un objeto a partir de una clase, ej: carro = Auto()

- implementar un metodo -> significa como va a funcionar, definir el conjunto de instrucciones
que va a realizar un metodo
- metodo abstracto -> es un metodo que esta declarado en esta clase abstracta pero no tiene 
ninguna implementacion.

sirve para crear diferentes implementaciones pero tener una plantilla unica

cuando se define una clase como abstracta se esta definiendo una clase de contrato
se esta obligando que tenga los metodos que se puso como abstracto implementados, 
se evitan errores, fomenta el polimorfismo (se esta aseguran que todas las clases 
tengan los mismo metodos por lo tanto podrian ser usadas por todas las subclases)

Proporcionan un nivel extra de seguridad, aumenta la claridad y define un marco específico
que todas las subclases deben seguir. 
Se puede definir un metodo abstracto que debe ser implementado
por todas las subclases, si no se implementa se generara un error.
'''

from abc import ABC, abstractmethod, abstractclassmethod #decorador, abc es una clase auxiliar

'''
ABC -> Abstract Base Class. Es una clase que no se puede instanciar, es una clase de plantilla
para poder crear clases a traves de esta. Se puede definir metodos abstractos que deben ser
implementados por las subclases. Es una clase auxiliar que se usa para definir una clase de una clase.
'''
class Persona(ABC): # con ABC se convierte en una clase abstracta
    @abstractmethod 
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    # @abstractclassmethod -> está en desuso
    @abstractmethod
    def hacer_actividad(self):
        pass

    def presentarse(self):
        print(f'Hola me llamo {self.nombre} y tengo {self.edad} años')

'''
Las clases abstractas sirven para tener diferente implementaciones (clases)
pero que estan en una sola plantilla. Te ayuda a evitar errores, fomenta el 
polimorfismo cuando estas asegurando que una clase sea abstracta y tenga metodos 
abstractos, estas asegurando que todas las subclases tengan los mismos metodos
y por lo tanto podrian ser usadas por todas las subclases.
'''

class Estudiante(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)

    def hacer_actividad(self):
        print(f'Estoy estudiando: {self.actividad}')


class Trabajador(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)

    def hacer_actividad(self):
        print(f'Actualmento estoy trabajando en: {self.actividad}')


# Instancias de la clase
dalto = Estudiante('Sofia',21,'Femenino','Programacion')
pedrito = Trabajador('Pedro',25,'Masculino','Programacion')

dalto.presentarse()
dalto.hacer_actividad()
pedrito.presentarse()
pedrito.hacer_actividad()