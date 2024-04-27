cantidad = int(input("Ingrese la cantidad de piezas que va a procesar"))

aptas = 0

for i in range (1, cantidad + 1 ):
    longitud = float(input("Ingrese la mededida de su pieza"))

    if 1.20 <= longitud <= 1.30:
        aptas += 1

print("El número de piesas aptas para tu proyecto es de:" , int(aptas))
