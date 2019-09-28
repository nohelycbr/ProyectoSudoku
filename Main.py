import Funciones as fun
import random
from colorama import Cursor, init, Fore

init()

#Mensaje de bienvenida

print(Fore.BLUE+"-----------Sudoku-----------")
print(Fore.GREEN + "Instrucciones:")
print(Fore.GREEN+ "En la parte superior y lateral izquierda del sudoku")
print(Fore.GREEN+ "aparecerán números con los que podrás ingresar la coordenada")
print(Fore.GREEN+ "del número que deseas modificar.")
print(Fore.GREEN+ "Recuerda: Solo puedes modificar las casillas en "+Fore.BLUE+"azul")
print(Fore.WHITE+ "En caso de que quieras salir del juego sólo escribe " + Fore.RED+""'Salir'""+Fore.RESET)
print("")
print("Bienvenido, escoge un nivel para comenzar:")
print("1. Fácil")
print("2. Intermedio")
print("3. Díficil")

#Elección del nivel (Interacción con usuario)
bandera = True
while (bandera):
    nivel = input()

    if nivel == "1":
        #   Elegir un sudoku de la lista Fácil
        print("Fácil")
        sudokus = fun.nivel_facil()
        tabla = random.choice(sudokus)
        bandera = False

    elif nivel == "2":
        #   Elegir un sudoku de la lista Intermedio
        print("intermedio")
        sudokus = fun.nivel_inter()
        tabla = random.choice(sudokus)
        bandera = False

    elif nivel == "3":
        #   Elegir un sudoku de la lista Dificil
        print("Díficil")
        sudokus = fun.nivel_dificil()
        tabla = random.choice(sudokus)
        bandera = False

    else:
        print("Hubo un error con tu opción, vuelve a intentarlo :D")

#Se obtienen las coordenadas no modificables
noModificables = fun.obtenerNoModificables(tabla)
# Se muestra la tabla al usuario

fun.VisualizaTabla_2(tabla,noModificables)
print(Fore.WHITE + "¡Que empiece el juego!")
contador = 0

while (fun.comprobar_llenado_tabla(tabla)):
    if contador == 0:
        print("Ingresa las coordenadas del dato:")
        fila = input("Fila:")
        columna = input("Columna:")

        if(fila.lower() == 'salir' or columna.lower()=='salir'):
            print("Hasta pronto!")
            break;

        coordenada = fila +","+ columna
        dato = input("Ingresar dato: ")
        #Comprobar si es una celda modificable
        fun.IngresarCoordenadas(noModificables,coordenada,dato,tabla)
        #Si es modificable, insertar el dato en la tabla
        #De lo contrario, pedir de nuevo una coordenada

        fun.VisualizaTabla_2(tabla,noModificables)
    else:
        decision = input("1 - Eliminar, 2 - Modificar o Añadir Nuevo")
        if decision == "1":
            print("Ingresa las coordenadas del dato:")
            fila = input("Fila:")
            columna = input("Columna:")
            coordenada = fila + "," + columna
            if (fila.lower() == 'salir' or columna.lower() == 'salir'):
                print("Hasta pronto!")
                break;
            fun.EliminarCoordenada(noModificables,coordenada,tabla)
            fun.VisualizaTabla_2(tabla, noModificables)
        elif decision == "2":
            print("Ingresa las coordenadas del dato:")
            fila = input("Fila:")
            columna = input("Columna:")
            coordenada = fila + "," + columna
            if (fila.lower() == 'salir' or columna.lower() == 'salir'):
                print("Hasta pronto!")
                break;
            dato = input("Ingresar dato: ")
            fun.IngresarCoordenadas(noModificables,coordenada,dato,tabla)
            fun.VisualizaTabla_2(tabla, noModificables)
        else:
            if decision.lower() == 'salir':
                print("Hasta pronto!")
                break;
            else:
                print("Error. Vuelve a intentar")

    contador += 1



#Si sale del while quiere decir que toda la tabla ya está llena
if (fun.comprobar_llenado_tabla(tabla) == False):
    resultado = fun.comprobar_tabla(tabla)
    if(resultado):
        print("¡Felicidades, eres un champion!")
    else:
        print("Has perdido: Eres un L-O-S-E-R!")

