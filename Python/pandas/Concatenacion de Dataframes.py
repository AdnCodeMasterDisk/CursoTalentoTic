import pandas as pd

df1 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [3, 4, 5],
    'C': [6, 7, 8]
})

df2 = pd.DataFrame({
    'A': [9, 10, 11],
    'B': [12, 13, 14],
    'C': [15, 16, 17] 
})

concatenacion = pd.concat([df1, df2], axis=0)

print("La concatenacion de las dos tablas de datos da como resutado:")
print(concatenacion)

suma = concatenacion['A'].sum()
print ("La suma de la colummna a es igual a:" , suma)