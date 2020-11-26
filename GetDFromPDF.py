from funciones.UtilString import buscar_Indices
from GetDToExcel import GetDToExcel
from DocumentContent import DocumentContent
from DocumentFunc import *
import sys, os
import PyPDF2

#ruta 
path="pdfs/" 
content=""
documents=[]

try:
    documentsPDF= os.listdir(path) #documentos
except:
    print("No se puedo encontrar el directorio o archivo")

if len(documentsPDF)!=0:
    #numeros de documentos
    for l in documentsPDF:
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
                    content+=leer_Boletas(l,page_content)
                else:
                    content+=leer_Facturas(l,page_content)
    

    contentDocumentos=content.split('*')
    contentDocumentos.pop(len(contentDocumentos)-1)

    for j in contentDocumentos:
        sublist=[]
        for k in j.split('//'):
            sublist.append(k)
        documents.append(sublist)
    
    #Asignar Nombre a la hoja
    MyDataToExcel = GetDToExcel('ReporteMensual')
    #Generar documento en formato xls
    for document in documents:
       objDocumento=DocumentContent(document)
       MyDataToExcel.addContents(objDocumento)
    #Generar documento xls
    MyDataToExcel.saveFile("ReporteDocumentos.xls")

else:
    print("No hay documentos a recuperar")
