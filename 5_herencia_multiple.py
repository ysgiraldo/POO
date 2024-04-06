'''Hereda varias clases a la vez, se hereda de izquierda a derecha, 
si hay metodos iguales se toma el de la primera clase que se hereda'''
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre= nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print('Hola, estoy hablando un poco')

class Artista:
    def __init__(self,habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        return (f'Mi habilidad es: {self.habilidad}')

class EmpleadoArtista(Persona, Artista):
    # pass # no hace nada
    def __init__(self,nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self,nombre, edad, nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario = salario
        self.empresa = empresa

    def presentarse(self):
        # return f'{self.mostrar_habilidad()}'
        # return f'{super().mostrar_habilidad()}'
        print(f'Hola soy: {self.nombre}, {self.mostrar_habilidad()} y trabajo en {self.empresa}')


persona = EmpleadoArtista('Roberto',43,'colombiano', 'Bailar', 100000, 'Google')
persona.presentarse()
# persona = Artista('Cantar')


herencia = issubclass(EmpleadoArtista, Persona) # EmpleadoArtista es una subclase de Persona
instancia = isinstance(persona, Artista) # Permite ver si un objeto es una instancia de una clase, en este caso Artista
print(instancia)
