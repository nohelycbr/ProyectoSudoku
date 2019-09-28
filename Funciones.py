from colorama import Cursor, init, Fore

init()


def nivel_facil():
    f1 = [['*', '*', '*', '*', '*', '*', 1, '*', "*"],
          ['*', 4, 7, 1, 6, '*', '*', '*', '*'],
          ['*', 2, '*', 5, 3, 4, '*', '*', 7],
          ['*', 6, 1, '*', '*', 7, 8, '*', '*'],
          ['*', 7, 4, '*', 9, '*', 3, 1, '*'],
          ['*', '*', 2, 6, '*', '*', 4, 7, '*'],
          [2, '*', '*', 3, 4, 5, '*', 6, '*'],
          ['*', '*', '*', '*', 7, 1, 9, 5, '*'],
          ['*', '*', 3, '*', '*', '*', '*', '*', '*']]

    f2 = [['*', '*', '*', 4, '*', 3, '*', '*', '*'],
          ['*', '*', 5, 9, '*', 7, 2, '*', '*'],
          ['*', 3, '*', '*', 6, '*', '*', 7, '*'],
          ['*', 9, '*', 7, '*', 8, '*', 2, '*'],
          ['*', 4, 3, '*', '*', '*', 7, 9, '*'],
          ['*', 7, '*', 3, '*', 2, '*', 5, '*'],
          ['*', 1, '*', '*', 5, '*', '*', 3, '*'],
          ['*', '*', 9, 2, '*', 6, 4, '*', '*'],
          ['*', '*', '*', 1, '*', 4, '*', '*', '*']]

    f3 = [['*', '*', 5, '*', '*', '*', 7, '*', '*'],
          ['*', 8, '*', 1, '*', 5, '*', 2, '*'],
          [9, '*', '*', 4, 6, 7, '*', '*', 5],
          ['*', 5, 6, 2, '*', 1, 3, 8, '*'],
          ['*', '*', 8, '*', '*', '*', 9, '*', '*'],
          ['*', 9, 2, 5, '*', 8, 6, 7, '*'],
          [2, '*', '*', 8, 5, 9, '*', '*', 3],
          ['*', 6, '*', 7, '*', 3, '*', 4, '*'],
          ['*', '*', 3, '*', '*', '*', 5, '*', '*']]

    f4 = [['*', '*', 8, 2, '*', 9, 5, '*', '*'],
          ['*', '*', 6, 1, '*', 5, 4, '*', '*'],
          [5, 9, '*', '*', '*', '*', '*', 2, 7],
          [6, 7, '*', '*', 9, '*', '*', 4, 5],
          ['*', '*', '*', 3, '*', 4, '*', '*', '*'],
          [2, 4, '*', '*', 1, '*', '*', 8, 9],
          [3, 6, '*', '*', '*', '*', '*', 5, 8],
          ['*', '*', 2, 5, '*', 8, 7, '*', '*'],
          ['*', '*', 4, 7, '*', 6, 9, '*', '*']]

    f5 = [['*', '*', '*', 4, '*', 5, '*', '*', '*'],
          ['*', '*', 6, 2, 1, 7, 9, '*', '*'],
          ['*', 8, 4, 9, '*', 6, 5, 1, '*'],
          [8, 6, 9, '*', '*', '*', 7, 5, 1],
          ['*', 7, '*', '*', '*', '*', '*', 4, '*'],
          [5, 4, 2, '*', '*', '*', 6, 9, 3],
          ['*', 9, 5, 8, '*', 1, 4, 3, '*'],
          ['*', '*', 1, 7, 9, 2, 8, '*', '*'],
          ['*', '*', '*', 5, '*', 3, '*', '*', '*']]

    return [f1, f2, f3, f4, f5]


def nivel_inter():
    i1 = [['*', 6, 9, 2, '*', 3, 4, 5, '*'],
          [5, '*', 7, '*', '*', '*', 9, '*', 1],
          [3, '*', '*', '*', '*', '*', '*', '*', 6],
          [7, '*', '*', 6, '*', 9, '*', '*', 3],
          ['*', 8, '*', 4, '*', 2, '*', 6, '*'],
          ['*', '*', '*', '*', 1, '*', '*', '*', '*'],
          ['*', 7, '*', 3, '*', 8, '*', 2, '*'],
          ['*', '*', '*', 7, '*', 1, '*', '*', '*'],
          ['*', '*', '*', '*', '*', '*', '*', '*', '*']]

    i2 = [['*', 7, 2, '*', '*', 3, 1, '*'],
          ['*', '*', 8, '*', '*', '*', '*', 4],
          [5, '*', '*', 4, '*', 7, '*', 9],
          [8, '*', 1, '*', 5, '*', '*', '*'],
          ['*', 1, '*', '*', '*', 5, '*', '*'],
          ['*', '*', 7, '*', 8, '*', 6, 1],
          [6, 3, '*', 2, '*', '*', '*', 5],
          [1, '*', '*', '*', 3, '*', '*', '*'],
          ['*', 4, '*', '*', 7, 8, '*', '*']]

    i3 = [[6, '*', '*', '*', '*', '*', '*', '*'],
          [5, 9, 4, 3, '*', '*', '*', '*'],
          ['*', '*', '*', 7, '*', 4, '*', '*'],
          ['*', '*', 3, '*', 1, '*', '*', '*'],
          ['*', 5, '*', '*', '*', '*', 6, 2],
          ['*', '*', 7, '*', '*', 9, 4, '*'],
          ['*', 3, '*', '*', 6, '*', 9, '*'],
          ['*', '*', '*', 2, 3, 1, '*', '*'],
          ['*', '*', '*', 8, '*', '*', '*', '*']]

    i4 = [['*', '*', '*', '*', '*', '*', '*', '*'],
          [3, '*', '*', 2, 6, '*', '*', '*'],
          ['*', '*', 3, '*', 7, 2, 8, '*'],
          ['*', 7, '*', '*', 8, 1, '*', 5],
          ['*', '*', '*', '*', '*', '*', '*', '*'],
          ['*', 5, 1, '*', '*', 7, '*', 2],
          ['*', 3, 6, '*', 2, 9, 1, '*'],
          ['*', 9, '*', '*', '*', 4, '*', '*'],
          ['*', '*', 8, '*', 5, '*', '*', '*']]

    i5 = [['*', 3, '*', 5, 7, 6, 1, '*'],
          ['*', 5, '*', '*', '*', '*', '*', '*'],
          [7, '*', 9, '*', '*', 4, '*', '*'],
          ['*', 8, '*', 6, '*', 7, '*', '*'],
          [1, '*', 5, 3, '*', '*', '*', '*'],
          [3, '*', '*', '*', '*', 1, 9, '*'],
          [2, 9, 1, '*', 4, '*', 7, '*'],
          [8, '*', '*', '*', 2, 3, '*', '*'],
          ['*', '*', '*', '*', '*', '*', '*', '*']]

    return [i1, i2, i3, i4, i5]


def nivel_dificil():
    d1 = [[6, '*', '*', 7, '*', '*', 9, '*'],
          [7, 8, '*', '*', '*', '*', '*', '*'],
          ['*', '*', 6, 8, '*', '*', '*', '*'],
          [9, '*', '*', '*', '*', '*', 3, '*'],
          ['*', 7, 5, '*', 2, 1, '*', '*'],
          ['*', '*', '*', '*', '*', '*', '*', 6],
          ['*', '*', '*', 1, 6, '*', 7, '*'],
          ['*', '*', '*', '*', '*', 3, '*', 2],
          ['*', '*', '*', 3, '*', '*', '*', 9]]

    d2 = [['*', '*', 4, '*', 1, '*', '*', '*'],
          ['*', '*', 2, '*', 7, '*', 8, '*'],
          ['*', '*', '*', '*', '*', '*', 1, '*'],
          ['*', 1, 5, '*', 8, 6, '*', '*'],
          ['*', '*', '*', 2, '*', '*', '*', '*'],
          ['*', '*', 1, '*', 6, '*', 5, '*'],
          ['*', '*', 6, '*', 9, '*', 3, '*'],
          ['*', 6, 8, '*', 3, 9, 2, '*'],
          ['*', 9, '*', '*', '*', 8, '*', '*']]

    d3 = [['*', '*', '*', '*', 8, '*', '*', '*'],
          ['*', '*', '*', 3, '*', '*', 2, 1],
          ['*', 5, 7, '*', 4, 9, '*', 3],
          ['*', 8, '*', '*', '*', 3, 1, '*'],
          ['*', '*', '*', '*', '*', '*', 4, 9],
          [1, 3, '*', '*', '*', '*', '*', '*'],
          ['*', 6, 9, '*', '*', '*', '*', '*'],
          ['*', '*', 8, 2, '*', '*', '*', '*'],
          ['*', 2, '*', 5, '*', '*', '*', 7]]

    d4 = [['*', '*', '*', '*', '*', '*', '*', '*'],
          [6, '*', '*', '*', '*', '*', 1, 8],
          ['*', '*', 6, '*', 9, '*', '*', 4],
          ['*', '*', 3, '*', '*', 8, 9, '*'],
          [9, 2, '*', 1, '*', '*', 6, '*'],
          ['*', '*', 2, '*', '*', 4, 7, '*'],
          ['*', '*', 1, '*', 2, '*', '*', 9],
          [7, '*', '*', '*', '*', '*', 8, 6],
          ['*', '*', '*', '*', '*', '*', '*', '*']]

    d5 = [[5, '*', '*', '*', '*', '*', '*', '*'],
          ['*', '*', 6, '*', '*', '*', 2, '*'],
          ['*', 8, '*', '*', 2, '*', '*', 9],
          ['*', '*', '*', 3, '*', 9, '*', '*'],
          ['*', 9, 2, 6, 1, 5, 8, '*'],
          ['*', 7, '*', 5, '*', '*', '*', '*'],
          [8, '*', 9, '*', '*', 2, 1, '*'],
          ['*', '*', '*', '*', 3, '*', 6, '*'],
          ['*', '*', '*', '*', '*', '*', '*', 8]]

    return [d1, d2, d3, d4, d5]


def solucion():
    return [[9, 6, 3, 1, 7, 4, 2, 5, 8],
            [1, 7, 8, 3, 2, 5, 6, 4, 9],
            [2, 5, 4, 6, 8, 9, 7, 3, 1],
            [8, 2, 1, 4, 3, 7, 5, 9, 6],
            [4, 9, 6, 8, 5, 2, 3, 1, 7],
            [7, 3, 5, 9, 6, 1, 8, 2, 4],
            [5, 8, 9, 7, 1, 3, 4, 6, 2],
            [3, 1, 7, 2, 4, 6, 9, 8, 5],
            [6, 4, 2, 5, 9, 8, 1, 7, 3]]


def VisualizaTabla_2(tabla, noModificables):
    i = 0
    j = 0
    indices = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    fila_concat = '  |'
    fmto = ""
    for indice in indices:
        fmto = Fore.WHITE + fmto + ' ' + str(indice)
        if j == 2 or j == 5 or j == 8:
            fmto = fmto + "|"
        j += 1

    print(fila_concat + fmto)
    print("   ---------------------")

    for fila in tabla:
        fila_concat = str(indices[i]) + " |"
        fmto = ""
        j = 0
        for columna in fila:
            coordenada = str(i) + "," + str(j)

            if coordenada in noModificables:
                fmto = fmto + " " + Fore.WHITE + str(columna)
            else:
                fmto = fmto + " " + Fore.BLUE + str(columna)

            if j == 2 or j == 5 or j == 8:
                fmto = fmto + Fore.WHITE + "|"
            j += 1
        print(fila_concat + fmto)
        if i == 2 or i == 5 or i == 8:
            print("   ---------------------")
        i += 1


def obtenerNoModificables(tabla):
    lista = []
    fila = 0

    for i in tabla:
        col = 0
        for j in i:
            if j != '*':
                coordenada = str(fila) + "," + str(col)
                lista.append(coordenada)
            col += 1
        fila += 1
    return lista


def comprobacion_filas(tabla):
    bandera = True

    for filas in tabla:

        set_fila = set(filas)
        regla_1 = len(set_fila) == 9
        regla_2 = max(set_fila) == 9
        regla_3 = min(set_fila) == 1

        if (regla_1 and regla_2 and regla_3):
            bandera = True
        else:
            bandera = False
            return bandera
            break;

    return bandera


def comprobacion_columnas(tabla):
    transpuesta = []
    # Se transpone la tabla para reutilizar la funcion de comprobacion_filas
    for i in range(len(tabla)):
        new_fila = []
        for j in range(len(tabla[0])):
            new_fila.append(tabla[j][i])
        transpuesta.append(new_fila)
    # Se utiliza la funcion de comprobacion_filas y se regresa el resultado
    bandera = comprobacion_filas(transpuesta)
    return bandera


def comprobacion_cuadrante(tabla):
    # Se transforma cada cuadrante en una fila de la matriz para reutilizar la
    #
    cuadrantes = []
    cuadrante_1 = []
    cuadrante_2 = []
    cuadrante_3 = []
    cuadrante_4 = []
    cuadrante_5 = []
    cuadrante_6 = []
    cuadrante_7 = []
    cuadrante_8 = []
    cuadrante_9 = []

    for i in range(len(tabla)):
        for j in range(len(tabla[0])):
            if i < 3:
                if j < 3:
                    cuadrante_1.append(tabla[i][j])
                elif j > 2 and j < 6:
                    cuadrante_2.append(tabla[i][j])
                elif j > 5 and j < 9:
                    cuadrante_3.append(tabla[i][j])
            elif i > 2 and i < 6:
                if j < 3:
                    cuadrante_4.append(tabla[i][j])
                elif j > 2 and j < 6:
                    cuadrante_5.append(tabla[i][j])
                elif j > 5 and j < 9:
                    cuadrante_6.append(tabla[i][j])
            elif i > 5 and i < 9:
                if j < 3:
                    cuadrante_7.append(tabla[i][j])
                elif j > 2 and j < 6:
                    cuadrante_8.append(tabla[i][j])
                elif j > 5 and j < 9:
                    cuadrante_9.append(tabla[i][j])

    cuadrantes.append(cuadrante_1)
    cuadrantes.append(cuadrante_2)
    cuadrantes.append(cuadrante_3)
    cuadrantes.append(cuadrante_4)
    cuadrantes.append(cuadrante_5)
    cuadrantes.append(cuadrante_6)
    cuadrantes.append(cuadrante_7)
    cuadrantes.append(cuadrante_8)
    cuadrantes.append(cuadrante_9)

    return comprobacion_filas(cuadrantes)


def comprobar_tabla(tabla):
    boolean_filas = comprobacion_filas(tabla)
    boolean_columnas = comprobacion_columnas(tabla)
    boolean_cuadrante = comprobacion_cuadrante(tabla)

    return (boolean_filas and boolean_columnas and boolean_cuadrante)

def comprobar_llenado_tabla(tabla):
    bandera = False

    for i in tabla:
        for j in i:
            if j == '*':
                bandera = True
                return bandera
                break;

    return bandera


def IngresarCoordenadas(listaNM,XY, dato,tabla):
    #Checar si se puede modificar
    if XY in listaNM:
        print("Esa celda no se puede modificar. Intenta con otra coordenada")
    else:
        tabla[int(XY.split(",")[0])][int(XY.split(",")[1])] = int(dato)
    return tabla

def EliminarCoordenada(listaNM,XY,tabla):
    #Checar si se puede modificar
    if XY in listaNM:
        print("Esa celda no se puede modificar. Intenta con otra coordenada")
    else:
        tabla[int(XY.split(",")[0])][int(XY.split(",")[1])] = "*"
    return tabla