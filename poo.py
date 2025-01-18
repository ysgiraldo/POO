class Personaje:
    nombre="Default"
    fuerza=0
    inteligencia=0
    defensa=0
    vida=0

    # metodo
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

mi_personaje = Personaje('Bitboss',10,1,5,100) # Constructor
print(mi_personaje)
print(mi_personaje.nombre) 