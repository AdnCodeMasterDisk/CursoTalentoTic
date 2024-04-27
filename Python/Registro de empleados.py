class Empleado:
    def __init__(self, nombre, salario, cargo):
        self.nombre = nombre
        self.salario = salario
        self.cargo = cargo

def agregar_emplado():
    nombre = input("Ingresa el nombre del empleado:")
    salario = float(input("Ingrese el salario de el empleado"))
    cargo = input("Ingrese el cargo del empleado")
    empleado = Empleado(nombre, salario, cargo)
    empleados.append(empleado)
    print("Empleado agregado")

def mostrar_empleados():
    if empleados:
        print("Listado de empleados:")
        for i, empleado in enumerate(empleados, start=1):
            print(f"{i}. Nombre: {empleado.nombre}, Salario: {empleado.salario}, Cargo: {empleado.cargo}")

    else:
        print("No hay empleados registados")

def menu():
    print("\nMenú:")
    print("1. Añadir empleado")
    print("2. Mostrar todos los empleados")
    print("3. Salir") 

empleados = []

while True:
    menu()
    option = input("Seleccione una opcion: ")
    if option == "1":
        agregar_emplado()
    elif option == "2":
        mostrar_empleados()
    elif option == "3":
        print ("Saliendo del programa.....")        
        break
    else:
        print("Seleccione una opcion valida")