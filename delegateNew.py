from bs4 import BeautifulSoup
from lxml import etree
import pandas as pd
import requests
import xlsxwriter
import sys,os

#path= 'fileDataGate/'
path= 'sourceDataGate/'
#url= 'sourceDataGate\data.html'

# contenido
content=""

#numero de documentos
documentsHTML= os.listdir(path)

if len(documentsHTML)!=0:
    for l in documentsHTML:
        with open(path+l,"r",encoding="utf8") as fp:
            content+=fp.read()
    
soup= BeautifulSoup(content,'html.parser')

#content=soup.find("mat-table")
trows= soup.find_all('mat-row')

#Header=["columna1","columna2","column3","columnx"]
Header=['check','Fecha','Emisor','Tipo','Documento','Cliente','Moneda','Monto','Estado']
rows=[]
#row =get las filas mat-row 
#i=numero de row desde 0
for counta, rowValue in enumerate(trows):

    #print (rowValue)
    celdas=rowValue.find_all('mat-cell')
    #print(celdas)
    row=[]
    for countb,celVal in enumerate(celdas):

        _value=celVal.text.replace("\n","")

        if  _value.startswith("USD"):
            row.append("USD")
            row.append(_value[3:len(_value):1].strip())
        else:
            if _value.startswith("EUR"):
                row.append("EUR")
                row.append(_value[3:len(_value):1].strip())
            else:
                if _value.startswith("PEN"):
                    row.append("EUR")
                    row.append(_value[3:len(_value):1].strip())
                else:
                    if _value.startswith("RC-"):
                        #row.append("NONE")
                        row.append(_value)
                        row.append("NONE")
                    else:
                        if _value.startswith(" - - - "):
                            row.append("0")
                            #row.append(_value)
                        else:
                            row.append(_value)


    rows.append(row)

#print (rows)
df= pd.DataFrame(rows[0:],columns=Header)
#print(df)
# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter("SourceDataGate.xlsx", engine='xlsxwriter') # pylint: disable=abstract-class-instantiated
#Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer,sheet_name='Publicadas')
# Get the xlsxwriter workbook and worksheet objects.
worksheet = writer.sheets['Publicadas']

#formatos 
writer.save()

            

