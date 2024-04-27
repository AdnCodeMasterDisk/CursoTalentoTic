tamano = float(input("Cual es el tamaño de tu toormillo?"))

if 1 <= tamano <= 3:
    print("El tornillo es pequeño")
elif 3 <= tamano <= 5:
    print("El tornillo es mediano")    
elif 5 <= tamano <= 6.5:
    print("El tornillo es grande")    
elif 6.5 <= tamano <= 8.5:
    print("El tornillo es muy grande")    
else:
    print("El tornillo es enorme")    

