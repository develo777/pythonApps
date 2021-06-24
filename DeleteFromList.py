import re
textoAbuscar="b"

months=['Enero','febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Setiembre','Octubre','Noviembre','Diciembre']
#Month=['Enero','Marzo','Mayo','Junio','Julio','Agosto','Setiembre','Noviembre']
elements=[]
#print(len(months))

for i in range(len(months)-1,-1,-1):
    #print(months[i])
    x=months[i]
    if re.search(textoAbuscar,x):
        months.remove(months[i])
print(months)
