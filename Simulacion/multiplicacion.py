valor = float(input("Ingrese un numero por el cual va a multiplicar"))

while True:
    entrada = input( f"Ingrese un numero para multiplicarlo por {valor} o escribea 'x' para salir")

    if entrada == 'x':
        print('Adios...')
        break

    try:
        numero = float(entrada)
        resultado = numero * valor
        print (resultado)

    except:
        print("El numero ingresado no es correcto")