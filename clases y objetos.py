# celular1_marca = 'samsung'
# celular2_marca = 'apple'
# celular3_marca = 'huawei'

# celular1_modelo = 's23'
# celular2_modelo = 'Iphone 15 PRO'
# celular3_modelo = 'P20 pro'

# celular1_camaraT = '48MP'
# celular2_camaraT = '48MP'
# celular3_camaraT = '12MP'

# celular1_camaraF = '24MP'
# celular2_camaraF = '24MP'
# celular3_camaraF = '8MP'

'''class Celular():
    # atributo
    marca = 'Samsung'
    modelo = 'S23'
    camara = '48MP'

# objetos fijos
celular1 = Celular() # instanciar un objeto (instancia de una clase)
print(celular1.marca) # preguntar propiedades del objeto  '''

# clases que permitan crear objetos con diferentes caracteristicas
# atributos -> variables que pertencen a una clase
# atributos o propiedades de instancia -> crear un objeto

class Celular:
    # constructor
    # funcion que se ejecuta automaticamente cada vez que creamos un objeto 
    def __init__(self, marca, modelo, camara): # self -> referencia al mismo objeto
        self.marca = marca
        self.modelo = modelo 
        self.camara = camara
    # metodo
    def llamar(self):
        print(f'Estas haciendo un llamado desde un: {self.modelo}')
    
    def cortar(self):
        print(f'Cortaste la llamada desde tu: {self.modelo}')

# crear objetos
celular1 = Celular('Samsung', 'S23', '48MP')
celular2 = Celular('Apple', 'Iphone 15 pro', '96MP')
print(celular1)
celular2.llamar()
celular1.cortar()
