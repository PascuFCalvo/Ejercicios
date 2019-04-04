

#calcula el maximo sin usar funcion max

numeros = [1, 3, 3, 85, 5, 6, 7, 8, 42, 10, 11, 12, 111, 14, 15, 4000, 30, 60, 70]

maximo = 0
for pos in range(len(numeros)):
 if maximo < numeros[pos]:
        maximo = numeros[pos]



print (maximo)