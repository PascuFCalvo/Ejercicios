

#cambia las vocales por su numero de aparición. Por ejemplo la string “aurora boreal” se convertiría en “12r3r4 b5r67l”

string_usuario = input("Escribe una frase: ")
nueva_string = ""
vocal = "aeiouAEIOU"
contador_posicion = 0




for posicion in string_usuario:
    if posicion in vocal:
        contador_posicion += 1
        string_usuario = string_usuario.replace(str(posicion), str(contador_posicion), 1)



print (string_usuario)











