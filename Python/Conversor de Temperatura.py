def celsius_to_fahrenheit(celsius):
    return( celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return( fahrenheit - 32 ) * 5/9

def menu():
    print("1. Convertir de Celsius a Fahrenheit")
    print("2. Convertir de Fahrenheit a Celsius")
    print("3. Salir")

def main():    

    while True:
        menu()
        option = input("Elija una opcion")

        if option == "1":
            celsius = float(input("Ingrese la temperatura en celsius:"))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius} grados Celsius equivalen a {fahrenheit} grados Fahrenheit.\n")
        
        elif option == "2":
            fahrenheit = float(input("Ingrese la temperatura en fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit} grados Fahrenheit equivalen a {celsius} grados Celsius.\n")
            
        
        elif option == "3":
            print ("Hasta luego...")
            break

        else:
            print("Ingrese una opcion correcta")

if __name__ == "__main__":
    main()
 

