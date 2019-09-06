import Ciudad

class Rutas:
    m = Ciudad.Ciudad()
    grafo = {}

    def setCiudad(self, m):
        self.m = m
        for node in m.calles:
            if node[0] not in self.grafo:
               self.grafo[node[0]] = {node[1]: node[2]}
            else:
                self.grafo[node[0]][node[1]] = node[2]
            if node[1] not in self.grafo:
                self.grafo[node[1]] = {node[0]: node[2]}
            else:
                self.grafo[node[1]][node[0]] = node[2]

    def dijkstra(self, comienzo, final):#CALCULAR RUTAAA *******
        distancias = {}
        predecesores = {} ## siguiente punto q le toca pasar
        a_evaluar = self.grafo.keys()
        for node in self.grafo:
            distancias[node] = float('inf')### infinitooo a todo
            predecesores[node] = None ### null a todo
        sp_set = [] ### path de cada carros
        distancias[comienzo] = 0
        while len(sp_set) < len(a_evaluar):  ### condicion para que no recorra todos los nodos
            adentro = {node: distancias[node] for node in [node for node in a_evaluar if node not in sp_set]}
            mas_cercano = min(adentro, key=distancias.get)
            sp_set.append(mas_cercano)
            for node in self.grafo[mas_cercano]:
                if distancias[node] > distancias[mas_cercano] + self.grafo[mas_cercano][node]:
                    distancias[node] = distancias[mas_cercano] + self.grafo[mas_cercano][node]
                    predecesores[node] = mas_cercano
        path = [final]

        while comienzo not in path:
            path.append(predecesores[path[-1]])
        result = path[::-1]

        return result

    def calcRuta(self, camino):
        opt = []
        for w in range(len(camino) - 1) :
            street = self.m.encontrarCalle(camino[w], camino[w+1])
            length = self.m.calles[street][-1]
            for i in range(length):
                opt.append((street, i + 1))
        return opt
