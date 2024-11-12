salir="N"
while salir=="N":
        print("Bienvenidos a este humilde programa\n"
        "Para saber si dos palabras son anagramas, por favor ingreselas a continuacion\n")

        palabra_1=input("Ingrese la primera palabra: ")
        palabra_2=input("Ingrese la segunda palabra: ")
        palabra_1=palabra_1.lower().strip()
        palabra_2=palabra_2.lower().strip()
        list_1=sorted(palabra_1)
        list_2=sorted(palabra_2)
        if list_1==list_2:
            print("Las palabras ingresadas son un anagrama")
        else:
            print("las palabras ingresadas NO son un anagrama")
        salir=input("Desea salir? S/N")
        salir=salir.upper().strip()
