class Mensaje:

    titulo="titulo mensaje"
    isEnvidado=False

    def sendMensaje(self):
        self.isEnvidado=True
        
    def estado(self):
        if(self.isEnvidado):
            return "enviado"
        else:
            return "no enviado"

miMensaje=Mensaje()

miMensaje.sendMensaje()
print(miMensaje.estado())