
#Para comerte un helado, te tiene que apetecer,
#tienes que tener dinero o gorronear a tu tia, y que la tienda este abierta

#El .upper te pasa las strings a mayusculas, evitando los problemas de input del usuario

apetece_helado_input = input("Te apetece un helado?(Si / No) ").upper()

if apetece_helado_input == "SI":
    apetece_helado = True
elif apetece_helado_input == "NO":
    apetece_helado = False
else:
    print("Teclea si o no, no se que has puesto, pero lo voy a contar como no")
    opcion_erronea = True


tienes_dinero_input = input("Tienes dinero para un helado?(Si / No) ").upper()
esta_la_tienda_abierta_input = input("¿Esta la tienda abierta? (Si / No) ").upper()
esta_tu_tia_input = input("¿Estas con tu tia? (Si/No)").upper()



apetece_helado = apetece_helado_input == "SI"
puedes_pagarlo = tienes_dinero_input == "SI" or esta_tu_tia_input == "SI"
esta_la_tienda_abierta = esta_la_tienda_abierta_input == "SI"



if opcion_erronea == True:
    print ("Teclea la opcion correcta")
if apetece_helado and puedes_pagarlo and esta_la_tienda_abierta:
    print("Pues te lo comes")
else:
    print("Pues te jodes")

