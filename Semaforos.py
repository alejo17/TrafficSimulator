import sys
from random import *
from itertools import *
import time
import Vehiculo
import Ciudad
import Rutas

class Semaforos:

    maxTime = 10000
    flag = True

    m = Ciudad.Ciudad()
    vehiculos = []
    navi = Rutas.Rutas()
    bloqueados = []

    semaforos = {}
    estadoInter = {}
    largoRuta = {}

    totaltotal = []
    totalfinal = 0

    cont_vehi = {}
    cont_pos = {}

    suma = []

    def __init__(self):
        self.initialize()

    def initialize(self):
        # print "Inicializacion"
        self.cargarInter()
        self.cargarCalles()
        self.cargarSema()
        self.cargarLabel()
        self.navi.setCiudad(self.m)
        self.m.calcEntrantes()

        self.iniciarSemaforos()
        self.actualizarBloqueados()
        self.iniciarEstadoInter()

        #vehiculo1 = Vehiculo.Vehiculo(5, 30, "Porsche")
        #vehiculo2 = Vehiculo.Vehiculo(19, 18, "BMW")
        #vehiculo3 = Vehiculo.Vehiculo(27, 11, "Lambo")
        #self.vehiculos.append(vehiculo1)
        #self.vehiculos.append(vehiculo2)
        #self.vehiculos.append(vehiculo3)
        self.iniciarRandomVehiculos(50)
        self.calcularRutas()
        self.numberOfVehiculos = len(self.vehiculos)
        for c in self.vehiculos:
            self.largoRuta[c.nombre] = len(c.rutaOpt)
        for c in self.vehiculos:
            self.bloqueados.append(c.posActual)


    def iniciarRandomVehiculos(self, n):
        everywhere = self.m.intersecciones.keys()
        available = self.m.intersecciones.keys()
        for x in range(n):
            comienzo  = available[randint(0,len(available)-1)]
            final  = everywhere[randint(0,len(everywhere)-1)]
            nombre = "vehiculo" + str(x)
            if not comienzo == final:
                self.vehiculos.append( Vehiculo.Vehiculo(comienzo, final, nombre) ) #### en comienzo y final poner indices del 0 al 30
            available.remove(comienzo)

    def iniciarEstadoInter(self):
        # dos calles o menos siempre verde
        for i in self.m.intersecciones:
            if self.m.cuantos[i] <= 2:
                self.estadoInter[i] = "VERDE"
            else:
                self.estadoInter[i] = "ROJO"
        self.actEstadoInter()

    def iniciarSemaforos(self):
        for i in self.m.intersecciones:
            state = {}
            state['Verde'] = []
            state['Rojo'] = self.m.entrantes[i]
            self.semaforos[i] = state

    def cargarInter(self):
        f = open('interNY.txt', 'r')
        for line in f:
            line = line.split()
            self.m.agregarInter(int(line[0]), float(line[1]), float(line[2]))
        f.close()

    def cargarSema(self):
        f = open('semaCenPark.txt', 'r')
        for line in f:
            line = line.split()
            self.m.agregarSema(int(line[0]), float(line[1]), float(line[2]), int(line[3]) )
        f.close()

    def cargarLabel(self):
        f = open('semaNYlabel.txt', 'r')
        for line in f:
            line = line.split()
            self.m.agregarLabel(int(line[0]), float(line[1]), float(line[2]), int(line[3]) )
        f.close()

    def cargarCalles(self):
        f = open('unirInterNY.txt', 'r')
        for line in f:
            line = line.split()
            to = int(line.pop(0))
            for remaining in line:
                self.m.agregarCalle(int(remaining), to, 0)
        f.close()

        # todas las distancias 10
        for x in self.m.calles:
            x[-1] = 10

    def calcCuantos(self):
        # cont = 0
        # for i,j in enumerate(self.vehiculos):
        #     for k in self.vehiculos[i+1:]:
                # print j.posActual[0],k.posActual[0]
                # if ( j.posActual[0] == k.posActual[0] ):
                    # print "yesss"+str(j.posActual[0])
                    # cont += 1


        for l in range(0, 194): ## cantidad de calles
            self.cont_vehi[l] = []

        for l in range(0, 194):
            self.cont_pos[l] = []

        for i,j in enumerate(self.vehiculos):
            if len(self.cont_vehi) > 0:
                for v, w in self.cont_vehi.items():
                    if i in w:
                        del w[w.index(i)]
                try:
                    self.cont_vehi[j.posActual[0]] = self.cont_vehi[j.posActual[0]] +[i]
                    self.cont_pos[j.posActual[0]] = [j.posActual[0],j.posActual[1]]
                except NameError:
                    self.cont_vehi[j.posActual[0]] = [i]
            else:
                self.cont_vehi[j.posActual[0]] = [i]
                self.cont_pos[j.posActual[0]] = [j.posActual[0],j.posActual[1]]

        # for v,w in self.cont_vehi.items():
            # print len(w)

    def calcParadas(self):
        cont = 0
        for i in self.semaforos.values(): ### dict -> keys (Rojo o verde)
            for v,w in i.items(): ##recorro el array con esos keys
                if v=="Rojo":
                    for i,j in self.cont_vehi.items(): ### i -> indice de calle   j -> array de cuantos en esa calle
                        for k in w: ## recorro rojos y veo si tienen carro y la misma calle del carro
                            if len(j)>0 and k==i:
                                cont+=1

        self.suma.append(cont)
        # print self.suma
        # paradas = 0
        # print len(self.suma)
        # print paradas



    def printVehiculos(self):
        rpta=""
        # for c in self.vehiculos:
            # rpta += c.nombre + " en " + str(c.posActual) + " con ruta a " + str(c.rutaOpt[:5]) + "\n\n"
            # print c.nombre + " en " + str(c.posActual) + " con ruta a " + str(c.rutaOpt[:5])
        # file = open("test","a")
        # file.write(rpta)
        # file.close()
        return 0

    def printState(self):
        # print '\n### intersecciones: '
        # print self.m.intersecciones
        # print '### calles: '
        # print self.m.calles
        # print '### entrantes: '
        # print self.m.entrantes
        # print '### cuantos: '
        # print self.m.cuantos
        # print '### semaforos: '
        # print self.semaforos
        # print '### estados de las intersecciones: '
        # print self.estadoInter
        # print '### vehiculos: '
        # self.printVehiculos()
        # print '\n'
        # file = open("test","a")
        # i = 0
        # for i in self.m.intersecciones:
        #     file.write(self.estadoInter[str(i)])
        #     i = i + 1
        # file.close()
        return 0

    def calcularRutas(self):
        # dar siempre una ruta
        for c in self.vehiculos:
            c.rutaBruta = self.navi.dijkstra(c.comienzo, c.destino)

        # ver si es que hay ruta opt
        for c in self.vehiculos:
            c.rutaOpt = self.navi.calcRuta(c.rutaBruta)

        # dependiendo de su pos ver cual le sigue
        for c in self.vehiculos:
            c.sgteInter = c.rutaBruta[1]
            street = self.m.encontrarCalle(c.comienzo, c.sgteInter)
            c.posActual = (street, 0)

    def run(self, total):
        s = time.time()

        #self.prueba(11, 11, total)
        self.cambioCamara(self.cont_vehi,total)
        # self.prueba2(10, total)
        if len(self.vehiculos) == 0:
            print("Todos los vehiculos llegaron a su destino!! ... tiempo:")
            sys.exit(self.tiempo())
        self.timeStep()
        if self.flag:
            self.calcCuantos()
            self.calcParadas()
            self.printVehiculos()
            # print self.estadoInter
        # chequea si llego a su destino
        for c in self.vehiculos[::-1]:
            if c.termino:
                self.bloqueados.remove(c.posActual)
                self.vehiculos.remove(c)

        f = time.time()
        self.totaltotal.append(f-s)

    def tiempo(self):
        for i in self.totaltotal:
            self.totalfinal = self.totalfinal + i
        return self.totalfinal

    def puedePasar(self, vehiculo):
        return not (vehiculo.nextPos() in self.bloqueados)

    def timeStep(self):
        for c in self.vehiculos:
            if not c.termino:
                if self.puedePasar(c):
                    if c.posActual in self.bloqueados:
                        self.bloqueados.remove(c.posActual)
                    c.posAnterior = c.posActual
                    c.posActual = c.rutaOpt.pop(0)
                    self.bloqueados.append(c.posActual)
                    c.actualizar = True
                    if len(c.rutaOpt) == 0:
                        c.termino = True

    def actualizarBloqueados(self):
        for i in self.m.intersecciones.keys():
            for g in self.semaforos[i]['Verde']:
                street = self.m.ultimaPos(g)
                if street in self.bloqueados:
                    self.bloqueados.remove(street)
            for r in self.semaforos[i]['Rojo']:
                # print "Rojo"
                # print (i,r)
                street = self.m.ultimaPos(r)
                if street  not in self.bloqueados:
                    self.bloqueados.append(street)

    def aVerde(self, inter, street):
        self.semaforos[inter]['Rojo'].remove(street)
        self.semaforos[inter]['Verde'].append(street)
        self.actualizarBloqueados()

    def aRojo(self, inter, street):
        self.semaforos[inter]['Verde'].remove(street)
        self.semaforos[inter]['Rojo'].append(street)
        self.actualizarBloqueados()

    def actEstadoInter(self):
        for i in self.estadoInter.keys():
            if self.estadoInter[i] == 'ROJO':
                self.semaforos[i]['Verde'] = []
                self.semaforos[i]['Rojo'] = self.m.entrantes[i]
            if self.estadoInter[i] == 'VERDE':
                self.semaforos[i]['Rojo'] = []
                self.semaforos[i]['Verde'] = self.m.entrantes[i]
            if self.estadoInter[i] == 'horizontal': # se requiere 4 inter
                rojos = []
                verdes = []
                nghs = self.m.entrantes[i]
                rojos.append(nghs[0])
                rojos.append(nghs[2])
                verdes.append(nghs[1])
                verdes.append(nghs[3])
                self.semaforos[i]['Rojo'] = rojos
                self.semaforos[i]['Verde'] = verdes
            if self.estadoInter[i] == 'vertical':     # se requiere 4 inter
                rojos = []
                verdes = []
                nghs = self.m.entrantes[i]
                rojos.append(nghs[1])
                rojos.append(nghs[3])
                verdes.append(nghs[0])
                verdes.append(nghs[2])
                self.semaforos[i]['Rojo'] = rojos
                self.semaforos[i]['Verde'] = verdes
            if self.estadoInter[i] == 'hor_izq':        # se requiere 4 inter
                pass
            if self.estadoInter[i] == 'ver_izq':         # se requiere 4 inter
                pass
        self.actualizarBloqueados()

    def cambiarEstadoInter(self, inter, mode):
        self.estadoInter[inter] = mode
        self.actEstadoInter()

    #cambio de hor a ver o al reves
    def swapEstadoInter(self, inter):
        if self.estadoInter[inter] == 'horizontal':
            self.estadoInter[inter] = 'vertical'
        else:       # default para ROJO o VERDE
            self.estadoInter[inter] = 'horizontal'
        self.actEstadoInter()

    # cambio random de estados
    def prueba(self, par1, par2, cont):
        # s = time.time()
        signal = [0 for y in range(self.maxTime)]
        for i in range(self.maxTime):
            if i%par1 == 0:
                signal[i] = 1

        if signal[cont] == 1:
            for x in range(par2):
                i = randint(0,len(self.m.cuatroInter)-1)
                self.swapEstadoInter(self.m.cuatroInter[i])

        # f = time.time()
        # self.totaltotal.append(f-s)

    def prueba2(self, par, cont):
        signal = [int(float(i)/par) % 2 for i in range(self.maxTime)]
        # print signal
        if signal[cont] == 0:
            for i in self.m.cuatroInter:
                self.cambiarEstadoInter(i, 'horizontal')
        else:
            for i in self.m.cuatroInter:
                self.cambiarEstadoInter(i, 'vertical')

    def cambioCamara(self, cont_dict, cont):
        milen = 0
        rpta = ""
        # file = open("testV","a")
        for v,w in cont_dict.items():

            milen = len(w)
            if milen > 1:
                self.prueba(1,1,cont)
                # rpta+= "entro al 3" + " " + str(milen) + " "
            else:
                self.prueba(11,11,cont)
                # rpta+= "entro al 11" + " " + str(milen) + " "

        # file.write(rpta)
        # file.close()


    def cambioDataReal(self, json, cont):
        JF = 0
        rpta = ""
        iter = 1
        for v,w in json.items():

            JF = json[iter]

            if JF > 0.5:
                self.prueba(1,1,cont)
            else:
                self.prueba(11,11,cont)

            iter+=2