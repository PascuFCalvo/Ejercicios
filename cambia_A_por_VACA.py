

string_usuario = input("Escribe una frasse: ")
nueva_string =""

for caracter in string_usuario:
    nueva_string = string_usuario.replace("a","VACA")

print(nueva_string)