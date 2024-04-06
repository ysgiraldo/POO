# Analisis de sentimiento -- EJERCICIO FINAL

import openai
openai.api_key = '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'
system_rol = '''Hace de cuenta que sos un analizador de sentimientos.
                Yo te paso sentimientos y vos analizas el sentimiento de 
                de los mensajes y me das una respuesta con al menos 1 caracter y
                como máximo 4 caracteres SOLO RESPUESTAS NÚMERICAS. Donde -1 es negatividad
                máxima, 0 es neutral y 1 es positividad máxima. 
                Podes ir entre esos rango, es decir 0.3, -0.5 etc tambien son validos
                (Podés solo responder con ints o floats)'''

mensajes = [{"role":"system",
            "content" : system_rol}]


class Sentimiento:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

    def __str__(self):
        return "\x1b[1;{}m{}\x1b[1;37m".format(self.color,self.nombre)

class AnalizadorDeSentimientos:
    def __init__(self,rangos):
        self.rangos = rangos 

    def analizar_sentimientos(self, polaridad):
        for rango, sentimiento in self.rangos:
            if rango[0] < polaridad <= rango[1]:
                return sentimiento
        return Sentimiento('Muy negativo', "31")
    
rangos = {
    ((-0.6,-0.3),Sentimiento("Negativo", "31")),
    ((-0.3,-0.1),Sentimiento("Algo negativo", "31")),
    ((-0.1,0.1),Sentimiento("Neutral", "33")),
    ((0.1,0.4),Sentimiento("Algo positivo", "32")),
    ((0.4,0.9),Sentimiento("Positivo", "32")),
    ((0.9,1),Sentimiento("Muy positivo", "32")),
}

analizador= AnalizadorDeSentimientos(rangos)

while True:
    user_prompt = input ("\x1b[1;33m" + "\n Decime Algo:" + "\x1b[0;37m")
    mensajes.append({"role":"user", "content":user_prompt})

    completion = openai.ChatCompletion.create(
        model = "got-3.5-turbo",
        menssages = mensajes,
        max_tokens = 8
    )

    respuesta = completion.choices[0].message["content"]

    mensajes.append({"role":"assistant",
                    "content": respuesta})
    
    sentimiento = analizador.analizar_sentimientos(float(respuesta))
    print(sentimiento)

'''
Hacer este mismo ejercicio con la libreria textblob y asi ya no se depende de la api paga de chatgpt
'''

# Programar para crear soluciones #