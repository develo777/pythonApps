import sys,os

pathG="i:\\marcasn\\avisosHtml\\2021"
path="I:\\MarcasN"
selectSubPath="AvisosHtml"
casoID="SD202100024"
textoToFind="878755.HTML"
# Buscar solo archivos 
#--------------------------------------------------
#for (root,dirs,files) in os.walk(path,topdown=True):
#    print(files)

# Buscar solo archivos bajo condicion 
#--------------------------------------------------
def search_file(path,textoToFind):
    FileFound=[]
    #busca entre arbol de directorios.
    for root,dirs,files in os.walk(path,topdown=True): #todo hacia abajo
        # recorrer todos los archivos
        for filename in files:
            #quitamos la extension y buscamos solo nombres
            # retorna un array
            root_ext=os.path.splitext(filename)
            #evalua si existe un archivo con el texto a buscar
            if root_ext[0] in textoToFind:
                #Imprimir el file encontrado
                print(root_ext[0]) 
                #agregar a nuestra lista de archivos encontrados
                FileFound.append(filename)
    return FileFound

print(search_file(pathG,textoToFind))
