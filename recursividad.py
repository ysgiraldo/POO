'''
EJERCICIO
Entiende el concepto de recursividad creando una función recursiva que imprima números del 100 al 0

- Calcular el factorial de un número concreto 


Recursividad -> funcion que se llama a ella misma
'''

def countdown(number: int):
    if number >= 0:
        print(number)
        countdown(number - 1)

countdown(100)
