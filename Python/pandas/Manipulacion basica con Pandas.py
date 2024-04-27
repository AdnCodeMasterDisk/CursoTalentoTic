import pandas as pd

datos = pd.DataFrame({
    'Nombre': ['Juan', 'María', 'Pedro', 'Laura', 'Sofía'],
    'Edad': [30, 25, 28, 22, 35],
    'Ciudad': ['Bogotá', 'Medellín', 'Cali', 'Barranquilla', 'Cartagena']
})

print("Tabla completa")
print(datos)
print()

datos_filtrados  = datos[datos['Edad'] > 25]

print("Los Mayores de 25 años son:")
print(datos_filtrados)
print()

datos['Categoria'] = datos['Edad'].apply(lambda x: 'Joven' if x <= 25 else 'Adulto')

print("Data frame actualizado:")
print(datos)