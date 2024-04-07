''' es un concepto que hace referencia a poder mandar un mensaje sintactico a diferentes objetos,
el mensaje es el mismo pero el resultado seria distinto por sus propiedades 

multiples formas --> poli morfismo --> muchas formas
'''
# en otros lenguajes se necesita una herencia
# en python esto no se hace necesario ya que es un lenguaje tipado dinamico
class Animal():
    def sonido(self):
        pass

    # polimorfismo de sobrecarga -> permite crear una clase pero depende 
    # de los parametros se comporte de una forma u otra
    '''polimorfismo de sobrecarga -> es la capacidad de una clase 
    de tener varios metodos con el mismo nombre pero con diferente parametros'''
    def sonido(self, nombre):
        pass
    def sonido(self, nombre, edad):
        pass

class Gato(Animal):
    def sonido(self):
        return 'Miau'

class Perro(Animal):
    def sonido(self):
        return 'Guau'
    
def hacer_sonido(animal):
    print(animal.sonido())

gato = Gato()
perro = Perro()

print(gato.sonido())
print(perro.sonido())

hacer_sonido(gato) # otra forma de polimorfismo

'''
INVESTIGAR

- Duck typing -> es un estilo de programación en el que un objeto,
método o función se comporta de acuerdo a su interfaz,
es decir, a los métodos y atributos que define.
Esto es en lugar de su tipo o clase. Se enfoca en lo que
hace un objeto, en lugar de lo que es. (Ver ejemplo en 7-1_duck_typing.py)


- Enlaces dinámicos -> se le da prioridad a uno o al otro
- Enlaces estáticos -> se refiere a la resolución de llamadas a 
métodos en tiempo de compilación, basándose en el tipo declarado de 
la variable. Esto significa que la implementación del método se determina 
en tiempo de compilación y no puede cambiar durante la ejecución del programa.


- Tipo real -> origen de todo
- Tipo declarado -> origen de la variable

el polimorfismo permite estandarizar la llamada de metodos, ademas, hacer unas
clases mas flexibles, mas versatiles, que sean extensibles

'''