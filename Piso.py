from Patron import *
class Piso:
    def __init__(self, nombre, filas, columnas,volteo, intercambio, patrones):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.volteo = volteo
        self.intercambio = intercambio
        self.patrones = patrones
        

    def getNombre(self):
        return self.nombre
    
    def getFilas(self):
        return self.filas 
    
    def getColumnas(self):
        return self.columas 
    
    def getVolteo(self):
        return self.volteo 
    
    def getIntercambio(self):
        return self.intercambio 
    
    def getPatrones(self):
        return self.patrones

    def mostrar_piso(self):
        print("NOMBRE:  "+str(self.nombre)+" FILAS: "+str(self.filas)+" COLUMNAS: "+str(self.columas)+" PRECIO VOLTEO: "+str(self.volteo)+" PRECIO INTERCAMBIO: "+str(self.intercambio)+"")
        for patron in self.patrones: 
            patron.mostrar_patron()