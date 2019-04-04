

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


suma = 0
media = 0
longitud = 0

for posicion in numeros_usuario:
    suma = suma + posicion
    longitud += 1

media = suma / longitud

print("La media es {}. ".format(media))