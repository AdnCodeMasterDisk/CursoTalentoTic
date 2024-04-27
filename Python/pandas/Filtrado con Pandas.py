import pandas as pd

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = pd.read_csv(url, header=None, names=["sepal_length", "sepal_width", "petal_length", "petal_width", "species"])

print("Primeras 5 filas")
print(iris.head(5))

setosa = iris[iris["species"] == "Iris-setosa"]
print("\nLa lista de las especies de setosa es:\n", setosa)

media_length_sepalos_setosas = setosa['sepal_length'].mean()

print("\nLa media de la longitud de los sepalos de las especies de setosas es de: ", media_length_sepalos_setosas)


