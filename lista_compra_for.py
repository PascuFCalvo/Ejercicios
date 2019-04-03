#Crear una lista de la compra "infinita" hasta que el usuario diga fin, y luego mostarla

mi_lista = []
input_usuario = ""


while input_usuario != "fin":
    input_usuario = input("¿que necesitas comprar? (escribe -fin- para salir): ")
    if input_usuario != "fin":
        mi_lista.append(input_usuario)

#la variable despues de for es un nombre arbitrario completamente
#for va a ir recorriendo la lista y ejecutando su "bucle" tantas veces como elementos tenga la lista

for articulo in mi_lista:
    print("tengo que comprar: {}".format(articulo))

print("Esta es la lista de la compra")