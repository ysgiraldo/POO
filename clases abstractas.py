'''
Es una clase que no podemos instanciar, es como una clase de platallia para
poder crear clases a traves de esa plantilla

implementar un metodo -> significa como va a funcionar, definir el conjunto de instrucciones
que va a realizar un metodo

sirve para crear diferentes implementaciones pero tener una plantilla unica

cuando se define una clase como abstracta se esta definiendo una clase de contrato
se esta obligando que tenga los metodos que se puso como abstracto implementados, 
se evitan errores, fomenta el polimorfismo (se esta aseguran que todas las clases 
tengan los mismo metodos por lo tanto podrian ser usadas por todas las subclases)
'''

from abc import ABC, abstractclassmethod #decorador

class Persona(ABC):
    @abstractclassmethod
    def __init__(self,nombre,edad,sexo,actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractclassmethod
    def hacer_actividad(self):
        pass

    def presentarse(self):
        print(f'Hola me llamo {self.nombre} y tengo {self.edad} años')

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


dalto = Estudiante('Sofia',21,'Femenino','Programacion')
pedrito = Trabajador('Pedro',25,'Masculino','Programacion')

dalto.presentarse()
dalto.hacer_actividad()
pedrito.presentarse()
pedrito.hacer_actividad()