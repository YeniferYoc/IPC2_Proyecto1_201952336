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
        print("*** Imprimiendo lista de pisos***")
        nodoTemporal = Nodo("")

        nodoTemporal = self.head
        contador = 0
        while nodoTemporal != None:
            contador += 1
            print("Nodo:"+str(contador)+" -> "+"NOMBRE: "+nodoTemporal.objeto_piso.nombre+" FILAS:"+str(nodoTemporal.objeto_piso.filas)+" COLUMNAS: "+nodoTemporal.objeto_piso.columnas)
            print("PRECIO VOLTEO: "+str(nodoTemporal.objeto_piso.volteo)+" PRECIO INTERCAMBIO: "+ str(nodoTemporal.objeto_piso.intercambio))
            nodoTemporal.objeto_piso.patrones.imprimirLista()

            nodoTemporal = nodoTemporal.siguiente

        print("*** Lista Terminada de pisos***")

    def imprimir_nombre_pisos(lista):
        nodoTemporal = Nodo("")

        nodoTemporal = lista.head
        contador = 0
        while nodoTemporal != None:
            contador += 1
            print(str(contador)+" -> "+"NOMBRE: "+nodoTemporal.objeto_piso.nombre)

            nodoTemporal = nodoTemporal.siguiente

        print("*** Lista Terminada de pisos***")


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