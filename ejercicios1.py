class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

estudiante1 = Estudiante('Pedro',23,3)
print(estudiante1.nombre)

# para que el usuario interactue
class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print('Estudiando...')
    

nombre = input('Digame su nombre:')
edad = int(input('Ahora su edad:'))
grado = input ('Por último, su grado:')

estudiante = Estudiante(nombre, edad, grado)
print(f'''
        DATOS DEL ESTUDIANTE \n \n
        Nombre: {estudiante.nombre} \n
        Edad: {estudiante.edad} \n
        Grado: {estudiante.grado} \n
    '''
    )

while True:
    estudiar = input()
    if (estudiar.lower() == 'estudiar'):
        estudiante.estudiar()
        break