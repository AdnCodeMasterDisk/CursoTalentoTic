valor = float(input("Cual es el valor del producto que quieres vender?"))
igv = valor * 0.19

print("El ingreso genral a las ventas por de tu producto es ${:,.0f}".format(igv) , "asi que puedes vender tu producto en: ${:,.0f}".format(valor + igv) )