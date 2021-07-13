from bs4 import BeautifulSoup
from lxml import etree
import pandas as pd
import requests
from openpyxl.styles import PatternFill

url= 'http://sistemas.indecopi.gob.pe/OsdConsultasPublicas/Marcas_Solicitadas/principal.asp?Fecha_Presentacion=2021-03-15'

response= requests.get(url)

soup= BeautifulSoup(response.content.decode('utf8','ignore'),'lxml')
content=soup.find("table")
subcontent= content.find("table")
childcontent= subcontent.find("table")
trows= childcontent.find_all('tr')
#Columnas
Header=['Nro. de Expediente','Tipo de Expediente','Tipo de Solicitud','Marca','Clase','Presentación','N°. Certificado']
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
# Create a Pandas Excel writer using openpyxl as the engine.
writer = pd.ExcelWriter("publicadas.xlsx", engine='openpyxl') # pylint: disable=abstract-class-instantiated

writer['A1'].fill = PatternFill(bgColor="FFC7CE", fill_type = "solid")

#Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer,sheet_name='Publicadas')


writer.save()