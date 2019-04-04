

#cambia vocales por i

string_usuario = input("Escribe una frase: ")
nueva_string =""
vocal = "aeiouAEIOU"

for caracter in string_usuario:
    if caracter in vocal:
        string_usuario = string_usuario.replace(caracter, "i")

print(string_usuario)
