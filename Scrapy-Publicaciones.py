from bs4 import BeautifulSoup
from lxml import etree
import pandas as pd
import requests
import xlsxwriter


url= 'http://sistemas.indecopi.gob.pe/OsdConsultasPublicas/Marcas_Solicitadas/principal.asp?Fecha_Presentacion=2021-03-15'

response= requests.get(url)

soup= BeautifulSoup(response.content.decode('utf8','ignore'),'lxml')
content=soup.find("table")
subcontent= content.find("table")
childcontent= subcontent.find("table")
trows= childcontent.find_all('tr')
#Columnas
Header=['Nro. de Expediente','Tipo de Expediente','Tipo de Solicitud','Signo Solicitado','Clase','Tipo de signo','NCertificado']
#Filas
rows= []

for i, row in enumerate(trows):
    tds= row.find_all('td')
    row= []
    for j, td in enumerate(tds):
                row.append(td.text.replace("\r\n",""))
    rows.append(row)

#data
df= pd.DataFrame(rows[2:],columns=Header)
df.insert(1,'Fecha de publicación',"")
df.insert(2,'Fe de erratas',"")
df.insert(3,'Publicación sin efectos',"")
df.insert(4,'Fecha limite oposición',"")
df.insert(5,'Fecha de presentación',"")

columna = df['Tipo de Solicitud']
del df['Tipo de Solicitud']
df.insert(6,'Tipo de Solicitud',columna)
df.insert(7,'Fecha de primer uso',"")
df.insert(8,'Solicitante',"")
columna = df['Clase']
del df['Clase']
df.insert(9,'Clase',columna)
df.insert(10,'Consulta Expedientes',"")
del df['Tipo de Expediente']
del df['NCertificado']
df.insert(13,'País del solicitante',"")


# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter("publicadas.xlsx", engine='xlsxwriter') # pylint: disable=abstract-class-instantiated
#Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer,sheet_name='Publicadas')
# Get the xlsxwriter workbook and worksheet objects.

worksheet = writer.sheets['Publicadas']
#formatos 


worksheet.set_column('B:B',25,'')
worksheet.set_column('C:C',15,'')
worksheet.set_column('D:D',15,'')
worksheet.set_column('E:E',15,'')
worksheet.set_column('F:F',15,'')
worksheet.set_column('G:G',15,'')
worksheet.set_column('H:H',30,'')



writer.save()