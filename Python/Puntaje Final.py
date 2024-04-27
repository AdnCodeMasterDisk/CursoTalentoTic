correctas = float(input("Cuantas Respuestas tienes correcta?"))
incorrectas = float (input("cuantas Respuestas tienes incorrectas?"))
blanco = float(input("cuantas respuestas tienes sin responder?"))

numeroderespuestas = correctas + incorrectas + blanco
promedio = (correctas * 3) + (incorrectas * -1) + blanco

print("Respondiste", int(numeroderespuestas), "preguntas y tu promedio fue de:", int(promedio) )