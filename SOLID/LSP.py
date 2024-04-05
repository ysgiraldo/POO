'''
las clases derivadas tienen que ser sustituibles por sus clases padre

si la clase B es una subclase de A, la clase A deberia poder utilizar en todos 
los lugares donde B pueda utilizarse
'''

# class Ave:
#     def volar(self):
#         return "Estoy volando"
    
# class Pinguino(Ave):
#     def volar(self):
#         return "No puedo volar"
    
# def hacer_volar(ave = Ave): #variable de parametro
#     return ave.volar()

# print(hacer_volar(Pinguino()))

class Ave:
    pass

class AveVoladora(Ave):
    def volar(self):
        return "Estoy volando"
    
class AveNovoladora(Ave):
    pass