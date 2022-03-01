class Celda:
    def __init__(self, fil, col, color):
        self.fil = fil
        self.col = col 
        self.color = color 
        self.siguiente = None 
        self.anterior = None
    
    def getFil(self):
        return self.fil
    
    def getCol(self):
        return self.col
    
    def getColor(self):
        return self.color 
    
    def mostrar_celda(self):
        print(" FILA: "+str(self.fil)+" COLUMNA: "+str(self.col)+" COLOR: "+self.color)
        