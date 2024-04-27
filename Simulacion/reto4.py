def decimal_a_binario(decimal):
    if decimal == 0:
        return '0'
    binario = ''

    while decimal > 0:
        residuo = decimal % 2
        binario = str(residuo) + binario
        decimal //= 2
    
    return binario

numero = int(input())

numeroBin = decimal_a_binario(numero)

print(f"El numro binario es {numeroBin}")


