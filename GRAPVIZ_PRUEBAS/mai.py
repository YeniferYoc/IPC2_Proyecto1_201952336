from numpy import absolute
import interc

listaDoble = interc.ListaDoble()
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
    #listaDoble.borrarNodo("Vainilla")
    nodo_temporal = interc.Nodo("")
    nodo_temporal = listaDoble.head
    while nodo_temporal != None :
        listaDoble.borrarNodo(listaDoble)
        print("Eme")
        nodo_temporal = nodo_temporal.siguiente
    listaDoble.imprimirLista()
    print("***  Espacio  ***")
    #y cualquier otra instrucción


    print(absolute(-4))