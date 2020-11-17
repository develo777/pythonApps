from funciones.mod_Content import buscar_Indices
#Funcion para limpiar Monto
def limpiar_Monto_Total(contenido,textoABuscar):
    pos=buscar_Indices(contenido,textoABuscar)
    nuevoLen=pos[0]+3
    monto=contenido[0:nuevoLen]
    return monto
#leer boletas
def leer_Boletas(nombre_doc,page_content):
    
    numDocuments=[]
    mTotal=[]
    rows=""
    indice=0

    posNDocuments=buscar_Indices(page_content,"B001-")
    posTMonedae=buscar_Indices(page_content,"EUR./")
    posTMonedau=buscar_Indices(page_content,"USD./")

    if len(posTMonedae)==0:
        posMTotals=posTMonedau
        tipoMoneda="USD"
    else:
        posMTotals=posTMonedae
        tipoMoneda="EUR"

    #recuperar los numeros de documentos
    for posj in posNDocuments:
        numDocuments.append(page_content[posj:posj+11])
    #recuperar los montos
    for posk in posMTotals:
        mTotal.append(limpiar_Monto_Total(page_content[posk+5:posk+13].strip(),"."))

    #recorrer los indices y tomar los valores
    while indice < len(numDocuments):
        rows+="<tr><td>"+nombre_doc+"</td><td>"+str(indice+1)+"</td><td>BOLETA</td><td>"+numDocuments[indice]+"</td><td>"+tipoMoneda+"</td><td>"+mTotal[indice]+"</td></tr>"
        indice+=1   
    return rows    
#leer facturas        
def leer_Facturas(nombre_doc,page_content):

    #Numero de Factura
    posAi=page_content.find("Nro.")
    numFactura =page_content[posAi+4:posAi+16]
    #Tipo de Moneda
    posTMoneda=page_content.find("Moneda")
    tipoMoneda =page_content[posTMoneda+7:posTMoneda+12]
    if tipoMoneda=="SOLES":
        tipoMoneda=tipoMoneda
    else:
        tipoMoneda="USD"
    #MontoTotal
    posMontoTotal=page_content.find("Importe")
    montoTotal =page_content[posMontoTotal-50:posMontoTotal]
    montoTotalx=buscar_Indices(montoTotal,".")
    #print(montoTotal)
    #print(montoTotalx)
    countA=len(montoTotalx)
    #print(mt)
    lastpos=montoTotalx[countA-1]
    antpos=montoTotalx[countA-2]
    #print(antpos)
    #print(lastpos)
    busant1=montoTotal[antpos:antpos+3]
    busant2=montoTotal[lastpos:lastpos+3]

    if busant1==busant2:
        search_t=montoTotal.replace(str(busant1), str(busant1)+"/")
    else:
        search_t=montoTotal.replace(str(busant1), str(busant1)+"/")
        search_t=search_t.replace(str(busant2), str(busant2)+"/")
    
    newArray=search_t.split('/')
    #print(newArray)
    #print(len(newArray))
    LasIndex=len(newArray)-2
    #print(LasIndex)
    Monto=newArray[LasIndex]
    return "<tr><td>"+nombre_doc+"</td><td>"+str(1)+"</td><td>FACTURAS</td><td>"+str(numFactura)+"</td><td>"+tipoMoneda+"</td><td>"+str(Monto)+"</td></tr>"
#crear documento html