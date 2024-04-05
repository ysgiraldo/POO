# uno de los pilares fundamentales del POO
# permite a la clase hija acceder a todos los metodos y las propiedades de la clase padre

class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre= nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print('Hola, estoy hablando un poco')

# clase hija
# herencia simple
class Empleado(Persona):
    # pass # no hace nada
    def __init__(self,nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario

    # def hablar(self):
    #     print('NO')

persona = Empleado('Roberto',43,'colombiano', 'Programador', 100000)
print(persona.salario)
persona.hablar()