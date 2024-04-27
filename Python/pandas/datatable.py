import pandas as pd

data = {
    'Nombres' : ['David', 'Manuel', 'Mateo'],
    'Edades' : ['23', '34', '12'],
    'Calificaciones' : ['4', '5', '6']
}

df = pd.DataFrame(data)

print(df)
