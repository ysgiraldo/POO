'''
El principio de abierto/cerrado nos dice que una clase deberia estar abierta
para la extension pero cerrada para la modificacion, es decir, deberiamos
poder agregar nuevas funcionalidades sin tener que cambiar el codigo fuente
de esta clase o de las entidades como tal. 
'''
#programa extensible
class Notificador:
    def __init__(self,usuario,mensaje):
        self.usuario = usuario
        self.mensaje = mensaje

    def notificar(self):
        raise NotImplementedError
    
class NotificadorEmail(Notificador):
    def Notificador(self):
        print(f"Enviando mensaje a {self.usuario.email}")

class NotificadorEmail(Notificador):
    def Notificador(self):
        print(f"Enviando SMS a {self.usuario.sms}")

class NotificadorEmail(Notificador):
    def Notificador(self):
        print(f"Enviando whatsapp a {self.usuario.whatsapp}")

class NotificadorEmail(Notificador):
    def Notificador(self):
        print(f"Enviando Twitter a {self.usuario.twitter}")