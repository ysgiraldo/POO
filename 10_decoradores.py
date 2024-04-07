# Title: Decoradores en Python
'''
toma una funcion como entrada, le agrega una funcionalidad
extra y devuelve como salida la funcion modificada, pero no cambia
el codigo original de la funcion.

te agarra una funcion y le agrega una funcionalidad antes o despues (o las dos)
de ejecutarla
'''

def decorador(funcion):
    def funcion_modificada():
        print('Antes de llamar a la función')
        funcion()
        print('Después de llamar a la función')
    return funcion_modificada

# def saludo():
#     print('Hola Sofía, como andas')

# saludo_modificado = decorador(saludo)
# saludo_modificado()

@decorador # Es lo que está arriba, esto va a realizar una funcion decorador
def saludo():
    print('Hola Sofía, como andas')

saludo()

# Las funciones tienen que ser modularizables y explicitas, encargarse de una sola funcionalidad

'''
investigar sobre los decoradores de clase y multiples, decoradores con argumento 
'''
#--------------------------------------------------------------
# Decoradores de Clase
#--------------------------------------------------------------

'''
Los decoradores de clases son una característica de Python que permite modificar o 
mejorar una clase de una manera limpia y fácil de leer. Funcionan de manera similar 
a los decoradores de funciones, pero se aplican a las clases.

Un decorador de clase toma una clase como entrada y devuelve una nueva clase que puede 
ser una versión modificada de la entrada o una clase completamente nueva.
'''

'''
En tu código, tienes un decorador de clase llamado decorador_clase. Este decorador toma 
una clase, define una nueva clase ClaseModificada que hereda de la clase de entrada, y 
luego devuelve ClaseModificada. En ClaseModificada, se sobrescribe el método __init__ 
para imprimir un mensaje antes y después de inicializar la clase.
'''

def decorador_clase(clase):
    class ClaseModificada(clase):
        def __init__(self, *args, **kwargs):
            print('Antes de inicializar la clase')
            super().__init__(*args, **kwargs)
            print('Después de inicializar la clase')
    return ClaseModificada

'''
Luego, usas este decorador en la definición de MiClase con la sintaxis @decorador_clase. 
Esto significa que MiClase se pasa al decorador y se reemplaza por la clase que devuelve el decorador.
'''
@decorador_clase
class MiClase:
    def __init__(self):
        print('Inicializando la clase')

objeto = MiClase()

# --------------------------------------------------------------
# Decoradores Multiples
# --------------------------------------------------------------
'''
Los decoradores múltiples se refieren a la aplicación de más de un decorador a 
una función o clase. Se aplican de abajo hacia arriba. Por ejemplo:

En este caso, mi_funcion se pasa primero a decorador2, y luego el resultado se pasa a decorador1.
'''

def decorador1(func):
    def envoltura():
        print("Esto se imprime antes de llamar a la función con decorador1")
        func()
        print("Esto se imprime después de llamar a la función con decorador1")
    return envoltura

def decorador2(func):
    def envoltura():
        print("Esto se imprime antes de llamar a la función con decorador2")
        func()
        print("Esto se imprime después de llamar a la función con decorador2")
    return envoltura

@decorador1
@decorador2
def mi_funcion():
    print("¡Hola, mundo!")

mi_funcion()

# Esto se imprime antes de llamar a la función con decorador1
# Esto se imprime antes de llamar a la función con decorador2
# ¡Hola, mundo!
# Esto se imprime después de llamar a la función con decorador2
# Esto se imprime después de llamar a la función con decorador1