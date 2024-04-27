totaldecompras = 0

while True:
    compra = float(input("Ingresa tu compra, si quieres saber el valor total ingresa '0' "))

    if compra < 0:
        print("El valor de la compra no puede ser negativo")
        continue

    if compra == 0:
        break

    totaldecompras += compra

print("El valor total de tus compras es de: ${:,.0f}".format(totaldecompras))
