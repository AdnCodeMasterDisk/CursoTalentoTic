opcion = input("Escribe 't' o 'T' si quieres saber el area de un triangulo o escrive 'o' o 'O' si quieres saber el area de un circulo")

if opcion.lower() == "t":
    base = float(input("Escribe la longitud de la base de tu tringulo"))
    altura = float(input("Escribe la longitud de la artura de tu tringulo"))

    area = 0.5 * base * altura

    print("El area de tu triingulo es: " , int(area))

elif opcion.lower() == "c":
    radio = float(input("Cual es el Area de tu circulo?"))

    areaCirculo = 3.1416 *  radio ** 2

    print ("El Area de tu circulo es: ", int(areaCirculo))

else:
    print("Escribe una opcion correcta, las opciones son: 't' o 'T' si quieres saber el area de un triangulo o escrive 'o' o 'O' si quieres saber el area de un circulo")