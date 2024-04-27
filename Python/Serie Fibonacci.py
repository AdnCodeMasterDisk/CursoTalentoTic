def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

num_elementos = int(input("Ingrese el número de elementos de la serie de Fibonacci que desea visualizar: "))

print("Serie de Fibonacci:")
for i in range(num_elementos):
    print(fibonacci(i))
