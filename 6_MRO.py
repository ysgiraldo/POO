# method resolution order MRO
# el orden en el que python busca metodos y atributos en las clases 
# cuando es igual la rama de dos clases seguidas, se pondran las dos clases y luego la clase padre
# si se repite la clase, se pondra la clase una sola vez

# se utiliza la ramificacion 

# Demostración 1
class A:
    def hablar(self):
        print('Hola desde A')


class B(A):
    def hablar(self):
        print('Hola desde B')

class C(A):
    def hablar(self):
        print('Hola desde C')

class D(B,C):
    # pass
    def hablar(self):
        print('Hola desde D')

d = D()
d.hablar()

# El orden será -> D > B > C > A

# Demostración 2
class A:
    def hablar(self):
        print('Hola desde A')

class F(A):
    def hablar(self):
        print('Hola desde F')

class B(A):
    def hablar(self):
        print('Hola desde B')

class C(F):
    def hablar(self):
        print('Hola desde C')

class D(B,C):
    # pass
    def hablar(self):
        print('Hola desde D')

# El orden será -> D > B > A > C > F 
# (primero busca en toda la rama de la primera clase que se le pasa, es decir, de B es A, luego de C es F)

d = D()
d.hablar()
F.hablar(D()) # esta llamando la clase y el objeto
A.hablar(d)
print(D.mro()) # orden de clases que se ejecutan

