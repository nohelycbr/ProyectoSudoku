import pandas as pd

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

def VisualizaTabla(tabla):
    contador = 0
    indices = [0,1,2,3,4,5,6,7,8]

    print("  |",indices[0],indices[1],indices[2],"|",indices[3],indices[4],indices[5],"|",indices[6],indices[7],indices[8])
    print("   ----------------------")
    for fila in tabla:
        print(indices[contador],"|",fila[0],fila[1],fila[2],"|",fila[3],fila[4],fila[5],"|",fila[6],fila[7],fila[8])
        if(contador == 2 or contador== 5 or contador == 8):
                print("   ----------------------")
        contador+=1

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
        print(lista)

tabla = crear_tabla_vacia()
VisualizaTabla(tabla)
obtenerNoModificables(tabla)