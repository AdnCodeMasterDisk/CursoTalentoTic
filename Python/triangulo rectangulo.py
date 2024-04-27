altura = int(input("ingresa un numero que sera omado como la altura del trinagulo"))

for i in range(altura, 0, -1):
    for j in range (i, 0, -2):
        print ( j, end= " ")
    print()