def agregar(base_datos) :
    nit = input("Ingrese el NIT del cliente: ")
    nombre = input("Ingrese el nombre del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    correo = input("Ingrese el correo electrónico del cliente: ")
    preferencial = input("¿Es cliente preferencial? (Sí/No): ").lower() == "sí"
    base_datos[nit] = {
        'nombre': nombre,
        'direccion': direccion,
        'telefono': telefono,
        'correo': correo,
        'preferencial': preferencial
    }
    print("Cliente agregado con Exito")

def eliminar(base_datos):
    nit = input("Ingrese el NIT del cliente a eliminar: ")
    if nit in base_datos:
        del base_datos[nit]
        print ("Cliente eliminado")
    else:
        print ("Cliente no encontrado")


def mostrar(base_datos):
    nit = input("Ingrese el NIT del cliente que quiere ver: ")
    if nit in base_datos:
        print ("Cliente:")
        print(base_datos[nit])
    else:
        print ("Cliente no encontrado")

def mostrartodos(base_datos):
    print("Listado completo de clintes:")
    for nit, datos in base_datos.items():
        print(f"NIT: {nit}, Nombre: {datos['nombre']}")

def preferenciales(base_datos):
    print("Listado completo de clintes preferenciales:")
    for nit, datos in base_datos.items():
        if datos['preferencial']:
            print(f"NIT: {nit}, Nombre: {datos['nombre']}")


def main():
    base_datos_clientes = {}
    while True:
        print("\nMenú:")
        print("1. Añadir cliente")
        print("2. Eliminar cliente")
        print("3. Mostrar cliente")
        print("4. Listar todos los clientes")
        print("5. Listar clientes preferenciales")
        print("6. Terminar")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar(base_datos_clientes)
        elif opcion == "2":
            eliminar(base_datos_clientes)
        elif opcion == "3":
            mostrar(base_datos_clientes)
        elif opcion == "4":
            mostrartodos(base_datos_clientes)
        elif opcion == "5":
            preferenciales(base_datos_clientes)
        elif opcion == "6":
            print("Programa terminado")
            break
        else:
            print("Ingrese una opcion correcta de las opciones mostradas en el menu")
            
if __name__ == "__main__":
    main()