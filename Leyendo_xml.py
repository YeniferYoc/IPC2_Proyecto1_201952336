from xml.dom import minidom
from Piso import *
from Patron import *

#FUNICONA
lista_pisos = []

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
    lista_patrones = []
    for patron in patrones:
        codigo_pat = patron.attributes['codigo'].value  
        patron_letras = patron.childNodes[0].data
        #print(codigo_pat)
        #print(patron.childNodes[0].data)
        patron_nuevo = Patron(codigo_pat, patron_letras)
        lista_patrones.append(patron_nuevo)

    piso_nuevo = Piso(nombre, fila, columna, volteo, intercambio, lista_patrones)
    piso_nuevo.mostrar_piso()
    lista_pisos.append(piso_nuevo)
    




