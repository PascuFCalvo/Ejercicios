

numero = int(input("De que numero quieres la tabla de multiplicar"))

#usamos la funcion range, que recorre todos los valores dentro de un rango asignado

for posicion in range(1,11):
    print("{} x {} = {}".format(numero, posicion, numero*posicion))