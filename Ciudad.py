class Ciudad:
    intersecciones = {}
    calles = []
    entrantes = {}
    cuantos = {} ## de cada inter cuantas calles
    cuatroInter = []
    dibusema = {}
    dibulabel = {}

    def agregarLabel(self, index, x, y, labelinter):
        self.dibulabel[index] = [x,y,labelinter]

    def agregarSema(self, index, x, y, semainter):
        self.dibusema[index] = [x,y,semainter]

    def agregarInter(self, index, x, y):
        self.intersecciones[index] = [x,y]

    def agregarCalle(self, From, To, length):
        s = [From, To, length]
        self.calles.append(s)

    def encontrarCalle(self, comienzo, finish):
        t = [comienzo, finish]
        for s in self.calles:
            if s[:2] == t:
                return self.calles.index(s)
        print ("No existe")

    def calcEntrantes(self):### es calcular las intersecciones
        for i in self.intersecciones:
            result = []
            for s in self.calles:
                if s[1] == i:
                    result.append(self.calles.index(s))
            self.entrantes[i] = result
            self.cuantos[i] = len(result)
        self.cuatroInter = [i for i in self.intersecciones if self.cuantos[i] == 4]

    def ultimaPos(self, street):
        length = self.calles[street][2]
        return (street,length)

    def calcDist(self, node1, node2, l):
        s1 = self.encontrarCalle(node1, node2)
        s2 = self.encontrarCalle(node2, node1)
        self.calles[s1][2] = l
        self.calles[s2][2] = l
