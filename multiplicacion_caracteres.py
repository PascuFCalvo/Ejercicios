

numeros_usuario = []
num = ""
terminar = "no"

while terminar != "si":
     while not num.isdigit():
         num = input("dime un numero: ")
     numeros_usuario.append((num))
     num=""
     terminar = input("añadido, has terminado (si/no):")

print("Esta es tu lista:")
print(numeros_usuario)

#convierte la string en enteros, por cada posicion en la lista, le da el formato int

numeros_usuario = [int(pos) for pos in numeros_usuario]


resultado = 1


for posicion in numeros_usuario:
    resultado = posicion * resultado

print("La multiplicaion es {}. ".format(resultado))