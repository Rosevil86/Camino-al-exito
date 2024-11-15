ingredientes=("Pimientos", "Tofu", "Peperoni", "Jamon", "Salmon")


def ingreso():
  while True:
    try:
         print("Para agregar ingredientes vegetarianos ingrese 1"
             "\nPara ingredientes no vegetarianos ingrese 2")
         tipo=int(input("Cual es su eleccion? "))
         if tipo==1:
           vegetariano()
         elif tipo==2:
           no_vegetariano()
         else:
             print("Ingrese una opcion valida")
    except ValueError:
        print("Error, entrada invalida. Elija una opcion")



def vegetariano():
  while True:
    try:
       ingvege=int(input("Elija una opcion de ingrediente para su pizza vegetariana"
                         "\n1...... Pimientos"
                         "\n2...... Tofu"
                         "\n3...... Volver al menu anterior"
                         "\n4...... Volver al menu principal\n "))
       if ingvege==1:
            print("Su eleccion fue", ingredientes[0],
                  "\nSu piza de tomate, muzzarella y ", ingredientes[0], "se esta preparando")
            exit()
       elif ingvege==2:
           print("Su eleccion fue", ingredientes[1],
                 "\nSu piza de tomate, muzzarella y ", ingredientes[1], "se esta preparando")
           exit()
       elif ingvege == 3:
            vegetariano()
       elif ingvege == 4:
            ingreso()
       else:
           print("Ingrese una opcion valida")
           vegetariano()
    except ValueError:
       print("Error. Ingrese una opcion valida")



def no_vegetariano():
    while True:
        try:
            ingno = int(input("Elija una opcion de ingrediente para su pizza vegetariana"
                                "\n1...... Peperoni"
                                "\n2...... Jamon"
                                "\n3...... Salmon"
                                "\n4...... Volver al menu anterior"
                                "\n5...... Volver al menu principal\n "))
            if ingno == 1:
                print("Su eleccion fue", ingredientes[2],
                      "\nSu piza de tomate, muzzarella y ", ingredientes[2], "se esta preparando")
                exit()
            elif ingno == 2:
                print("Su eleccion fue", ingredientes[3],
                      "\nSu piza de tomate, muzzarella y ", ingredientes[3], "se esta preparando")
                exit()
            elif ingno == 3:
                print("Su eleccion fue", ingredientes[4],
                      "\nSu piza de tomate, muzzarella y ", ingredientes[4], "se esta preparando")
                exit()
            elif ingno == 4:
                no_vegetariano()
            elif ingno == 5:
                ingreso()
            else:
                print("Ingrese una opcion valida")
                no_vegetariano()
        except ValueError:
            print("Error. Ingrese una opcion valida")


print("Bienvenidos a Pizzeria Bella Napoli"
      "\nNuestras pizzas tienen tomate, queso muzzarela y un ingrediente a eleccion ")

ingreso()
