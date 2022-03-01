palabra1 = "ab01"
palabra2 = "ab0"
if palabra1 < palabra2:
    print("fallo ")
else:
    print("funciona")
   # palabralista = palabra1.split("")
   # print(palabralista)
    #for letra in palabralista:
      #  print(letra)

cadena = "¡Hola, mundo!"

# Método 2, con índice
for indice in range(len(cadena)):
    caracter = cadena[indice]
    print("En el índice {} tenemos a '{}'".format(indice, caracter))
   
for letra in palabra1:
   # print(letra)
    if letra == 'a':
        print(letra+"ddd")
    else:
        print(letra)

