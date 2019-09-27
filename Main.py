#Mensaje de bienvenida

print("Bienvenido, escoge un nivel para comenzar:")

print("1. Fácil")
print("2. Intermedio")
print("3. Díficil")


bandera = True
while (bandera):
    nivel = input()

    if nivel == "1":
        #   Elegir un sudoku de la lista Fácil
        print("Fácil")
        bandera = False

    elif nivel == "2":
        #   Elegir un sudoku de la lista Intermedio
        print("intermedio")
        bandera = False

    elif nivel == "3":
        #   Elegir un sudoku de la lista Dificil
        print("Díficil")
        bandera = False

    else:
        print("Hubo un error con tu opción, vuelve a intentarlo :D")
