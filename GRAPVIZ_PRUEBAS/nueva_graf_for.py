from os import startfile
import graphviz
from os import system


def Generar_graphviz():
    filas = 4
    columnas = 5
    
    hhh = '''
        Fila1[label= "1", group=1]
        Fila2[label= "2", group=1]
        Fila3[label= "3", group=1]
        Fila4[label= "4", group=1]
        Fila5[label= "5", group=1]
        #ENLAZAR NODOS FILAS 
        Fila1->Fila2;
        Fila2->Fila3;
        Fila3->Fila4;
        Fila4->Fila5;
        #COLUMNAS
        Columna1[label= "1", group=2, fillcolor=yellow]
        Columna2[label= "2", group=3, fillcolor=yellow]
        Columna3[label= "3", group=4, fillcolor=yellow]
        Columna4[label= "4", group=5, fillcolor=yellow]
        Columna5[label= "5", group=6, fillcolor=yellow]
        #ENLAZAR COLUMNAS
        Columna1->Columna2;
        Columna2->Columna3;
        Columna3->Columna4;
        Columna4->Columna5;
        #ENLAZAR A LA RAIZ
        raiz ->Fila1;
        raiz -> Columna1;
        #ALINEACION CABECERAS
        {rank = same;raiz;Columna1; Columna2;Columna3;Columna4;Columna5}
        nodo1_1[label="1,1", fillcolor = green, group = 2 ]
        nodo4_4[label="4,4", fillcolor = green, group = 5 ]
        nodo5_3[label="5,3", fillcolor = green, group = 4 ]
        nodo2_2[label="2,2", fillcolor = green, group = 3 ]
        nodo2_4[label="2,4", fillcolor = green, group = 3 ]
        nodo3_4[label="3,4", fillcolor = green, group = 5 ]
        nodo5_5[label="5,5", fillcolor = green, group = 2 ]
        #DIRECCION A LOS NODOS NUEVOS 
        Fila1 -> nodo1_1
        {rank = same; Fila1; nodo1_1}
        Fila2 -> nodo2_2;
        nodo2_2 -> nodo2_4;
        {rank= same; Fila2; nodo2_2; nodo2_4}
        Fila3 -> nodo3_4;
        {rank = same; Fila3; nodo3_4}
        Fila4 -> nodo4_4;
        {rank = same; Fila4;nodo4_4}
        Fila5 -> nodo5_3;
        nodo5_3  -> nodo5_5;
        {rank = same; Fila5; nodo5_3; nodo5_5}
        #enlazar con columnas
        Columna1 -> nodo1_1;
        Columna2 ->nodo2_2;
        Columna3 -> nodo5_3;
        Columna4 -> nodo2_4;
        Columna5 ->nodo5_5;
        nodo2_4 ->nodo3_4;
        nodo3_4 ->nodo4_4;


        

    }
}


    '''

    mi_archivo= open('prueba_gra_10.dot','w')
    mi_archivo.write("digraph L{")
    mi_archivo.write("node[shape = box fillcolor = \"#FFEDBB\" style  = filled]")
    mi_archivo.write("subgraph cluster_p{")
    mi_archivo.write("label= \"MATRIZ DISERSA\"")
    mi_archivo.write("bgcolor = \"#398D9C\"")
    mi_archivo.write("edge [dir = \"both\"]")
    celda="celda"
    contador = 1 
    mensaje =''
    for i in range(filas):
        for j in range(columnas):
            mensaje =str(celda+str(contador))
            
            mi_archivo.write(mensaje+"[label= \""+str(contador)+"\", fillcolor = green, group = 2 ];")
            contador += 1 

    total_celdas = filas* columnas
    
    mensaje = ''
    for j in range(1, total_celdas-filas+1, columnas):
        contador2 = j
        for i in range(1,columnas,1):
            mensaje =str(celda+str(contador2))
            sig_fila = str(celda+str(contador2+1))
            mi_archivo.write(mensaje+"->"+sig_fila+";")
            contador2+=1
    
    for j in range(1, total_celdas-filas+1, columnas):
        contador2 = j
        mi_archivo.write("{rank = same;")
        for i in range(1,columnas+1,1):
            mensaje =str(celda+str(contador2))
            mi_archivo.write(mensaje+";")
            contador2+=1

        mi_archivo.write("}")

    
    
    for j in range(1, columnas+1, 1):
        for i in range(j,total_celdas-columnas+1,columnas):
            mensaje =str(celda+str(i))
            sig_fila = str(celda+str(i+columnas))
            mi_archivo.write(mensaje+"->"+sig_fila+";")
    

    mi_archivo.write("}")
    mi_archivo.write("}")

    mi_archivo.close()

    system('dot -Tpng prueba_gra_10.dot -o prueba_gra_10.png')
    system('cd./prueba_gra_10.png')
    startfile('prueba_gra_10.png')

if __name__== "__main__":
    Generar_graphviz()