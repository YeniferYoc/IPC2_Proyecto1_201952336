class Nodo:
    def __init__(self, objeto_celda):
        self.objeto_celda = objeto_celda
        self.siguiente = None
        self.anterior = None

class ListaDoble_cuadritos:
    def __init__(self):
        self.head = None
        self.end = None

    def añadirNodo(self, objet_celda):
        nuevoNodo = Nodo(objet_celda)
        #insertamos si la lista esta vacia
        if self.head == None:
            self.head = nuevoNodo
            self.end = nuevoNodo

        #si por lo menos hay un nodo, insertamos al final
        else:
            self.end.siguiente = nuevoNodo
            nuevoNodo.anterior = self.end
            self.end = nuevoNodo


    def imprimirLista(self):
        print("--------------------------------------------------------------------------------")
        nodoTemporal = Nodo("")

        nodoTemporal = self.head
        contador = 0
        while nodoTemporal != None:
            contador += 1
            print("Nodo: "+str(contador)+" FILA -> "+str(nodoTemporal.objeto_celda.fil)+" COLUMNA -> "+str(nodoTemporal.objeto_celda.col)+" COLOR -> "+str(nodoTemporal.objeto_celda.color))
            nodoTemporal = nodoTemporal.siguiente

        print("--------------------------------------------------------------------------------")