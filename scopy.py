minombre='Charly'

def imprimir_nombre():
    global minombre
    minombre="Karloz"
    print('El nombre dentro de la funcion',minombre)

imprimir_nombre()
print('El nombre dentro de la funcion',minombre)