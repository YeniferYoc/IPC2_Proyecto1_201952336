import Estructuras_patron
class Nodo:
    def __init__(self, objeto_piso):
        self.objeto_piso = objeto_piso
        self.siguiente = None
        self.anterior = None

class ListaDoble:
    def __init__(self):
        self.head = None
        self.end = None

    def añadirNodoPrincipio(self, obj_piso):
        nuevoNodo = Nodo(obj_piso)

        #Validamos si la lista esta vacia
        if self.head == None:
           # print("Ingresando nodo con lista vacia")
            self.head = nuevoNodo
            self.end = nuevoNodo
        
        #Si por lo menos hay un nodo, insertamos al inicio
        else:
            #print("*** ORDENANDO***")
            nodoTemporal = Nodo("")

            nodoTemporal = self.head
            if nodoTemporal.objeto_piso.nombre > nuevoNodo.objeto_piso.nombre:
                self.head.anterior = nuevoNodo
                nuevoNodo.siguiente = self.head
                self.head = nuevoNodo
            else:
                #print("Insertando nodo al final")
                self.end.siguiente = nuevoNodo
                nuevoNodo.anterior = self.end
                self.end = nuevoNodo


    def imprimirLista(self):
        print("--------------------------------------------------------------------------------")
        print("-------------------------------------- PISOS -----------------------------------")
        nodoTemporal = Nodo("")

        nodoTemporal = self.head
        contador = 0
        while nodoTemporal != None:
            contador += 1
            print("Nodo:"+str(contador)+" -> "+"NOMBRE: "+nodoTemporal.objeto_piso.nombre+" FILAS:"+str(nodoTemporal.objeto_piso.filas)+" COLUMNAS: "+nodoTemporal.objeto_piso.columnas)
            print("PRECIO VOLTEO: "+str(nodoTemporal.objeto_piso.volteo)+" PRECIO INTERCAMBIO: "+ str(nodoTemporal.objeto_piso.intercambio))
            nodoTemporal.objeto_piso.patrones.imprimirLista()

            nodoTemporal = nodoTemporal.siguiente

        print("--------------------------------------------------------------------------------")

    def imprimir_nombre_pisos(lista):
        nodoTemporal = Nodo("")

        nodoTemporal = lista.head
        contador = 0
        while nodoTemporal != None:
            contador += 1
            print(str(contador)+" -> "+"NOMBRE: "+nodoTemporal.objeto_piso.nombre)

            nodoTemporal = nodoTemporal.siguiente

        print("")
        print("")

    