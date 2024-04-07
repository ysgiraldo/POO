'''
encapsulamiento es una forma de proteger los datos de una clase,
es decir, no se puede acceder a ellos directamente desde fuera de la clase.
- atributos privados -> se accede a ellos mediante metodos
- atributos muy privados -> se accede a ellos mediante metodos
- atributos protegidos -> se accede a ellos mediante metodos

permite a la legibilidad del codigo, a la funcionalidad
--> proteger los elementos de una clase
'''
# atributo privado
class MiClase:
    def __init__(self):
        self._atributo_privado = 'Valor'

    def _hablar(self):
        print('Hola, como estass')

objeto = MiClase()
print(objeto._atributo_privado)

# atributo muy privado
class MiClase:
    def __init__(self):
        self.__atributo_privado = 'Valor'

    def _hablar(self):
        print('Hola, como estass')

objeto = MiClase()
print(objeto.__atributo_privado)

'''
El encapsulamiento es un principio fundamental de la programación orientada 
a objetos (OOP). Se refiere a la idea de ocultar los detalles internos de cómo 
se implementa un objeto, y solo exponer métodos (funciones) y propiedades (variables) 
que sean seguros y necesarios para interactuar con ese objeto.

El encapsulamiento permite agrupar datos (atributos) y los métodos que operan sobre estos 
datos en una sola unidad, que es la clase. Esto ayuda a mantener la integridad de los datos 
al prevenir el acceso directo a ellos, y permite cambiar la implementación interna de la 
clase sin afectar a otras partes del código que usan la clase.

En Python, los atributos y métodos privados se denotan con un guion bajo _ antes del nombre, y 
los muy privados con dos guiones bajos __. Sin embargo, Python no tiene una forma estricta de 
hacer que los atributos o métodos sean completamente privados, es más una convención que una regla estricta.
'''

# Ejemplo de encapsulamiento
class MiClase:
    def __init__(self):
        self._atributo_privado = 'Valor privado'  # atributo privado
        self.__atributo_muy_privado = 'Valor muy privado'  # atributo muy privado

    # Método getter para el atributo privado
    def get_atributo_privado(self):
        return self._atributo_privado

    # Método setter para el atributo privado
    def set_atributo_privado(self, valor):
        self._atributo_privado = valor

    # Método getter para el atributo muy privado
    def get_atributo_muy_privado(self):
        return self.__atributo_muy_privado

    # Método setter para el atributo muy privado
    def set_atributo_muy_privado(self, valor):
        self.__atributo_muy_privado = valor


objeto = MiClase()

# Acceder al atributo privado
print(objeto.get_atributo_privado())  # Imprime: 'Valor privado'
objeto.set_atributo_privado('Nuevo valor privado')
print(objeto.get_atributo_privado())  # Imprime: 'Nuevo valor privado'

# Acceder al atributo muy privado
print(objeto.get_atributo_muy_privado())  # Imprime: 'Valor muy privado'
objeto.set_atributo_muy_privado('Nuevo valor muy privado')
print(objeto.get_atributo_muy_privado())  # Imprime: 'Nuevo valor muy privado'

'''
En este ejemplo, la clase MiClase tiene dos atributos: _atributo_privado y __atributo_muy_privado.
Ambos atributos son privados, pero el segundo es muy privado, ya que tiene dos guiones bajos antes del nombre.

En este código, los métodos 
get_atributo_privado, 
set_atributo_privado, 
get_atributo_muy_privado y 
set_atributo_muy_privado 
son los métodos getter y setter para los atributos privado y muy privado, respectivamente. 
Estos métodos permiten acceder y modificar los atributos de manera controlada.
'''