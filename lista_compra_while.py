
#Crear una lista de la compra "infinita" hasta que el usuario diga fin, y luego mostarla

mi_lista = []
input_usuario = ""


while input_usuario != "fin":
    input_usuario = input("¿que necesitas comprar? (escribe -fin- para salir): ")
    if input_usuario != "fin":
        mi_lista.append(input_usuario)

largo_lista = len(mi_lista)
indice_actual = 0

while indice_actual < largo_lista:
    item = mi_lista[indice_actual]
    print("Tengo que comprar: {}".format(item))
    indice_actual += 1

print("Esta es la lista de la compra")
