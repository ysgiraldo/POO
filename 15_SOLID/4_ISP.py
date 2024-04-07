'''
principio de segregacion de la interfaz

ningun cliente tiene que ser forzado a depender de interfacez
que no utilice, es decir, tendriamos que eliminar las dependencias 
que no vamos a utilizar
'''

from abc import ABC, abstractmethod

class Trabajador(ABC):

    @abstractmethod
    def trabajar(self):
        pass

class Comedor(ABC):
    
    @abstractmethod
    def comer(self):
        pass

class Durmiente(ABC):

    @abstractmethod
    def dormir(self):
        pass

class Humano(Trabajador, Comedor, Durmiente): 
    def comer(self):
        print('El humano esta comiendo')

    def trabajar(self):
        print('El humano esta trabajando')

    def dormir(self):
        print('El humano esta durmiendo')

class Robot(Trabajador): 
    def trabajar(self):
        print('El robot esta trabajando')

robot = Robot()
humano = Humano()
robot.trabajar()
humano.comer()