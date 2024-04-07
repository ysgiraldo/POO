## metodos dunder

'''
Son funciones que tienen un nombre especial reservado.
Estan creados con la unica finalidad de que nosotros podamos crear 
funcionalidades especiales que con metodos normales no podríamos crear

los metodos dunder son metodos especiales que nos permiten hacer cosas
especiales con nuestras clases, como por ejemplo, poder sumar dos objetos
de una clase que nosotros creamos, o poder imprimir un objeto de una clase
de una forma especial, o poder comparar dos objetos de una clase de una forma
especial, etc.
'''

class Persona:
    def __init__(self,nombre,edad,):
        self.nombre = nombre
        self.edad = edad

    # representacion del objeto en una cadena de texto
    def __str__(self): # devolver una representacion del objeto en una cadena de texto
        return f'Persona(nombre={self.nombre},edad={self.edad})'
    
    def __repr__(self): # actue como la representacion del objeto en una cadena de texto
        return f'Persona("{self.nombre}",{self.edad})'
    
    #sobrecarga de operadores
    def __add__(self,otro): # modificar la forma en la que se va a comportar
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre+otro.nombre,nuevo_valor)
    
dalto = Persona('Sofia',21)

repr = repr(dalto)
resultado = eval(repr)

print(repr)
print(resultado.nombre)
print(resultado.edad)

dalto = Persona('Sofia',21)
pedro = Persona('Pedro',24)
maria = Persona('Maria',18)

# se puede sumar objetos de una clase
nueva_persona = dalto + pedro + maria
print(nueva_persona.nombre)
print(nueva_persona.edad)

'''
Esto es una sobrecarga de operadores, es decir, estamos modificando la forma en la que se va a comportar
'''

