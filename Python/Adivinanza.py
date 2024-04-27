import random

def adivinanza():
    numero_ramdom = random.randint(1, 10)
    intentos = 0

    while True:
        intento = int(input("Ingresa un número entre 1 a 10"))
        intentos += 1

        if numero_ramdom == intento:
            print("Felicidades adivinaste el numero")
            break
        elif intento < numero_ramdom:
            print ("El numero segreto es mayor al numero que ingresaste")
        else:
            print("El numero segreto es menor al numero que ingresaste")    

adivinanza()


