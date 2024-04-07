# 
# Juego de fusión de personajes
'''
el juego consiste en crear personajes de un juego y que estos se puedan
fusionar para formar personajes mas poderosos que tengan mas poder

para ello debemos cambiar el comportamiento del operador '+' para que cuando los
personajes se fusiones, salga un nuevo personaje con habilidades mejoradas

una posible formula es -> el promedio de las habiliades de ambos, al cuadrado

- Clase -> Personaje
- atributos -> nombre, fuerza, velocidad
- metodos -> __init__ -> inicializar los atributos de la clase
- metodos -> __repr__ -> representacion del objeto en una cadena de texto
- metodos -> __add__ -> fusionar personajes
Formulas: Promedio de las habilidades al cuadrado
'''

class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad

    def __repr__(self):
        return f'{self.nombre} (fuerza: {self.fuerza}, Velocidad: {self.velocidad})'
    
    def __add__(self, otro_pj):
        nuevo_nombre = self.nombre + '-' + otro_pj.nombre
        nueva_fuerza = round(((self.fuerza + otro_pj.fuerza)/2)**1.34)
        nueva_velocidad = round(((self.velocidad + otro_pj.velocidad)/2)**1.34)
        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)

goku = Personaje('Goku', 100,100)
vegeta = Personaje('Vegeta',99,99)
jiren = Personaje('Jiren',130,140)

gogeta = goku + vegeta + jiren
print(goku)
print(vegeta)
print(jiren)
print(gogeta)

## crear un nuevo juego en el que el usuario pueda interactuar
'''
Que muestra un menu con las siguientes opciones:
1. Crear personaje
2. Fusionar personajes
3. Mostrar personajes
4. Salir
Si elige uno se le pedira el nombre, fuerza y velocidad del personaje, después se dira que se ha creado con exito

Luego se le volveran a mostrar las opciones del menu
si elige 2 se le pedira que elija dos personajes de la lista para fusionarlos
si elige 3 se le mostraran los personajes que ha creado
si elige 4 se saldrá del juego
'''
class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
    
    personajes = []
    while True:
        print('1. Crear personaje')
        print('2. Fusionar personajes')
        print('3. Mostrar personajes')
        print('4. Salir')
        opcion = int(input('Elige una opción: '))

        if opcion == 1:
            def __repr__(self):
                return f'{self.nombre} (fuerza: {self.fuerza}, Velocidad: {self.velocidad})'
    
    def __add__(self, otro_pj):
        nuevo_nombre = self.nombre + '-' + otro_pj.nombre
        nueva_fuerza = round(((self.fuerza + otro_pj.fuerza)/2)**1.34)
        nueva_velocidad = round(((self.velocidad + otro_pj.velocidad)/2)**1.34)
        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)
