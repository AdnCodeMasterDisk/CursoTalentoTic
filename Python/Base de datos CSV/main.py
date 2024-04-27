import csv

def guardar_clientes(clientes):
    with open('/Users/daniel/Downloads/ejercicios clase programacion /Python/Base de datos CSV/ clientes.csv', mode='w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow(['NIT', 'Nombre', 'Direccion', 'Telefono', 'Correo', 'Preferencial'])
        for nit, datos in clientes.items():
            escritor_csv.writerow([nit, datos['nombre'], datos['direccion'], datos['telefono'], datos['correo'], datos['preferencial']])

def cargar_clientes():
    clientes = {}
    try:
        with open('/Users/daniel/Downloads/ejercicios clase programacion /Python/Base de datos CSV/ clientes.csv', mode='r') as archivo_csv:
            lector_csv = csv.DictReader(archivo_csv)
            for fila in lector_csv:
                nit = fila['NIT']
                datos = {'nombre': fila['Nombre'], 'direccion': fila['Direccion'], 'telefono': fila['Telefono'], 'correo': fila['Correo'], 'preferencial': fila['Preferencial']}
                clientes[nit] = datos
    except FileNotFoundError:
        print("El archivo clientes.csv no existe. Se creará uno nuevo.")
    return clientes

def main():
    clientes = cargar_clientes()
    while True:
        opcion = input("Seleccione una opción:\n1. Añadir cliente\n2. Eliminar cliente\n3. Mostrar cliente\n4. Listar todos los clientes\n5. Listar clientes preferenciales\n6. Terminar\n")
        if opcion == '1':
            # Añadir cliente
            nit = input("Ingrese el NIT del cliente: ")
            nombre = input("Ingrese el nombre del cliente: ")
            direccion = input("Ingrese la dirección del cliente: ")
            telefono = input("Ingrese el teléfono del cliente: ")
            correo = input("Ingrese el correo del cliente: ")
            preferencial = input("¿Es cliente preferencial? (S/N): ").upper() == 'S'
            clientes[nit] = {'nombre': nombre, 'direccion': direccion, 'telefono': telefono, 'correo': correo, 'preferencial': preferencial}
            guardar_clientes(clientes)
            print("Cliente añadido exitosamente.")
        elif opcion == '2':
            # Eliminar cliente
            nit = input("Ingrese el NIT del cliente que desea eliminar: ")
            if nit in clientes:
                del clientes[nit]
                guardar_clientes(clientes)
                print("Cliente eliminado exitosamente.")
            else:
                print("El NIT ingresado no corresponde a ningún cliente.")
        elif opcion == '3':
            # Mostrar cliente
            nit = input("Ingrese el NIT del cliente que desea mostrar: ")
            if nit in clientes:
                print("Datos del cliente:")
                print(f"NIT: {nit}")
                for clave, valor in clientes[nit].items():
                    print(f"{clave.capitalize()}: {valor}")
            else:
                print("El NIT ingresado no corresponde a ningún cliente.")
        elif opcion == '4':
            # Listar todos los clientes
            print("Listado de todos los clientes:")
            for nit, datos in clientes.items():
                print(f"NIT: {nit}, Nombre: {datos['nombre']}")
        elif opcion == '5':
            # Listar clientes preferenciales
            print("Listado de clientes preferenciales:")
            for nit, datos in clientes.items():
                if datos['preferencial']:
                    print(f"NIT: {nit}, Nombre: {datos['nombre']}")
        elif opcion == '6':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
