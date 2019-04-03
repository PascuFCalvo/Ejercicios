

#Extrae las vocales de una frase

frase_sacar_vocales = input("Escribe una frase: ")

vocales = [ "a", "e", "i", "o","u"]

nvocales = 0

lista_vocales = []

for posicion in frase_sacar_vocales:
    if posicion in vocales:
        lista_vocales.append(posicion)



print(lista_vocales)