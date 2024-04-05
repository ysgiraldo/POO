'''
una clase debe tener una y solo una razon para cambiar.
cada clase tiene que tener una unica responsabilidad o tarea
'''

class TanqueDeCombustible:
    def __init__(self):
        self.combustible = 100

    def agregar_combustible(self, cantidad):
        self.combustible += cantidad
    
    def obtener_combustible(self):
        return self.combustible
    
    def usar_combustible(self,cantidad):
        self.combustible -= cantidad

class Auto():
    def __init__(self, tanque):
        self.posicion = 0
        self.tanque = tanque

    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2) 
            print('Has movido el auto exitosamente')
        else:
            print('No hay suficiente combustible')

    def obtener_posicion(self):
        return self.posicion

tanques = TanqueDeCombustible()
autito = Auto(tanques)

print(autito.obtener_posicion())
autito.mover(10)
print(autito.obtener_posicion())
autito.mover(20)
print(autito.obtener_posicion())
autito.mover(60)
print(autito.obtener_posicion())
autito.mover(100)
print(autito.obtener_posicion())
autito.mover(1)
print(autito.obtener_posicion())

