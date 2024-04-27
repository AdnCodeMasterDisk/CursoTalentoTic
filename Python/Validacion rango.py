numero = float(input("Elige un nùmero, pero ten  en cuenta que este entre 10 y 20, si eliges el nùmero correcto ganas un premio"))
numerocorrecto = 12

if 10 <= numero <= 20:
    print ("El nùmero " , int(numero), "esta en el rango de 10 a 20 ")
else:
    print ("El nùmero " ,  int(numero), "no esta en el rango de 10 a 20 ")

if numero == numerocorrecto:
    print ("Elejiste el " ,  int(numero), "el numero ganador es ", int(numerocorrecto), "Asi que Ganaste, Genial!!!")
else:
    print ("Elejiste el " , int(numero), "el numero ganador es ", int(numerocorrecto), "Asi que Perdiste, Intentalo de nuevo!!!")