from Cargar_archivo import recuperar
from xml.dom import minidom
from Piso import *
from Patron import *
import Estructuras
import Estructuras_patron
import Estructuras_cuadritos
from Celda import *
from graphviz import Graph
from os import startfile
import graphviz
from os import system


lista_pisos = Estructuras.ListaDoble()
piso_elegido = Piso(None,0,0,0.0,0.0,None)
lista_celdas = Estructuras_cuadritos.ListaDoble_cuadritos()
opcion_piso = 0
lista_celdas2 = Estructuras_cuadritos.ListaDoble_cuadritos()
objeto_patr_2 = Patron(0, None)
lista_cambiar = Estructuras_cuadritos.ListaDoble_cuadritos()
contador_cambios = 0
controlador = [0, None]

patron_final = Estructuras_cuadritos.ListaDoble_cuadritos()

def menu():
    salir = False
  
    while salir != True:    
        #AQUI ESTA EL MENU PRINCIPAL    
        print("")
        print("--------------------------------------------------------------------")
        print("1. CARGAR XML")
        print("2. MOSTRAR PISOS Y ELEGIR ")
        print("3. VER PATRON ELEGIDO")
        print("4. ELEGIR NUEVO PATRON")
        print("5. REALIZAR CAMBIOS")
        print("6. VER NUEVO PATRON")
        print("7. SALIR")
        print("--------------------------------------------------------------------")
        print("")
        opcion = int(input("DIGITE EL NUMERO DE LA OPCION CORRESPONDIENTE "))
        
        
        if(opcion == 1):
            print("AQUI SE SELECCIONAN LOS DATOS ")
            doc = minidom.parse('mi_xml.xml')
            pisos = doc.getElementsByTagName("piso")
            for piso in pisos:
                nombre = piso.attributes['nombre'].value 
                R = piso.getElementsByTagName("R")[0]
                C = piso.getElementsByTagName("C")[0]
                F = piso.getElementsByTagName("F")[0]
                S = piso.getElementsByTagName("S")[0]
                fila = R.firstChild.data
                columna = C.firstChild.data
                volteo = F.firstChild.data
                intercambio = S.firstChild.data

                patrones = piso.getElementsByTagName('patron')
                lista_patrones = Estructuras_patron.ListaDoble_patron()
                for patron in patrones:
                    codigo_pat = patron.attributes['codigo'].value 
                    patron_letras = patron.childNodes[0].data
                    #print(codigo_pat)
                    #print(patron.childNodes[0].data)
                    patron_nuevo = Patron(codigo_pat, patron_letras)
                    lista_patrones.añadirNodoPrincipio(patron_nuevo)

                piso_nuevo = Piso(nombre, fila, columna, volteo, intercambio, lista_patrones)
                #piso_nuevo.mostrar_piso()
                lista_pisos.añadirNodoPrincipio(piso_nuevo)


            lista_pisos.imprimirLista()

##########################################################################################################
        
        if(opcion == 2):
            print("")
            lista_pisos.imprimirLista()
            print("-------------------- PISOS DISPONIBLES ----------------------")
            
            nodoTemporal = Estructuras.Nodo("")

            nodoTemporal = lista_pisos.head
            contador = 0
            while nodoTemporal != None:
                contador += 1
                print(str(contador)+" -> "+"NOMBRE: "+nodoTemporal.objeto_piso.nombre)
                nodoTemporal.objeto_piso.patrones.imprimirLista()

                nodoTemporal = nodoTemporal.siguiente

            opcion_piso= int(input("ELIGE EL NUMERO DE PISO "))
            nodoTemp_opcion = Estructuras.Nodo("")
            nodoTemp_opcion = lista_pisos.head
            contador = 0
            opcion_patron = 0

            while nodoTemp_opcion != None:
                contador+=1
                if contador ==  opcion_piso:
                    print("NOMBRE: "+nodoTemp_opcion.objeto_piso.nombre+" FILAS: "+str(nodoTemp_opcion.objeto_piso.filas)+" COLUMNAS: "+nodoTemp_opcion.objeto_piso.columnas)
                    print("PRECIO VOLTEO: "+str(nodoTemp_opcion.objeto_piso.volteo)+" PRECIO INTERCAMBIO: "+ str(nodoTemp_opcion.objeto_piso.intercambio))
                    nodoTemp_opcion.objeto_piso.patrones.imprimirLista()

                    #LLENAR EL OBJETO PISO ELEGIDO PARA MAYOR FACILIDAD
                    nombre_elegido = nodoTemp_opcion.objeto_piso.nombre
                    filas_elegido = nodoTemp_opcion.objeto_piso.filas
                    columnas_elegido = nodoTemp_opcion.objeto_piso.columnas
                    volteo_elegido =nodoTemp_opcion.objeto_piso.volteo
                    intercamnbio_elegido = nodoTemp_opcion.objeto_piso.intercambio


                    opcion_patron=int(input("AHORA ELIGE EL NUMERO DE PATRON QUE DESEA: "))
                    #BUSCAMOS AL PATRON DEL PISO ELEGIDO 
                    nodoTemp_opcion_pat = Estructuras_patron.Nodo("")
                    nodoTemp_opcion_pat = nodoTemp_opcion.objeto_piso.patrones.head
                    contador_2 = 0  
                    while nodoTemp_opcion_pat != None:
                        contador_2+=1
                        if contador_2 ==  opcion_patron: 
                            print("PATRON ENCONTRADO ")
                            objeto_patr = Patron(nodoTemp_opcion_pat.objeto_patron.codigo,nodoTemp_opcion_pat.objeto_patron.lista)
                                                       
                            piso_elegido = Piso(nombre_elegido, filas_elegido, columnas_elegido, volteo_elegido, intercamnbio_elegido,objeto_patr)
                            print("")
                            print("***** EL PISO QUE ELEGISTE ES: ******")

                            print("NOMBRE: "+piso_elegido.nombre+" FILAS: "+str(piso_elegido.filas)+" COLUMNAS: "+piso_elegido.columnas)
                            print("PRECIO VOLTEO: "+str(piso_elegido.volteo)+" PRECIO INTERCAMBIO: "+ str(piso_elegido.intercambio))
                            piso_elegido.patrones.mostrar_patron()
                        nodoTemp_opcion_pat = nodoTemp_opcion_pat.siguiente
                                                                   

                nodoTemp_opcion = nodoTemp_opcion.siguiente
            print("")
            
            if piso_elegido.nombre == None:
                print("NO SE ENCONTRO EL PISO ")
            else:
                cadena_patron1 = str(piso_elegido.patrones.lista)
                
                #CONVIERTO LA CADENA DEL PATRON ELEGIDO A UNA LISTA DE OBJETOS TIPO CELDA
                contador_fila = 0
                contador_col = 0
                filas = int(piso_elegido.filas)
                columnas = int(piso_elegido.columnas)
                print("LLENANDO LISTA CELDAS")
                temp = ""
                print("longitud cadena "+str(len(cadena_patron1)))
                cadena_patron1 = cadena_patron1.replace(" ","")
                cadena_patron1 = cadena_patron1.replace("\n","")
                print(cadena_patron1)
                print("longitud cadena "+str(len(cadena_patron1)))
                for letra in cadena_patron1:
                    #print(letra)
                    temp += letra
                    print(letra)
                    if contador_fila < filas:
                        #print("hola")
                        #print(" segundo")
                        if contador_col < columnas:
                           # print("tercero")
                         #   print(letra)
                            
                            nueva_celda = Celda(contador_fila, contador_col,letra)
                            lista_celdas.añadirNodo(nueva_celda)
                            contador_col +=1
                        else:
                            contador_col = 0
                            contador_fila += 1
                            nueva_celda = Celda(contador_fila, contador_col,letra)
                            lista_celdas.añadirNodo(nueva_celda)
                            contador_col += 1
                
                print(" ")
                print("ESTA ES LA LISTA DE CELDAS")
                lista_celdas.imprimirLista()

#########################################################################################################
                        
        if(opcion == 3):
            print("VER PATRON ELEGIDO ")
            filas = int(piso_elegido.filas)
            columnas = int(piso_elegido.columnas)
            codigo_patron = str(piso_elegido.patrones.codigo)

            mi_archivo= open('patron_elegido1_1.dot','w')
            mi_archivo.write("digraph L{")
            mi_archivo.write("node[shape = box fillcolor = \"#FFEDBB\" style  = filled]")
            mi_archivo.write("subgraph cluster_p{")
            mi_archivo.write("label= \"PATRON "+codigo_patron+"\"")
            mi_archivo.write("bgcolor = \"#398D9C\"")
            mi_archivo.write("edge [dir = \"both\"]")
            celda="celda"
            contador = 1 
            mensaje =''
            print("*** Imprimiendo Celdas ***")
            nodoTemporal = Estructuras_cuadritos.Nodo("")

            nodoTemporal = lista_celdas.head
            
        
            for i in range(filas):
                for j in range(columnas):
                    mensaje =str(celda+str(contador))
                    color_celda = str(nodoTemporal.objeto_celda.color)
                    if color_celda.upper() == 'B':
                        color_celda = 'black'
                    if color_celda.upper() == 'W':
                        color_celda = 'white'
                    nodoTemporal = nodoTemporal.siguiente
                    mi_archivo.write(mensaje+"[label= \""+str(contador)+"\", fillcolor ="+color_celda+", group = 2 ];")
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

            system('dot -Tpng patron_elegido1_1.dot -o patron_elegido1_1.png')
            system('cd./patron_elegido1_1.png')
            startfile('patron_elegido1_1.png')
            
##########################################################################################################

        if(opcion == 4):
            print("----------------------------- ELEGIR NUEVO PATRON ------------------------------")
            nodoTemp_opcion = Estructuras.Nodo("")
            nodoTemp_opcion = lista_pisos.head
            contador = 0
            opcion_patron = 0

            while nodoTemp_opcion != None: #jsjs
                contador+=1
                if contador ==  opcion_piso:
                    print("NOMBRE: "+nodoTemp_opcion.objeto_piso.nombre+" FILAS: "+str(nodoTemp_opcion.objeto_piso.filas)+" COLUMNAS: "+nodoTemp_opcion.objeto_piso.columnas)
                    print("PRECIO VOLTEO: "+str(nodoTemp_opcion.objeto_piso.volteo)+" PRECIO INTERCAMBIO: "+ str(nodoTemp_opcion.objeto_piso.intercambio))
                    nodoTemp_opcion.objeto_piso.patrones.imprimirLista()



                    opcion_patron_2=int(input("AHORA ELIGE EL NUMERO DE PATRON QUE DESEA: "))
                    #BUSCAMOS AL PATRON DEL PISO ELEGIDO 
                    nodoTemp_opcion_pat = Estructuras_patron.Nodo("")
                    nodoTemp_opcion_pat = nodoTemp_opcion.objeto_piso.patrones.head
                    contador_2 = 0  
                    while nodoTemp_opcion_pat != None:
                        contador_2+=1
                        if contador_2 ==  opcion_patron_2: 
                            print("PATRON ENCONTRADO ")
                            objeto_patr_2 = Patron(nodoTemp_opcion_pat.objeto_patron.codigo,nodoTemp_opcion_pat.objeto_patron.lista)
                                                       
                            objeto_patr_2.mostrar_patron()
                        nodoTemp_opcion_pat = nodoTemp_opcion_pat.siguiente
                                                                   

                nodoTemp_opcion = nodoTemp_opcion.siguiente

            
            cadena_patron2 = str(objeto_patr_2.lista)
            #CONVIERTO LA CADENA DEL PATRON ELEGIDO A UNA LISTA DE OBJETOS TIPO CELDA
            contador_fila = 0
            contador_col = 0
            filas = int(piso_elegido.filas)
            columnas = int(piso_elegido.columnas)
            print("LLENANDO LISTA CELDAS")
            
            print("longitud cadena "+str(len(cadena_patron2)))
            cadena_patron2 = cadena_patron2.replace(" ","")
            cadena_patron2 = cadena_patron2.replace("\n","")
            print(cadena_patron2)
            print("longitud cadena "+str(len(cadena_patron2)))
            for letra in cadena_patron2:
                #print(letra)
                if contador_fila < filas:
                    if contador_col < columnas:
                        nueva_celda = Celda(contador_fila, contador_col,letra)
                        lista_celdas2.añadirNodo(nueva_celda)
                        contador_col +=1
                    else:
                        contador_col = 0
                        contador_fila += 1
                        nueva_celda = Celda(contador_fila, contador_col,letra)
                        lista_celdas2.añadirNodo(nueva_celda)
                        contador_col += 1
                
            print(" ")
            print("ESTA ES LA LISTA DE CELDAS")
            lista_celdas2.imprimirLista()

##########################################################################################################
        if(opcion == 5):
            print("REALIZAR CAMBIOS")
            #DETERMINO LOS PRECIOS PARA ENCONTRAR LA SOLUCION MAS ECONOMICA 
            precio_volteo = 1000#int(piso_elegido.volteo)
            precio_inter = 1#int(piso_elegido.intercambio)
            costo_total = 0 #EL COSTO TOTAL SE VA A AUMENTAR CON CADA ACCION 
            #HACEMOS LA PRIMERA EVALUACION DE CAMBIOS

            retorno = Comparar_patrones(lista_celdas, lista_celdas2)
            lista_cambiar = retorno[1]
            lista_cambiar.imprimirLista()
            contador_cambios =  retorno[0]#LLEVA EL CONTEO DE LAS CASILLAS DIFERENTES ENTRE
            #EL PATRON INICIAL Y EL NUEVO PATTRON
            #POSIBILIDADS DE CAMBIO
            if contador_cambios == 0 : #SINO HAY CASILLAS DIFERENTES ENTONCES EL PATRON FINAL ES IGUAL AL ORIGINAL
                print("NO HAY CAMBIOS POR REALIZAR, ENTONCES EL PATRON FINAL ES: ")
                patron_final = lista_celdas 
                patron_final.imprimirLista()
                print("EL COSTO TOTAL ES: "+str(costo_total))
            
            else: #SI SI HAY CASILLAS DIFERENTES O ERRONEAS 
                if precio_volteo >= precio_inter: #intentamos no usar mucho volteo 
                    print("INTENTAMOS USAR MAS EL INTERCAMBIO ")
                    while contador_cambios != 0: #MIENTRAS CONTADOR NO SEA 0 ENTONCES QUE SIGA CAMNIANDO
                        #NODO QUE CONTIENE LA PRIMERA CELDA HALLADA DIFERENTE AL PATRON ELEGIDO
                        nodo_cambios = Estructuras_cuadritos.Nodo("")
                        nodo_cambios = lista_cambiar.head
                        #PARA CAMBIAR EL NODO SE NECESITA CONOCER SU POSICION EXACTA 
                        fila_err = nodo_cambios.objeto_celda.fil
                        columna_err = nodo_cambios.objeto_celda.col
                        #SE RECORRE LA LISTA DE CELDAS PARA BUSCAR EL NODO QUE SE ENCONTRO DIFERENTE
                        nodo_que_busca = Estructuras_cuadritos.Nodo("")
                        nodo_que_busca = lista_celdas.head 

                        #SI SOLO ES UN PISO EL DIFERENTE LO UNICO POR HACER ES VOLTEARLO SIN IMPORTAT EL PRECIO                    
                        if contador_cambios == 1: 
                            print("SOLO ES UN CAMBIO ENTONCES SE VOLTEA EL PÍSO QUE ESTA EN LA POSICION: "+str(fila_err)+" , "+str(columna_err))
                            #SE BUSCA EÑ NODO A CAMBIAR PRIIMERO SE RECORRE LA LISTA
                            patron_final=Volteo(nodo_cambios,lista_celdas, fila_err, columna_err)
                            print("OBSERVE LOS CAMBIOS REALIZADOS")
                            patron_final.imprimirLista()
                            costo_total += precio_volteo
                        
                        else:#SI HAY MAS DE UN CAMBIO, ENTONCES SE EVALUA EL COSTO DE INTERCAMBIO Y VOLTEO  
                            #INTENTAMOS EL INTERCAMBIO
                            while nodo_que_busca != None:#BUSCAMOS EL NODO QUE ES DIFERENTE
                                
                                if nodo_que_busca.objeto_celda.fil == fila_err and nodo_que_busca.objeto_celda.col == columna_err:
                                    color_lista_celdas1 = nodo_que_busca.objeto_celda.color
                                    
                                    if color_lista_celdas1 != nodo_cambios.siguiente.objeto_celda.color : #VEO LAS COORDENADAS DEL NODO SIGUIENTE QUE TEIEN LO QUE NECESITO
                                        #AHORA BUSCAMOS EL NODO CON SUS COORDENADAS
                                        fila_siguiente = nodo_cambios.siguiente.objeto_celda.fil
                                        columna_siguiente = nodo_cambios.siguiente.objeto_celda.col
                                        #SI ESTA ENSEGUIDA A LA PAR
                                        if columna_siguiente == (columna_err+1) and fila_siguiente == fila_err:
                                            print("ESTA A LA PAR")
                                            aux1 = nodo_que_busca.objeto_celda
                                            aux2 = nodo_que_busca.siguiente.objeto_celda
                                            nodo_que_busca.objeto_celda = aux2
                                            nodo_que_busca.siguiente.objeto_celda = aux1
                                            costo_total += precio_inter
                                            patron_final = lista_celdas
                                            patron_final.imprimirLista()
                                            break

                                        #SI ESTA ENSEGUIDA ABAJO
                                        elif fila_siguiente == (fila_err+1) and columna_siguiente == columna_err:
                                            print("ESTA ABAJO")
                                            nodo_temp_abajo = Estructuras_cuadritos.Nodo("")
                                            nodo_temp_abajo = lista_celdas.head
                                            while nodo_temp_abajo != None:
                                                if nodo_temp_abajo.objeto_celda.fil == fila_siguiente and nodo_temp_abajo.objeto_celda.col == columna_siguiente:
                                                    aux1 = nodo_que_busca.objeto_celda
                                                    aux2 = nodo_temp_abajo.objeto_celda
                                                    nodo_que_busca.objeto_celda = aux2
                                                    nodo_temp_abajo.objeto_celda = aux1
                                                    costo_total += precio_inter
                                                    patron_final = lista_celdas
                                                    patron_final.imprimirLista()
                                                    break
                                                nodo_temp_abajo = nodo_temp_abajo.siguiente
 
                                        #SI ESTA LEJOS ABAJO
                                        elif fila_siguiente == (fila_err) :
                                            print("ESTA A LA PAR PERO LEJOS")
                                            #SE CREA UN NODO QUE AVANCE HACIA EL CAMBIO
                                            calcular_precio = (columna_siguiente -columna_err)*precio_inter
                                            print(calcular_precio)
                                            print(2*precio_volteo)
                                            if calcular_precio < (2*precio_volteo):
                                                print("entro")
                                                nodo_busca_par_lejos = Estructuras_cuadritos.Nodo("")
                                                nodo_busca_par_lejos = lista_celdas.head
                                                while nodo_busca_par_lejos != None: 
                                                    if nodo_busca_par_lejos.objeto_celda.fil == fila_siguiente and nodo_busca_par_lejos.objeto_celda.col == columna_siguiente:
                                                        aux1 = nodo_que_busca.objeto_celda
                                                        aux2 = nodo_busca_par_lejos.objeto_celda
                                                        nodo_que_busca.objeto_celda = aux2
                                                        nodo_busca_par_lejos.objeto_celda = aux1
                                                        costo_total += calcular_precio
                                                        patron_final = lista_celdas
                                                        patron_final.imprimirLista()
                                                        break
                                                    nodo_busca_par_lejos = nodo_busca_par_lejos.siguiente
                                            else:
                                                patron_final=Volteo(nodo_cambios,lista_celdas, fila_err, columna_err)
                                                print("OBSERVE LOS CAMBIOS REALIZADOS")
                                                patron_final.imprimirLista()
                                                costo_total += precio_volteo
                                                patron_final=Volteo(nodo_cambios.siguiente,lista_celdas, fila_siguiente, columna_siguiente)
                                                print("SIGUIENTE VOLTEO")
                                                patron_final.imprimirLista()
                                                costo_total += precio_volteo
                                                break

                                        elif columna_siguiente == (columna_err):
                                            print("ESTA ABAJO PERO LEJOS")
                                        #SI ESTA LEJOS ARRIBA
                                        break
                                    else:
                                        print("no me sirve")

                                nodo_que_busca = nodo_que_busca.siguiente
                                break

                            #BUSCAMOS EL NODO QUE ESTA MAL


                        #HAGO QUE VUELVA A COMPARAR LOS PATRONES PARA SEGUIR CAMBIANDO O FINALIZAR EL CICLO
                        retorno = Comparar_patrones(lista_celdas, lista_celdas2)
                        lista_cambiar = retorno[1]
                        print("ESTO ES LO QUE HAY QUE CAMBIAR")
                        lista_cambiar.imprimirLista()
                        contador_cambios =  retorno[0]
                        
            
            print("")
            print("----------------------------------------------------------------------------------")
            print("COSTO POR TODO: Q. "   +str(costo_total))
            print("IMPRIMIR PATRON FINAL")
            patron_final.imprimirLista()      

##########################################################################################################

        if(opcion == 6):
            print("VER NUEVO PATRON")
            salir = True

##########################################################################################################

        if(opcion == 7):
            print("ADIOS!!!! :)")
            salir = True 



def Generar_graphviz():    
    filas = int(piso_elegido.filas)
    columnas = int(piso_elegido.columnas)
    codigo_patron = str(piso_elegido.patrones)

    mi_archivo= open('patron_elegido1_1.dot','w')
    mi_archivo.write("digraph L{")
    mi_archivo.write("node[shape = box fillcolor = \"#FFEDBB\" style  = filled]")
    mi_archivo.write("subgraph cluster_p{")
    mi_archivo.write("label= \"PATRON"+codigo_patron+"\"")
    mi_archivo.write("bgcolor = \"#398D9C\"")
    mi_archivo.write("edge [dir = \"both\"]")
    celda="celda"
    contador = 1 
    mensaje =''
    print("*** Imprimiendo Celdas ***")
    nodoTemporal = Estructuras_cuadritos.Nodo("")

    nodoTemporal = lista_celdas.head
    
 
    for i in range(filas):
        for j in range(columnas):
            mensaje =str(celda+str(contador))
            color_celda = str(nodoTemporal.objeto_celda.color)
            if color_celda.upper() == 'B':
                color_celda = 'black'
            if color_celda.upper() == 'W':
                color_celda = 'white'
            nodoTemporal = nodoTemporal.siguiente
            mi_archivo.write(mensaje+"[label= \""+str(contador)+"\", fillcolor ="+color_celda+", group = 2 ];")
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

    system('dot -Tpng patron_elegido1_1.dot -o patron_elegido1_1.png')
    system('cd./patron_elegido1_1.png')
    startfile('patron_elegido1_1.png')

def Comparar_patrones(lista1, lista2):
    lista_cambiar = Estructuras_cuadritos.ListaDoble_cuadritos()
    nodo_tem_celd_pat1 = Estructuras_cuadritos.Nodo("")
    nodo_tem_celd_pat1 = lista1.head

    nodo_tem_celd_pat2 = Estructuras_cuadritos.Nodo("")
    nodo_tem_celd_pat2 = lista2.head

    contador_cambios = 0
    while nodo_tem_celd_pat1 != None:
        color1 = str(nodo_tem_celd_pat1.objeto_celda.color)
        color2 = nodo_tem_celd_pat2.objeto_celda.color 
            
        if  color1 == color2 :
            pass
        else:
           contador_cambios += 1
           nueva_celda = nodo_tem_celd_pat1.objeto_celda
           lista_cambiar.añadirNodo(nueva_celda) 

        nodo_tem_celd_pat1 = nodo_tem_celd_pat1.siguiente
        nodo_tem_celd_pat2 = nodo_tem_celd_pat2.siguiente
    
    print("LA CANTIDAD DE CUADROS A CORREGIR ES: "+str(contador_cambios))
    print(contador_cambios)
    controlador[0] = contador_cambios
    controlador[1] = lista_cambiar
    return controlador
    
def Volteo(nodo_diferente, lista_orignal, fila, columna):
    nodo_que_busca = Estructuras_cuadritos.Nodo("")
    nodo_que_busca = lista_orignal.head
    #SE BUSCA EÑ NODO A CAMBIAR PRIIMERO SE RECORRE LA LISTA
    while nodo_que_busca != None:
        if nodo_que_busca.objeto_celda.fil == fila and nodo_que_busca.objeto_celda.col == columna:
            color = nodo_diferente.objeto_celda.color
            if color.upper() == 'B':
                nodo_diferente.objeto_celda.color = 'W'
            else:
                nodo_diferente.objeto_celda.color = 'B'
        nodo_que_busca = nodo_que_busca.siguiente
    return lista_orignal
    
def Intercambio_siguiente():
    pass
    

def main(): #METODO PRINCIPAL QUE INVOCA AL MENU2 
    menu()

if __name__ == "__main__":
    main()
  

    