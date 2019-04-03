
#Este codigo cuenga vocales y consonantes

frase_a_contar = input("Escribe una frase: ")

vocales = [ "a", "e", "i", "o","u"]

nvocales = 0
nconsonantes = 0

for letra in frase_a_contar:
    if letra in vocales:
        nvocales +=1

    else:
        nconsonantes +=1

print("la frase tiene {} vocales y {} consonantes".format(nvocales, nconsonantes))