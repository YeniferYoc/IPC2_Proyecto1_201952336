class Patron:
    def __init__(self, codigo, lista):
        self.codigo = codigo
        self.lista = lista

    def getCodigo(self):
        return self.codigo
    def getLista(self):
        return self.lista 
    def mostrar_patron(self):
        print("CODIGO: "+str(self.codigo)+" PATRON: "+str(self.lista))
