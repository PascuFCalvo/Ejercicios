

#el mayor numero de una lista de 5 elementos
#Añadiendo numeros

numeros_usuario = []
num = ""

#vamos a utilizar un metodo para comprobar si el usuario teclea un numero


while len(numeros_usuario) < 5:
     while not num.isdigit():
         num = input("dime un numero: ")
#opcional, convertirlo en entero con la funcion int
     numeros_usuario.append(int(num))
     num=""
     print("añadido.")

print(numeros_usuario)

#Encontrando el mayor

num_mayor = numeros_usuario[0]

for posicion in numeros_usuario:
    if posicion > num_mayor:
        num_mayor = posicion

print("el numero mayor es {}. ".format(num_mayor))