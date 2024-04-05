# method resolution order MRO
# el orden en el que python busca metodos y atributos en las clases 

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

# D > B > C > A
# D > B > A > C > F
d = D()
d.hablar()
F.hablar(D()) # esta llamando la clase y el objeto
A.hablar(d)
print(D.mro()) # orden de clases que se ejecutan

