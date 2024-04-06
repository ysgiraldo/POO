'''
permite a la legibilidad del cosigo, a la funcionalidad
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
        self.__satributo_privado = 'Valor'

    def _hablar(self):
        print('Hola, como estass')

objeto = MiClase()
print(objeto.__atributo_privado)