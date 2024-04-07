# polimorfismo de coercion -> es la capacidad de una clase de 
# tener varios metodos con el mismo nombre pero con diferente parametros

# El polimorfismo de coerción es la transformación directa de 
# un tipo en otro . Ocurre cuando un tipo se convierte en otro tipo.

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