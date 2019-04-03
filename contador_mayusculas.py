

#Este codigo cuenga mayusculas

frase_a_contar = input("Escribe una frase: ")

nmayusculas = 0


for posicion in frase_a_contar:
    if posicion >= "a".upper() and posicion <= "z".upper():
     nmayusculas += 1




print("la frase tiene {} mayusculas".format(nmayusculas))