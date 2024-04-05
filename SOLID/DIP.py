'''
Los modulos de alto nivel no tienen que depender de los de bajo nivel,
sino que los dos tienen que depender de las abastracciones

las abstracciones no deben depender de los detalles sino que los detalles
deben depender de las abastracciones, en otras palabras, significa que no debemos
depender de implementaciones especificas o sea de una funcion particular o de algun
codigo que haga algo sino que tenemos que depender de interfacez mas complejas de cosas mas grandes
'''

# class Diccionario:
#     def verificar_palabra(self,palabra):
#         # logica para verificar palabra
#         pass

#no deberiamos depender de diccionario
# class CorrectorOrtografico:
#     def __init__(self):
#         self.diccionario = Diccionario()

#     def corregir_texto(self,texto):
#         #usamos el diccionario para corregir el texto
#         pass

from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self):
        # logica para verificar palabra
        pass    

class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self,palabra):
        # logica para verificar palabra si esta en el diccionario
        pass

# class ServicioOnline(VerificadorOrtografico):
#     def verificar_palabra(self,palabra):
#         #logica para verificar palabra si esta en el diccionario
#         pass

class CorrectorOrtografico:    
    def __init__(self, verificador):
        self.verificador = verificador

    def corregir_texto(self,texto):
        #usamos el diccionario para corregir el texto
        pass

corrector = CorrectorOrtografico(Diccionario())
# corrector = CorrectorOrtografico(Servicioweb())