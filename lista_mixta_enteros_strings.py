

#Dada una lista mixta de enteros y strings, devolver dos listas, una con todos los enteros y otra con todas las strings.


lista_base = ["uno", 1, "dos", 2, "tres", 3, "cuatro", 4, "cinco", 5]
lista_enteros = []
lista_strings = []

for posicion in lista_base:
    if type(posicion) == str:
        lista_strings.append(posicion)
    if type(posicion) == int:
        lista_enteros.append(posicion)

print (lista_strings)
print (lista_enteros)
