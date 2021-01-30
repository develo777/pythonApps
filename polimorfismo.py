class Coche():
    def desplazamiento(self):
        print("me desplazo usando cuetro ruedas")

class Moto():
    def desplazamiento(self):
        print("me desplazo usando dos ruedas")

class Camion():
    def desplazamiento(self):
        print("me desplazo usando 6 ruedas")

def desplazamiento(vehiculo):
    vehiculo.desplazamiento()

myVehiculo3=Moto()
desplazamiento(myVehiculo3)


