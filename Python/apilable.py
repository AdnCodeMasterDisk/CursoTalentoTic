def es_apilable (num):
    nivel = 1
    numero_latas = num

    while numero_latas > 0:
        if numero_latas == nivel:
            return True
        elif numero_latas < 0:
            return False
        
        numero_latas -= nivel
        nivel += 1

latas_usuario = int(input("Ingrese el numero de latas"))

if es_apilable(latas_usuario):
    print("El numero de latas que mensionaste es apilable")
else:
    print("El numero de latas que mensionaste no es apilable")