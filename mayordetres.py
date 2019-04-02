adivinar = 6
intentos = 1
countdown = 4

print("¿Que numero estoy pensando?, tienes 5 intentos")

usuario = int(input("Numero: "))

if usuario != adivinar:
    while intentos < 5:
        print("Has perdido")
        print("Te quedan {} intentos ".format(countdown))
        usuario = int(input("Numero: "))
        intentos = intentos + 1
        countdown = countdown - 1

if usuario == adivinar:
    print("Has ganado")
    print("Fin del programa")
else:

    print("Has perdido, se te han agotado las opciones")
    print("Fin del programa")
