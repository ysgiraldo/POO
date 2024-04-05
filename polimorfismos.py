''' es un concepto que hace referencia a poder mandar un mensaje sintactico a diferentes objetos,
el mensaje es el mismo pero el resultado seria distinto por sus propiedades 

multiples formas --> poli morfismo
'''
# en otros lenguajes se necesita una herencia
# en python esto no se hace necesario ya que es un lenguaje tipado dinamico
class Animal():
    def sonido(self):
        pass

    # polimorfismo de sobrecarga -> permite crear una clase pero depende 
    # de los parametros se comporte de una forma u otra
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

# polimorfismo de coersion
num1 = 3
num2 = 4.4

resultado = num1 + num2
print(resultado)
print(type(resultado))

def recorrer(elemento):
    for item in elemento:
        print(f'El elemento actual es: {item}')

lista = [1,2,3,4]
lista2 = ['maquina','como','andas']

recorrer(lista)
recorrer(lista2)

'''
INVESTIGAR

Duck typing

Enlaces dinámicos -> se le da prioridad a uno o al otro
Enlaces estáticos

Tipo real -> origen de todo
Tipo declarado -> origen de la variable

el polimorfismo permite estandarizar la llamada de metodos, ademas, hacer unas
clases mas flexibles, mas versatiles,s que sean extensibles
'''