import xlwt

class GetDToExcel:

    def __init__(self,name):

        #agrego una instancia
        self.wb=xlwt.Workbook()
        #agregar una hoja
        self.ws=self.wb.add_sheet(name,cell_overwrite_ok=True)

        #definimos nombre de columnas 
        columnas = [
                    "Indice",
                    "Archivo",
                    "N",
                    "Tipo"
                    "Documento",
                    "Moneda",
                    "ImporteTotal"
                    ]
        col=0
        #escribimos las columnas en la hoja
        for columna in columnas:
            self.ws.write(0,col,columna)
            col=col+1
        
        self.row=1
    def addContents(self,item):
        self.ws.write(self.row,0,item.Indice)
        self.ws.write(self.row,1,item.Archivo)
        self.row=self.row+1
    def saveFile(self,fileName):
        self.wb.save(fileName)
        print("Documento Excel generado!")


