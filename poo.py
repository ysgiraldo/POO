class Personaje:

    # metodo
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
    
    def atributos(self):
        print(self.nombre, ':', sep='')
        print('Fuerza:', self.fuerza)
        print('Inteligencia:', self.inteligencia)
        print('Defensa:', self.defensa)
        print('Vida:', self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
    
    def esta_vivo(self):
        return self.vida>0
        
mi_personaje = Personaje('Bitboss',10,1,5,100) # Constructor
# print(mi_personaje)
# print(mi_personaje.nombre) 
mi_personaje.atributos()
mi_personaje.subir_nivel(1,2,0)
mi_personaje.atributos()