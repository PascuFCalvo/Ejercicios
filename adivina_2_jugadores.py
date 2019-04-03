

volver_a_empezar = "si"

while volver_a_empezar == "si":
    intentos = 0

    num_adivinar = int(input("Jugador 1, introduce un numero para adivinar del 1 al 100: "))
    num_juego = 0

    while num_adivinar != num_juego:
        print ("Jugador 2, adivina el numero: ")
        num_juego = int(input("Dime un numero del 1 al 100: "))


        if num_adivinar != num_juego:
            intentos += 1
            print("Sigue intentadolo, llevas {} intentos".format(intentos))

        else:
            intentos += 1
            print("Has ganado en {} intentos!".format(intentos))

    volver_a_empezar =(input("quieres volver a empezar: (si / no): "))




