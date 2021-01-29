class Vehiculos():

    def __init__(self,marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frenar=False
    
    def arrancar(self):
        self.enmarcha=True
    def acelerar(self):
        self.acelera=True
    def frenar(self):
        self.frenar=True
    def estado(self):
        print("Marca:", self.marca,"\nModelo:",self.modelo)

class Furgoneta(Vehiculos):
    def carga(self,cargar):
        self.cargado=cargar
        if(self.cargado):
            return "la furgoneta esta cargada"
        else:
            return "la furgoneta no esta cargada"


class Moto(Vehiculos):
    hcaballito=""

    def caballito(self):
        self.hcaballito="voy haciendo el caballito"
    
    def estado(self):
        print("Marca:", self.marca,"\nModelo:",self.modelo,"\h",self.hcaballito)

class VEElectricos():
    def __init__(self,marca,modelo):
        super().__init__(marca,modelo)
        self.autonomia=100
    def cagarEnergia(self):
        self.cargando =True;    

myMoto = Moto("Honda","T20201")
myMoto.caballito()
myMoto.estado()

myfurgoneta = Furgoneta("Renault","Kangoo")
myfurgoneta.arrancar()
myfurgoneta.estado()
print(myfurgoneta.carga(True))

class BicicletaElectrica(VEElectricos,Vehiculos):
    pass

mibici=BicicletaElectrica("ninja","800")