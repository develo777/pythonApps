import pymssql
import pandas as pd
import sys,os

#path
path='T:\\T02 Computo\\Proyectos\\Scripts\\BMA - Signos Distintivos - SolicitudesRegistro - EnEspera - IngresoAlSistema.sql'

#contenido
content=""

def parse_sql(filename):

    data = open(filename, 'r').readlines()
    stmts = []
    DELIMITER = ';'
    stmt = ''

    for lineno, line in enumerate(data):
        if not line.strip():
            continue

        if line.startswith('--'):
            continue

        if 'DELIMITER' in line:
            DELIMITER = line.split()[1]
            continue

        if (DELIMITER not in line):
            stmt += line.replace(DELIMITER, ';')
            continue

        if stmt:
            stmt += line
            stmts.append(stmt.strip())
            stmt = ''
        else:
            stmts.append(line.strip())
    return stmts


with open(path,'r') as fp:
    sql=parse_sql(fp.read())


 #select * from    dbo.tblreportes
connString = pymssql.connect(server='S-DATOS4', user='BMA', password='', database='BMA')  
cursor = connString.cursor()
cursor.execute(sql)

row=cursor.fetchone()
while row:
    colx=row[1]
    row = cursor.fetchone() 
    print(colx)
cursor.close()
connString.close()

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

