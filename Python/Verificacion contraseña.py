contrasena = input("Escribe una contraseña, recuerda agregar al menos un nùmero")

if len(contrasena) < 8:
    print (" La contrasena no tiene los caracteres suficientes")
else:
    tiene_numeros = any(letra.isdigit() for letra in contrasena)
    if not tiene_numeros:
         print (" La contrasena no tiene al menos un numero, ingrese una contraseña correcta")
    else:
         print (" La contrasena es correcta")