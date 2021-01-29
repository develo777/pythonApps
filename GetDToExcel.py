import xlwt

class GetDToExcel:

    def __init__(self,name):

        #Agregar una instancia
        self.wb=xlwt.Workbook()
        #Agregar  hoja
        self.ws=self.wb.add_sheet(name,cell_overwrite_ok=True)

        #definimos nombre de columnas 
        columnas = [
                    "Indice",
                    "Archivo",
                    "N",
                    "Tipo",
                    "Documento",
                    "Moneda",
                    "ImporteTotal"
                    ]
        col=0
        #Escribir las columnas en la hoja
        for columna in columnas:
            self.ws.write(0,col,columna)
            col=col+1
        
        self.row=1

    def addContents(self,item):
        self.ws.write(self.row,0,item.Indice)
        self.ws.write(self.row,1,item.Archivo)
        self.ws.write(self.row,2,item.N)
        self.ws.write(self.row,3,item.Tipo)
        self.ws.write(self.row,4,item.Documento)
        self.ws.write(self.row,5,item.Moneda)
        self.ws.write(self.row,6,item.ImporteTotal)
        self.row=self.row+1

    def saveFile(self,fileName):
        self.wb.save(fileName)
        print("Documento Excel generado!")


