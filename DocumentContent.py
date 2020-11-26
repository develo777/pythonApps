
class DocumentContent(object):

    def __init__(self,lista):
        self.Indice=lista[0]
        self.Archivo=lista[1]
        self.N=lista[2]
        self.Tipo=lista[3]
        self.Documento=lista[4]
        self.Moneda=lista[5]
        self.ImporteTotal=lista[6]
    def listar(self):
        print(self.Indice+' '+'charly')