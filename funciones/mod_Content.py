#Funcion para buscar posiciones de textoABuscar
def buscar_Indices(contenido,textoABuscar):
    posiciones=[]
    length =len(contenido)
    index=0
    while index < length:
        i=contenido.find(textoABuscar,index)
        if i==-1:
            return posiciones
        posiciones.append(i)
        index =i+1
    return posiciones