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
        print("*** Imprimiendo Celdas ***")
        nodoTemporal = Nodo("")

        nodoTemporal = self.head
        contador = 0
        while nodoTemporal != None:
            contador += 1
            print("Nodo: "+str(contador)+" FILA -> "+str(nodoTemporal.objeto_celda.fil)+" COLUMNA -> "+str(nodoTemporal.objeto_celda.col)+" COLOR -> "+str(nodoTemporal.objeto_celda.color))
            nodoTemporal = nodoTemporal.siguiente

        print("*** Lista Terminada de patrones ***")

    def borrarNodo(self, dato):
        #creamos un nodo temporal
        nodoTemporal = Nodo("")

        #el temporal empieza en la cabeza
        nodoTemporal = self.head

        #Mientras que el temporal no sea nulo
        while nodoTemporal != None:

            #validamos si ese nodo es el que busco
            if nodoTemporal.dato == dato:

                #Si ese nodo es la cabeza
                if nodoTemporal == self.head:
                    print("Borrando dato en la cabeza")
                    self.head = self.head.siguiente
                    nodoTemporal.siguiente = None
                    self.head.anterior = None
                #Si ese nodo es la cola
                elif nodoTemporal == self.end:
                    print("Borrando dato en la cola")
                    self.end = self.end.anterior
                    nodoTemporal.anterior = None
                    self.end.siguiente = None
                #Si no es ni la cola ni la cabeza
                else:
                    print("Borrando dato del medio")
                    nodoTemporal.anterior.siguiente = nodoTemporal.siguiente
                    nodoTemporal.siguiente.anterior = nodoTemporal.anterior
                    nodoTemporal.siguiente = nodoTemporal.anterior = None

            nodoTemporal = nodoTemporal.siguiente

