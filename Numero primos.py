salir=""
def primo_def():
  try:
      numero=int(input("Ingrese un numero para saber si es primo: "))
      for i in range(2, numero):
         if numero%i==0:
              print("Su numero no es primo")
              break
         else:
              if i==numero-1:
                  print("Su numero es primo")
  except ValueError:
      print("Error. Tipo de dato no admitido.")

print("Bienvenidos a esta app inutil!!.\n"
      "Aqui sabras si tu numero es o no primo\n")

while salir!="salir":
    primo_def()
    salir=input("Si desea probar con otro numero apriete cualquier tecla\n"
                "Si desea salir escriba \"salir\": ")
    salir=salir.lower().strip()
