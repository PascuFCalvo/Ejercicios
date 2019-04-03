

print("Conversor de temperatura de Farenhait a Celsius")

acabar = "no"

while acabar != "si":

    unidad = input("En que unidad me vas a dar la temperatura: (farenheiet / celsius): ")
    temperatura = int(input("Dime la temperatura: "))

    if unidad == "farenheit":
        temperatura_convertida = (temperatura  -32) /1.8
        print("{} grados farenheit equivalen a {} grados celsius.".format(temperatura, temperatura_convertida))

    else:
        temperatura_convertida = (temperatura*1.8)+32
        print("{} grados celsius equivalen a {} grados farenheit.".format(temperatura, temperatura_convertida))



    acabar = input("¿Quieres acbaar: (si/no)")
