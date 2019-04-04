
#Cambiar valores si es divisible  3 por un Fizz y los de 5 por un Buzz y si es de 3 y 5 Bazinga

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 20, 30, 60, 70]

for pos in range(len(numeros)):
    numero = numeros[pos]


    if numero % 3 == 0 and numero % 5 == 0:
     numeros[pos] = ""

    if numero % 5 == 0:
     numeros[pos] = "Buzz"

    if numero % 3 == 0:
     numeros[pos] = "Fizz"

    if numero % 3 == 0 and numero % 5 == 0:
     numeros[pos] = ""
     numeros[pos] = "Bazinga"


print (numeros)