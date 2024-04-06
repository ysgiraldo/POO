'''
Crear
Clase -> Estudiante
Atributos -> nombre, edad, grado
Método -> estudiar() -> imprime 'Estudiando...'

Para instancias crear un objeto Estudiante y usar el método estudiar(), 
además este debe interactuar con el usuario para que el usuario pueda ingresar 
los datos del estudiante. Se debe pedir nombre, edad y grado.Luego instanciar 
esta clase y mostrar los datos de la clase creada.

Al escribir "estudiar" utilizar el método estudiar(), indistinto de mayúsculas o minúsculas.
'''

class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

estudiante1 = Estudiante('Pedro',23,3)
print(estudiante1.nombre)