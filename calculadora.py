

resultado = 0
salir = 0

while salir != 1:

    operacion = input("Introduce una operacion: (sumar, restar, multiplicar, dividir): ").upper()

    primer_digito = int(input("Introduce el primer numero para operar: "))

    segundo_digito = int(input("Introduce el segundo digito para operar: "))

    if operacion == "SUMAR":
        resultado = primer_digito + segundo_digito

    elif operacion == "RESTAR":
        resultado = primer_digito - segundo_digito

    elif operacion == "MULTIPLICAR":
        resultado = primer_digito * segundo_digito

    elif operacion == "DIVIDIR":
        resultado = primer_digito / segundo_digito


    print("El resultado es {}".format(resultado))

    salir_prog = input("¿Has terminado?: (Si/No): ").upper()

    if salir_prog == "Si":
        salir = 1
        print ("Adios!")
        quit()

    else: salir = 0

