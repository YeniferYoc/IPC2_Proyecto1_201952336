class Nodo:
    def __init__(self, objeto_patron):
        self.objeto_patron = objeto_patron
        self.siguiente = None
        self.anterior = None

class ListaDoble_patron:
    def __init__(self):
        self.head = None
        self.end = None

    def añadirNodoPrincipio(self, obj_patron):
        nuevoNodo = Nodo(obj_patron)

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
            if nodoTemporal.objeto_patron.codigo > nuevoNodo.objeto_patron.codigo:
                self.head.anterior = nuevoNodo
                nuevoNodo.siguiente = self.head
                self.head = nuevoNodo
            else:
             #   print("Insertando nodo al final")
                self.end.siguiente = nuevoNodo
                nuevoNodo.anterior = self.end
                self.end = nuevoNodo


    def imprimirLista(self):
        print("--------------------------------------------------------------------------------")
        print("---------------------------------- PATRONES ------------------------------------")
        nodoTemporal = Nodo("")

        nodoTemporal = self.head
        contador = 0
        while nodoTemporal != None:
            contador += 1
            print("PATRON:"+str(contador)+" -> "+nodoTemporal.objeto_patron.codigo+" CADENA DE PATRON: "+nodoTemporal.objeto_patron.lista)
            nodoTemporal = nodoTemporal.siguiente

        print("--------------------------------------------------------------------------------")

