from bs4 import BeautifulSoup
from lxml import etree
import pandas as pd
import requests
import xlsxwriter

url= 'sourceDataGate\data.html'
page=open(url,encoding="utf8")
soup= BeautifulSoup(page.read(), 'html.parser')
content=soup.find("mat-table")
trows= content.find_all('mat-row')

#Columnas
Header=['check','Fecha','Emisor','Tipo','Documento','Cliente','Monto','Estado']
#Filas
rows= []

for i, row in enumerate(trows):
    #numero de filas
    #print(row)
    tds= row.find_all('mat-cell')
    row= []
    for j, td in enumerate(tds):
        #numero de indice de columnas
        #if td.text<>'RESUMEN DIARIO':
        row.append(td.text.replace("\n",""))
    rows.append(row)
    


df= pd.DataFrame(rows[0:],columns=Header)

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter("SourceDataGate.xlsx", engine='xlsxwriter') # pylint: disable=abstract-class-instantiated
#Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer,sheet_name='Publicadas')
# Get the xlsxwriter workbook and worksheet objects.
worksheet = writer.sheets['Publicadas']

#formatos 
writer.save()
#print(df)