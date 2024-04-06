## metodos dunder

'''
Son funciones que tienen un nombre especial reservado.
Estan creados con la unica finalidad de que nosotros podamos crear 
funcionalidades especiales que con metodos especiales no podríamos crear
'''

class Persona:
    def __init__(self,nombre,edad,):
        self.nombre = nombre
        self.edad = edad

    # representacion del objeto en una cadena de texto
    def __str__(self):
        return f'Persona(nombre={self.nombre},edad={self.edad})'
    
    def __repr__(self):
        return f'Persona("{self.nombre}",{self.edad})'
    
    #sobrecarga de operadores
    def __add__(self,otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre+otro.nombre,nuevo_valor)
    
dalto = Persona('Sofia',21)
print(dalto)
repr = repr(dalto)
resultado = eval(repr)
print(repr)
print(resultado)
print(resultado.nombre)
print(resultado.edad)

dalto = Persona('Sofia',21)
dalto2 = Persona('Pedro',24)
maria = Persona('Maria',18)

nueva_persona = dalto + dalto2 + maria
print(nueva_persona.nombre)
print(nueva_persona.edad)

