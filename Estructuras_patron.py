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
        print("*** Imprimiendo patrones ***")
        nodoTemporal = Nodo("")

        nodoTemporal = self.head
        contador = 0
        while nodoTemporal != None:
            contador += 1
            print("PATRON:"+str(contador)+" -> "+nodoTemporal.objeto_patron.codigo+" CADENA DE PATRON: "+nodoTemporal.objeto_patron.lista)
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

"""
listaDoble = ListaDoble()
listaDoble.añadirNodoPrincipio("Fresa")
listaDoble.añadirNodoPrincipio("Vainilla")
listaDoble.añadirNodoPrincipio("Chocolate")
listaDoble.añadirNodoPrincipio("Pistacho")

#listaDoble2 = Estructuras.ListaDoble()
#listaDoble2.añadirNodoFinal("Fresa")
#listaDoble2.añadirNodoFinal("Vainilla")
#listaDoble2.añadirNodoFinal("Chocolate")
#listaDoble2.añadirNodoFinal("Pistacho")

if __name__ == '__main__':
    listaDoble.imprimirLista()
    print("***  Espacio  ***")
    listaDoble.borrarNodo("Vainilla")
    listaDoble.imprimirLista()
    print("***  Espacio  ***")
    #y cualquier otra instrucción
"""