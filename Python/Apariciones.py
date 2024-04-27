def cuatasveces(frase):
    palabras = frase.lower().split()
    apariciones = {}
    for palabra in palabras:
        if palabra in apariciones:
            apariciones[palabra] += 1
        else:
            apariciones[palabra] = 1
    return apariciones

frase = input("ingresa una frase")
resultado = cuatasveces(frase)
print(resultado)
    