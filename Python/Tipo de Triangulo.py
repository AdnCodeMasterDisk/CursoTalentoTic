lado1 = float(input("Longitud lado 1"))
lado2 = float(input("Longitud lado 2"))
lado3 = float(input("Longitud lado 3"))

if (lado1 == lado2 == lado3):
    print("El tiengulo es equilátero")
elif(lado1 == lado2 or lado2 == lado3 or lado3 == lado1):
    print("El tiengulo es isósceles")
else:
    print("El triangulo es escaleno")        