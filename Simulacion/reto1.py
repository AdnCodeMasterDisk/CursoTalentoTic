tornillo = float(input(""))

if 1 <= tornillo < 3:
    print("El tornillo es pequeno.")
elif 3 <= tornillo < 5:
    print("El tornillo es mediano.")
elif 5 <= tornillo < 6.5:
    print("El tornillo es grande.")
elif 6.5 <= tornillo < 8.5:
    print("El tornillo es muy grande.")
elif tornillo == 8.5:
    print("El tornillo es muy grande.")
elif tornillo >= 8.5:
    print("El tornillo es gigante.")
else:
    print("El tamano ingresado no es valido.")
