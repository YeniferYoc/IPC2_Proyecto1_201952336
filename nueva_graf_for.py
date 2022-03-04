from os import startfile
import graphviz
from os import system


def Generar_graphviz():
    filas = 4
    columnas = 5

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