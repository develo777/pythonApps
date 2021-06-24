import pyodbc
import pandas as pd
import sys,os

#path
path='T:\\T02 Computo\\Proyectos\\Scripts\\BMA - Signos Distintivos - SolicitudesRegistro - EnEspera - IngresoAlSistema.sql'

#contenido
content=""

with open(path,"r") as fp:
    content=fp.read()

#print(content)

server_name ='s-datos4'
database_name='BMA'
username='bma'
password=''


 #select * from    dbo.tblreportes

connString = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER='+ server_name +';Database='+ database_name+';UID='+username+';PWD='+password)
#conn=pyodbc.connect(connString)
cursor = connString.cursor()
SQLquery= pd.read_sql_query(""+content+"",connString)
#SQLquery= pd.read_sql_query('select * from dbo.tblreportes',connString)
print(SQLquery)


#df= pd.DataFrame(SQLquery,columns=['id','descripcion'])
#df.to_excel(r'exports/listReportes.xlsx', sheet_name='cartas',index = True,header=True)
#print(df)
#print(type(df))
#print(df)

#cursor.execute("select * from dbo.tblreportes")
#row = cursor.fetchone()
#while row:
#    print(row[0])
#    row = cursor.fetchone()

