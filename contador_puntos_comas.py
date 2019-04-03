

#Este codigo cuenga puntos, comas y espacios

frase_a_contar = input("Escribe una frase: ")

npuntos = 0
nespacios = 0
ncomas = 0

for posicion in frase_a_contar:
    if posicion == "," :
        ncomas +=1

    elif posicion == ".":
        npuntos +=1

    elif posicion == " ":
        nespacios += 1


print("la frase tiene {} comas, {} puntos u {} espacios".format(ncomas, npuntos, nespacios))