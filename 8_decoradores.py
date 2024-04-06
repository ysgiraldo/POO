'''
toma una funcion como entrada le agrega una funcionalidad
extra y devuelve como salida la funcion modificada

te agarra una funcion y le agrega una funciona antes o despues (o las dos)
de ejecurarla
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

'''
investigar sobre los decoradores de clase y multiples 
'''