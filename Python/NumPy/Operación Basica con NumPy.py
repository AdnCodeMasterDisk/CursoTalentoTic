import numpy as np

vector = np.array([1, 2, 3, 4, 5])

media= np.mean(vector)
desviacion = np.std(vector)

print("Media del vector es" , media)
print("La desviacion estandar del vector es:", desviacion)

matriz = np.random.randint(1, 11, size=(2, 3))
 
multiplicacion_matriz = matriz * 2

print("La matriz es igual a:")
print(matriz)
print("\n La matriz mltiplicada por 2 es:")
print(multiplicacion_matriz)
