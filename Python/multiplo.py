numero1 = float(input("Numero 1"))
numero2 = float(input("Numero 2"))

mayor = max(numero1, numero2)
menor = min(numero1, numero2)

if mayor % menor == 0 :
    print("El mayor numero que es: ", int(mayor) , " es multimplo del menor numero que es:" , int(menor))
else:
    print("El mayor numero que es: ", int(mayor) , " no es multimplo del menor numero que es:" , int(menor))
