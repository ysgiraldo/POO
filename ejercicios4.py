# Analisis de sentimiento -- EJERCICIO FINAL
'''
Realizar un chatbot en python que nos pida que le digamos algo y tome
eso que le decimos, analice el sentimiento y nos responda cual es el sentimiento
'''

from textblob import TextBlob

class AnalizadorDeSentimientos:
    def analizar_sentimiento(self,texto):
        analisis = TextBlob(texto)
        if analisis.sentiment.polarity > 0:
            return 'Positivo'
        elif analisis.sentiment.polarity == 0:
            return 'Neutral'
        else:
            return 'Negativo'

analizador = AnalizadorDeSentimientos()
resultado = analizador.analizar_sentimiento('Hello its me') # La libreria entiende ingles
print(resultado)

# otra forma de hacerlo con pago de api en chatgpt
# import openai
# openai.api_key = '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'
# system_rol = '''Hace de cuenta que sos un analizador de sentimientos.
#                  Yo te paso sentimientos y vos analizas el sentimiento de 
#                  de los mensajes y me das una respuesta con al menos 1 caracter y
#                  como máximo 4 caracteres SOLO RESPUESTAS NÚMERICAS. Donde -1 es negatividad
#                  máxima, 0 es neutral y 1 es positividad máxima. 
#                  Podes ir entre esos rango, es decir 0.3, -0.5 etc tambien son validos
#                  (Podés solo responder con ints o floats)'''

# mensajes = [{"role":"system",
#              "content" : system_rol}]

# class AnalizadorDeSentimientos:
#     def analizar_sentimientos(self, polaridad):
#         if polaridad > -0.6 and polaridad <= -0.3:
#             return "\x1b[1;31m" + "Negativo" +"\x1b[0;37m" # es para poder darle un color al texto, a la consola
#         elif polaridad > -0.3 and polaridad < -0.1:
#             return "\x1b[1;31m" + "Algo negativo" +"\x1b[0;37m"
#         elif polaridad >= -0.1 and polaridad <= 0.1:
#             return "\x1b[1;33m" + "Neutral" +"\x1b[0;37m"
#         elif polaridad > 0.1 and polaridad <= 0.4:
#             return "\x1b[1;32m" + "Algo positivo" +"\x1b[0;37m"
#         elif polaridad >= 0.4 and polaridad <= 0.9:
#             return "\x1b[1;32m" + "Positivo" +"\x1b[0;37m"
#         elif polaridad > 0.9:
#             return "\x1b[1;32m" + "Muy positivo" +"\x1b[0;37m"
#         else:
#             return "\x1b[1;31m" + "Muy negativo" + "\x1b[0;37m"
        
# analizador= AnalizadorDeSentimientos()
# print(analizador)
# # resultado = analizador.analizar_sentimientos(0.95)
# # print(resultado)

# while True:
#     user_prompt = input ("\x1b[1;33m" + "\n Decime Algo:" + "\x1b[0;37m")
#     mensajes.append({"role":"user", "content":user_prompt})

#     completion = openai.ChatCompletion.create(
#         model = "got-3.5-turbo",
#         menssages = mensajes,
#         max_tokens = 8
#     )

#     respuesta = completion.choices[0].message["content"]

#     mensajes.append({"role":"assistant",
#                      "content": respuesta})
    
#     sentimiento = analizador.analizar_sentimientos(float(respuesta))
#     print(sentimiento)
    

# print("\x1b[1;31m" + "Hola")
# \x1b[1;31m rojo
# \x1b[1;32m verde
# \x1b[1;33m amarillo
# "\x1b[0;37m" blanco