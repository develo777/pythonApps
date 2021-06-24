import xlsxwriter
import pymssql
import pandas as pd
import sys,os
# Import the byte stream handler.
from io import BytesIO


#headers
header=['Nmarcas','Titular','Marca','Figura']
#header=['Figura']

connString = pymssql.connect(server='S-DATOS4', user='BMA', password='', database='BMA')  
cursor = connString.cursor()
#parametrs
arg= '01/01/2021','01/05/2021'
#procedure
cursor.callproc("spMarcasFigurativasByTitular",arg)
cursor.nextset()
#get results
data= cursor.fetchall()
cursor.close()
connString.close()
#create a pandas dataframe from the data
df= pd.DataFrame(data=data,columns=header)
dfx=df['Figura'] #get column form  data

#df.groupby('Titular')
#create a pandas excel write using xlswrite as the engine.
writer =pd.ExcelWriter('figuras.xlsx',engine='xlsxwriter')
#convert the dataframe to an xlswriter  excel object
dfx.to_excel(writer,sheet_name='Sheet1')
# close the Pandas Excel writer and output the excel file
#writer.save()
#print(df)
#workbook= xlsxwriter.Workbook('figura.xlsx')
workbook= writer.book
worksheet = writer.sheets['Sheet1']
worksheet.write(0,0,'z')
workbook.close()



