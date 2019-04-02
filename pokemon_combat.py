
pokemon_elegido = input("¿Contra que pokemon quieres pelear?: (Squirtle / Charmander / Bulbasur)").upper()

vida_pikachu = 100
vida_enemigo = 0
ataque_pokemon = 0

if pokemon_elegido == "SQUIRTLE":
 vida_enemigo = 90
 nombre_pokemon = "Squirtle"
 ataque_pokemon = 8

elif pokemon_elegido == "CHARMANDER":
 vida_enemigo = 80
 nombre_pokemon = "Charmander"
 ataque_pokemon = 7

elif pokemon_elegido == "BULBASUR":
 vida_enemigo = 100
 nombre_pokemon = "Bulbasur"
 ataque_pokemon = 10

while vida_pikachu > 0 and vida_enemigo > 0:
#Elegimos el ataque
    ataque_elegido = input("¿Que ataque quieres usar?: (Chispazo / Bola Voltio): ")

    if ataque_elegido == "Chispazo":
        vida_enemigo -= 10

    if ataque_elegido == "Bola Voltio":
        vida_enemigo -= 12
#Mostramos resultado de la ronda de combate
    print("la vida de {} ahora es de {}".format(nombre_pokemon, vida_enemigo))
#El enemigo nos ataca
    print("{} ataca, te quita {} puntos de vida".format(nombre_pokemon, ataque_pokemon))
    vida_pikachu -= ataque_pokemon

    print("la vida de Pikachu es {}".format(vida_pikachu))

if vida_enemigo <= 0:
    print("¡Has ganado!")

if vida_pikachu <= 0:
    print("¡Has perdido!")

print("El combate ha terminado")