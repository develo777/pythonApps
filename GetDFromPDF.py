from funciones.mod_Content import buscar_Indices
from GetDToExcel import GetDToExcel
from GetDContent import GetDContent
from GetDocument import *
import sys
import os
import PyPDF2

#ruta 
path="pdfs/" 
body=""
listita=[]
newlist=[]
listota=[]
#Lista de docs
documents=[]
hayData=False

# crear documento html
def crear_Html(html_content):
    value = -1
    try:
        archivo=open("Documentos.html","w")
        headerHtml="<!DOCTYPE html><html><head><mETA charset='utf-8' /><title>documento generedo</title></head><body><table>"
        fotterHtml="</body></html>"
        archivo.write(headerHtml+html_content+fotterHtml)
        archivo.close()
        value =0
    except:
        print("error al generar documento html")
    return value 
        

try:
    documents= os.listdir(path) #documentos
except:
    print("No se puedo encontrar el directorio o archivo")

if len(documents)!=0:
    #numeros de documentos
    for l in documents:
        pdfFileObject = open(path+l, 'rb')
        ##no considerar archivos que empiezen con . para mac
        if not l.startswith('.'):
            pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
            count = pdfReader.numPages #numero de paginas por documento
            ##rango de umero de paginas 
            for i in range(count):
                page = pdfReader.getPage(i)
                ##extraer contenido
                page_content = page.extractText() 
                ##identificar el tipo de documento
                tipoDocument = buscar_Indices(page_content,"FACTURA") 
                if len(tipoDocument)==0:          
                    #body.append(leer_Boletas(l,page_content))
                    body+=leer_Boletas(l,page_content)
                else:
                    #body.append(leer_Facturas(l,page_content))
                    body+=leer_Facturas(l,page_content)
    
    #print(body)
    newlist=body.split('*')
    newlist.pop(len(newlist)-1)
    #print(newlist)
    for j in newlist:
        sublist=[]
        for k in j.split('//'):
            sublist.append(k)
        listota.append(sublist)

    MyDataToExcel = GetDToExcel('ReporteMensual')

    #item = []
    #item.append("abc")
    #item.append("lila")
    #item.append("ProductoA")
    #item.append("A")
    #item.append("papa")

    #print(listota)
    for fila in listota:
       Contentx=GetDContent(fila)
       MyDataToExcel.addContents(Contentx)
    MyDataToExcel.saveFile("ReporteDocumentos.xls")

else:
    print("No hay documentos a recuperar")
