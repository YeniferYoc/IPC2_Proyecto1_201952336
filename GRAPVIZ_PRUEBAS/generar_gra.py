from os import startfile
import graphviz
from os import system


def Generar_graphviz():
    graphviz = '''
    digraph L{
    node[shape = box fillcolor = "#FFEDBB" style  = filled]
    
    subgraph cluster_p{
        label= "MATRIZ DISERSA"
        bgcolor = "#398D9C"
        raiz[label = "0,0"]
        edge [dir = "both"]
        #CABEZERAS FILAS 
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

    mi_archivo= open('graphviz.dot','w')
    mi_archivo.write(graphviz)
    mi_archivo.close()

    system('dot -Tpng graphviz.dot -o graphviz.png')
    system('cd./graphviz.png')
    startfile('graphviz.png')

if __name__== "__main__":
    Generar_graphviz()