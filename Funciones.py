from colorama import Cursor,init, Fore
init()

def crear_tabla_vacia ():
    return [['*','*','*','*','*','*',1,'*',"*"],
            ['*',4,7,1,6,'*','*','*','*'],
            ['*',2,'*',5,3,4,'*','*',7],
            ['*',6,1,'*','*',7,8,'*','*'],
            ['*',7,4,'*',9,'*',3,1,'*'],
            ['*','*',2,6,'*','*',4,7,'*'],
            [2,'*','*',3,4,5,'*',6,'*'],
            ['*','*','*','*',7,1,9,5,'*'],
            ['*','*',3,'*','*','*','*','*','*']]

def solucion ():
    return [[9,6,3,1,7,4,2,5,8],
            [1,7,8,3,2,5,6,4,9],
            [2,5,4,6,8,9,7,3,1],
            [8,2,1,4,3,7,5,9,6],
            [4,9,6,8,5,2,3,1,7],
            [7,3,5,9,6,1,8,2,4],
            [5,8,9,7,1,3,4,6,2],
            [3,1,7,2,4,6,9,8,5],
            [6,4,2,5,9,8,1,7,3]]

def VisualizaTabla(tabla):
    contador_col = 0
    contador_fila = 0
    indices = [0,1,2,3,4,5,6,7,8]

    print("  |",indices[0],indices[1],indices[2],"|",indices[3],indices[4],indices[5],"|",indices[6],indices[7],indices[8])
    print("   ----------------------")
    for fila in tabla:
        print(indices[contador_col],"|",fila[0],fila[1],fila[2],"|",fila[3],fila[4],fila[5],"|",fila[6],fila[7],fila[8])
        if(contador_col == 2 or contador_col== 5 or contador_col== 8):
                print("   ----------------------")
        contador_col+=1

def VisualizaTabla_2(tabla,noModificables):
    i = 0
    j = 0
    indices = [0,1,2,3,4,5,6,7,8]
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
        fmto=""
        j = 0
        for columna in fila:
            coordenada = str(i) +","+ str(j)

            if coordenada not in noModificables:
                fmto = fmto + " " + Fore.GREEN + str(columna)
            else:
                fmto = fmto + " " + Fore.WHITE +str(columna)

            if j == 2 or j == 5 or j == 8:
                fmto = fmto +Fore.WHITE+"|"
            j += 1
        print(fila_concat + fmto)
        if i ==2 or i == 5 or i ==8:
            print("   ---------------------")
        i+=1

def obtenerNoModificables(tabla):
        lista=[]
        fila = 0

        for i in tabla:
                col = 0
                for j in i:
                        if j != '*':
                                coordenada = str(fila) +","+str(col)
                                lista.append(coordenada)
                        col += 1
                fila +=1
        return lista


tabla = crear_tabla_vacia()
noModificables = obtenerNoModificables(tabla)
VisualizaTabla_2(tabla, noModificables)
