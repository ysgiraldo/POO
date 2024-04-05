# crear un sistema para una escuela

'''
Vamos a tener dos clases principales Persona y Estudiante.

Persona tendrá atributos de nombre y edad y un método que imprima el nombre y la edad de la persona
Estudiante heredará de la clase Persona y tendrá un atributo adicional, grado y un método que imprima
el grado del estudiante
'''

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def mostrar_datos(self):
        print(f'Mi nombre es {self.nombre} y mi edad es {self.edad}')


class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def mostrar_grado(self):
        print(f'Mi grado es: {self.grado}')

individuo = Estudiante('Sofia',21,'Profesional')
print(individuo.grado)
individuo.mostrar_datos()
individuo.mostrar_grado()


### Ejercicio 2.1
'''
crear tres clase animal, mamifero y ave

animal debe tomar un metodo llamado comer
mamifero debe tener un metodo llamado amamantar
ave debe tener un metodo llamado volar

crear una clase murcielago que herede de mamifero y ave , amamantar y colar además de comer
'''


class Animal:
    def comer(self):
        print('El animal está comiendo')

class Mamifero(Animal):
    def amamantar(self):
        print('El animal está amamantando')

class Ave(Animal):
    def volar(self):
        print('El animal esta volando ')


class Murcielago(Mamifero,Ave):
    pass

murcielago = Murcielago()
murcielago.comer()
murcielago.amamantar()
murcielago.volar()

print(Murcielago.mro())