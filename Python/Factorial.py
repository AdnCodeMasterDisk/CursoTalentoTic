import math

while True:
    numero = int(input("Ingrese un numero que sa mayor que 0 y menor que 20 para calcular su factor"))
    if 0 < numero < 20:
        break
    else:
        print("El nùmero no se encuentra en el rango necesario")

factorizar = math.factorial(numero)

print ("El factor de" , int(numero) , "es:", factorizar)

