

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


cantidad = 0

for posicion in numeros_usuario:
    cantidad += 1

print("La lista tiene {} elementos. ".format(cantidad))