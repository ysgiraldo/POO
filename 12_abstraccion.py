'''
La abstraccion es manejar la complejidad al ocultar detalles innecesarios al programador o al usuario y 
mostrar solo los detalles necesarios(se da las funcionalidades relevantes). En programación orientada a 
objetos, la abstracción es un concepto fundamental que permite modelar ideas del mundo real en una forma 
que pueda ser implementada en un programa de computadora.

Se crea una interfaz simple que oculte la interfaz compleja y proporciona al usuario solo los detalles necesarios
para interactuar con el objeto. La abstracción se logra a través de la encapsulación, que es el proceso de
ocultar los detalles de implementación de un objeto y exponer solo los métodos y atributos necesarios para
interactuar con él.
'''

class Auto():
    def __init__(self):
        self._estado = 'apagado'

    def encender(self):
        self._estado = 'encendido'
        print('el auto esta encendido')
    
    def conducir(self):
        if self._estado == 'apagado':
            self.encender()
        print('Conduciendo el auto')

mi_auto = Auto()
mi_auto.conducir()

'''
En este caso, la abstracción te permite interactuar con el auto sin tener que preocuparte por los 
detalles de cómo se enciende o se conduce el auto. Estos detalles están "abstraídos" detrás de los 
métodos encender y conducir.

En el código que proporcionaste, la clase Auto es un buen ejemplo de abstracción. La clase Auto tiene 
un atributo _estado y dos métodos encender y conducir. Los detalles de cómo se implementan estos métodos 
están ocultos. Cuando creas un objeto Auto y llamas al método conducir, no necesitas saber qué está 
sucediendo internamente. Solo necesitas saber que al llamar a conducir, el auto se encenderá si está apagado 
y luego se conducirá.
'''

class Computadora:
    def __init__(self):
        self._estado = 'apagada'

    def encender(self):
        self._estado = 'encendida'
        print('La computadora está encendida')

    def apagar(self):
        self._estado = 'apagada'
        print('La computadora está apagada')

    def reiniciar(self):
        if self._estado == 'encendida':
            self.apagar()
            self.encender()
        else:
            print('La computadora ya está apagada')

mi_computadora = Computadora()
mi_computadora.reiniciar()