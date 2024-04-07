class Pato:
    def volar(self):
        return "El pato puede volar"

class Avion:
    def volar(self):
        return "El avión puede volar"

def hacer_volar(objeto):
    print(objeto.volar())

pato = Pato()
avion = Avion()

hacer_volar(pato)  # Imprime: "El pato puede volar"
hacer_volar(avion)  # Imprime: "El avión puede volar"

'''
En este código, tienes dos clases: Pato y Avion. Ambas clases 
tienen un método llamado volar, que devuelve una cadena de texto.

Luego, tienes una función llamada hacer_volar. Esta función toma 
un objeto como argumento y llama al método volar de ese objeto.

Lo importante aquí es que la función hacer_volar no se preocupa por el 
tipo de objeto que recibe. No le importa si es un Pato o un Avion. Todo 
lo que le importa es que el objeto tenga un método volar que pueda llamar. 
Esto es lo que se conoce como "Duck Typing". Si un objeto puede hacer algo 
(como "volar" en este caso), entonces se puede usar en cualquier lugar que 
requiera esa capacidad, sin importar el tipo de objeto que sea.
'''

'''la función hacer_volar puede aceptar cualquier objeto que tenga un 
método volar. No importa si el objeto es un Pato o un Avion, siempre 
que tenga el método volar, la función hacer_volar puede usarlo. 

Esto es Duck Typing: si se ve como un pato y grazna como un pato, entonces es un pato.'''