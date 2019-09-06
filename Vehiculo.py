class Vehiculo:
    posActual = (0,0)
    posAnterior = (0,0)
    actualizar = False
    sgteInter = 0
    nombre = ""

    comienzo = 0
    destino = 0

    rutaBruta = []
    rutaOpt = []
    time = 0

    termino = False

    def __init__(self, comienzo, destino, nombre):
        self.comienzo = comienzo
        self.destino = destino
        self.nombre = nombre

    def setDest(self, dest):
        self.destino = dest

    def nextPos(self):
        return self.rutaOpt[0]
