empleados = int(input("Numero de empleados"))
empleados_100_300 = 0
empleados_mas_300 = 0
importe_total = 0

for i in range(1, empleados + 1):
    sueldo = float(input(f"Ingresa el valor del salario para el empleado: {i}"))
    importe_total += sueldo

    if 1000000 <= sueldo <= 3000000:
        empleados_100_300 += 1

    elif sueldo > 300 :
        empleados_mas_300 += 1

print("Tienes una nomina de: ", int(empleados), "y tu nomina es de ${:,.0f}".format(importe_total))
print("Tienes un número de: " , int(empleados_100_300), "que ganan entre $1'000.000 y $3'000.000")   
print("Tienes un número de: " , int(empleados_mas_300), "que ganan más de $3'000.000")   