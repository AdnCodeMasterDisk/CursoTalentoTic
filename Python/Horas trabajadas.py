horas = float(input("Cuntas Horas trabajaste?"))
valor = float(input("Cuanto vale tu hora de trabajo?"))

calculo = horas * valor

print("Tu pago es de: ${:,.0f}".format(calculo))