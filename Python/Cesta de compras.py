cesta = {}

while True:
    articulo = input("Ingrese el articulo o escriba ESC para optener el valor total" )
    if articulo.upper() == "ESC":
        break
    precio = float(input("Cual es el Valor del Articulo?"))
    cesta[articulo] = precio

print("\nLista de Compras:")
total = 0

for articulo, precio in cesta.items():
    print(f"{articulo}: ${precio}")
    total += precio

print(f"\nCoste total: ${total}")