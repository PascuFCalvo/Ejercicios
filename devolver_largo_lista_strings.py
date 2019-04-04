
#Te devuelve la longitud de cada uno de los caracteres de la lista string

lista_strings = ["uno","dos","tres","cuatro","cinco"]
lista_longitudes =[]

for posicion in lista_strings:
    lista_longitudes.append(len(posicion))


print (lista_strings)
print (lista_longitudes)