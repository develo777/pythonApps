import sys
import os
import fnmatch #libreria para buscar con comodines


while True:
    ipath=input('Ingresar ruta de ubicación: ')

    if len(ipath)==0:
        print ("No hay Ubicación")
        continue
    if len(ipath)<=3:
        print ("Ruta invalida de Ubicación")
        continue
    if True!=os.path.isdir(ipath):
        print ("Ruta invalida!")

    else:
        break

while True:
    iTextABuscar=input('Ingresar texto a Buscar: ')
    if len(iTextABuscar) <=0:
        print ("No hay texto a Buscar")
        continue
    else:
        break


# Funcion Buscar archivos 
#--------------------------------------------------------------------------
def search_file(path,fileToFind):
    #crear una lista vacia
    lsfilesFound=[]
    #busca entre arbol de directorios.
    for root,dirs,files in os.walk(path,topdown=True): #todo hacia abajo
        # recorrer todos los archivos
        for filename in files:
            #quitamos la extension y buscamos solo nombres
            # retorna un array
            root_ext=os.path.splitext(filename)
            #evalua si existe coincidencia con el texto a buscar
            if fnmatch.fnmatch(root_ext[0].lower(),'*'+fileToFind.lower() +'*'):
                #recuperar el nombre completo
                fullname= os.path.join(root,filename) 
                #agregar a nuestra lista de archivos encontrados
                lsfilesFound.append(fullname)
    return lsfilesFound

#imprimir lista de archivos encontrados
print("Archivos Encontrados:")
for filesencontrado in search_file(ipath,iTextABuscar):
    print(filesencontrado)
