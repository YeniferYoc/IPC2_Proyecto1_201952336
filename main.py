from Cargar_archivo import recuperar
from xml.dom import minidom
from Piso import *
from Patron import *
import Estructuras
import Estructuras_patron
import Estructuras_cuadritos
from Celda import *
from graphviz import Graph

def menu():
    salir = False
    lista_pisos = Estructuras.ListaDoble()
    piso_elegido = Piso(None,0,0,0.0,0.0,None)
    lista_celdas = Estructuras_cuadritos.ListaDoble_cuadritos()
    opcion_piso = 0
    lista_celdas2 = Estructuras_cuadritos.ListaDoble_cuadritos()
    objeto_patr_2 = Patron(0, None)
  
    while salir != True:    
        #AQUI ESTA EL MENU PRINCIPAL    
        print("")
        print("--------------------------------------------------------------------")
        print("1. CARGAR XML")
        print("2. MOSTRAR PISOS Y ELEGIR ")
        print("3. ELEGIR NUEVO PATRON")
        print("4. SALIR")
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

                #print("nombre:%s " % nombre)
                #print("R:%s" % R.firstChild.data)
                #print("C:%s" % C.firstChild.data)
                #print("F:%s" % F.firstChild.data)
                #print("S:%s" % S.firstChild.data)

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
                                
            
##########################################################################################################

        if(opcion == 3):
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

        if(opcion == 4):
            print("ADIOS!!!! :)")
            salir = True

def main(): #METODO PRINCIPAL QUE INVOCA AL MENU2 
    menu()

if __name__ == "__main__":
    main()
  

    