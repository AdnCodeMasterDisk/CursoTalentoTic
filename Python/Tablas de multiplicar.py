while True:
    numero = int(input("Escribe un numero menor a 10"))

    if numero < 10 :
        break
    else:
        print("El nùmero es mayor a 10, ingresa un numero menor")

inicio = int(input("Ingresa el nùmero desde el que quieres multipliicar"))
final= int(input("Ingresa el nùmero maximo hasta el que quieres multiplicar"))

for i in range (inicio, final + 1):
    resultado = numero * i
    print(f"{numero} * {i} = {resultado}")
