asignaturas = ["matematicas", "ciencias", "religion", "sociales", "programcion", "deportes"]
notas = []

for asignatura in asignaturas:
    nota = float(input(f"Cual es la nota en {asignatura}:"))
    notas.append(nota)

promedio = sum(notas) / len(notas)

for i in range (len(asignaturas)):
    print(f"En la clase {asignaturas[i]} optubiste una nota de: {notas[i]}")    

print ("Tu promedio academico es de:" , promedio)