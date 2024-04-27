peso = float(input("Cual es tu peso?"))
estatura = float (input("Cues es tu estatura?")) / 100

imc = peso / (estatura ** 2)

imc_redondeado = round(imc, 2)

print("Tu indice de masa muscular es de: " , imc_redondeado)