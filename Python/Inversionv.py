inversion = float(input("Cuanto queires invertir?"))
interes = float(input("Cual es el interes que maneja la inversion"))
tiempo = int(input("Cuantos años quieres invertir"))

#Formula interes compuesto: A\=P×(1+nr​)nt 

for inversiontotal in range(1, tiempo + 1):
   capital = inversion * (1 + interes / 100 ) ** inversiontotal
   print(f"Año {inversiontotal} capital ${capital:,.0f}")
