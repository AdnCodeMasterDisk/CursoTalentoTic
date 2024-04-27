primerProducto = float(input("Cual es el valor de el primer producto?"))
segundoProducto = float(input("Cual es el valor de el segundo producto?"))
tercerProducto = float(input("Cual es el valor de el tercer producto?"))

mas_costoso = max(primerProducto, segundoProducto, tercerProducto)
mas_economico = min(primerProducto, segundoProducto, tercerProducto)
promedio = (primerProducto + segundoProducto + tercerProducto) / 3

print("El producto mas costoso es: ${:,.0f}".format(mas_costoso), "El producto mas economico es: ${:,.0f}".format(mas_economico) , "El promedio es ${:,.0f}".format(promedio))