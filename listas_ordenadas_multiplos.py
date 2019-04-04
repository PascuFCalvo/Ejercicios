lista_numeros = []
input_usuario = ""


while input_usuario != "fin":
    input_usuario = input("¿Dime un numero? (escribe -fin- para salir): ")
    if input_usuario != "fin":
        lista_numeros.append(input_usuario)


multiplos_dos = []
multiplos_tres = []
multiplos_cinco = []

for posicion in range(len(lista_numeros)):
    numero = int(lista_numeros[posicion])
    if numero % 2 == 0:
        multiplos_dos.append(numero)

    if numero % 3 == 0:
        multiplos_tres.append(numero)

    if numero % 5 == 0:
        multiplos_cinco.append(numero)

print("multiplos de dos {}".format(multiplos_dos))
print("multiplos de tres {}".format(multiplos_tres))
print("multiplos de cinco {}".format(multiplos_cinco))

