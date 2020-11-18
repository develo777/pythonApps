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
        rows+=str(1)+'//'+nombre_doc+'//'+str(indice)+'//'+'BOLETAS'+'//'+numDocuments[indice]+'//'+tipoMoneda+'//'+mTotal[indice]+'*'
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
    countA=len(montoTotalx)
    #Tomar las ultimas posiciones la antepenultima y la ultima  
    lastpos=montoTotalx[countA-1]
    antpos=montoTotalx[countA-2]

    busant1=montoTotal[antpos:antpos+3]
    busant2=montoTotal[lastpos:lastpos+3]
    #Si hay coincidencia entre los numeros realizar un replazo por cada numeros
    if busant1==busant2:
        search_t=montoTotal.replace(str(busant1), str(busant1)+"/")
    else:
        search_t=montoTotal.replace(str(busant1), str(busant1)+"/")
        search_t=search_t.replace(str(busant2), str(busant2)+"/")
    
    newArray=search_t.split('/')
    LasIndex=len(newArray)-2
    Monto=newArray[LasIndex]
    return str(1)+'//'+nombre_doc+'//'+str(1)+'//'+'FACTURAS'+'//'+str(numFactura)+'//'+tipoMoneda+'//'+str(Monto)+'*'
# crear documento html
def crear_Html(html_content):
    value = -1
    try:
        archivo=open("Documentos.html","w")
        headerHtml="<!DOCTYPE html><html><head><mETA charset='utf-8' /><title>documento generedo</title></head><body><table>"
        fotterHtml="</body></html>"
        archivo.write(headerHtml+html_content+fotterHtml)
        archivo.close()
        value =0
    except:
        print("error al generar documento html")
    return value 