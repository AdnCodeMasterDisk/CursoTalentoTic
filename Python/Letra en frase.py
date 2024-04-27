letra = input("Ingresa una letra")
frase = input("Ingresa una frase")

contador = 0

for caracter in frase:
    if caracter == letra:
        contador += 1

print("Tu frase tiene un nùmero de" , int(contador) , "dela bocal" , letra )