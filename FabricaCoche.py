class Coche():

    def __init__(self):
        self.__largoChasis=80
        self.__anchoChasis=80
        self.__ruedas=4
        self.__enmarcha=False

    def arrancar(self, arrancamos):
        self.__enmarcha=arrancamos
        if (self.__enmarcha):
            chekeo=self.__verificar_funcionamiento()
        if (self.__enmarcha and chekeo):
            return "el coche esta en marcha"
        else:
            return "el coche esta detenido"


    def __verificar_funcionamiento(self):
        print("realizando chekeo interno")
        self.gasolina ="mal"
        self.aceite="ok"
        self.puertas="cerradas"

        if (self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False





        

mycoche1=Coche()
print("se creo el nuevo auto")
print(mycoche1.arrancar(True))


