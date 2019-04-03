#tabla de multiplicar invertida

numero = int(input("De que numero quieres la tabla de multiplicar: "))

#usamos la funcion range, que recorre todos los valores dentro de un rango asignado

num = 11

for posicion in range(1,num):
    valor = num-posicion
    print("{} x {} = {}".format(numero, valor, numero*valor))