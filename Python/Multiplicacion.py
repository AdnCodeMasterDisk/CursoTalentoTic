multiplicacion = 1

while True:
    numero = int(input("Ingrese un número entero menor que 10 (0 para terminar): "))
    
    if numero >= 10:
        break
    
    if numero < 0 or numero >= 10:
        print("El número debe ser entero y menor que 10. Inténtalo de nuevo.")
        continue
    
    multiplicacion *= numero

    print("La multiplicación hasta el momento es:", multiplicacion)

print("La multiplicación final es:", multiplicacion)
