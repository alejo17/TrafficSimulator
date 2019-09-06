from Tkinter import *
import Semaforos
import time

class Visual(Frame):
    # estaba width = 900
    # estaba height = 600
    width = 1000
    height = 700

    total = 1
    mas = Semaforos.Semaforos()

    # estaba scaling = 13.0
    scaling = 2.2

    tamInter = 4

    # estaba origin = [50, 50]
    origin = [-330, -120]

    dibujar = False
    color = "green"

    def __init__(self, master=None):
        self.iniciarFrames(master)
# ****************************************************************************************************************************************
        self.iniciarCiudad()
        self.after(10, self.update)
       # self.origin = [self.width / 2, self.height / 2]

    def iniciarFrames(self, master):
        Frame.__init__(self, master)
        Pack.config(self)
        self.createWidgets()

    def iniciarCiudad(self):
        self.mas.printState()
        for inter in self.mas.m.intersecciones:
            self.drawInter(inter, self.scaling * self.mas.m.intersecciones[inter][0] + self.origin[0], self.scaling * self.mas.m.intersecciones[inter][1] + self.origin[1])
        #estaba
        #for i in self.mas.m.dibusema:
            ##estabvaself.drawSema(i, self.scaling * self.mas.m.dibusema[i][0]+50, self.scaling * self.mas.m.dibusema[i][1]+50,"red")
            #self.drawSema(i, self.scaling *self.mas.m.dibusema[i][0]+ self.origin[0], self.scaling *self.mas.m.dibusema[i][1]+ self.origin[1],"red")
        for street in self.mas.m.calles:
            self.drawCalle(street)
        for vehiculo in self.mas.vehiculos:
             self.drawVehiculo(vehiculo)

    # def drawGrid(self):
    #     for a in range(0, self.height, 50):
    #         for b in range(0, self.width, 50):
    #             self.draw.create_rectangle(a-self.tamInter, b-self.tamInter, a+self.tamInter  ,b+self.tamInter , fill="green")
    #     a = self.origin[0]
    #     b = self.origin[1]
    #     self.draw.create_rectangle(a-self.tamInter, b-self.tamInter, a+self.tamInter  ,b+self.tamInter , fill="red")

    def myprint(self,d):
        stack = d.items()
        while stack:
            k, v = stack.pop()
            if isinstance(v, dict):
                stack.extend(v.iteritems())
            else:
                print(v)

    def update(self, *args):
        self.mas.run(self.total)
        self.total += 1
        self.mas.printVehiculos()

        #print self.mas.estadoInter
        # file = open("testV","a")
        # rpta=""
        # rpta += str(j[2])
        # self.myprint(self.mas.semaforos)

# ****************************************************************************************************************************************
# ****************************************************************************************************************************************
        for i,j in self.mas.m.dibusema.items(): ## 60
            for k,l in self.mas.estadoInter.items(): #### 30
                if ( j[2] == k and i % 4 == 0  and  l == "horizontal" ):
                    col = "green"
                    self.drawSema(i, self.scaling * self.mas.m.dibusema[i][0] + self.origin[0], self.scaling * self.mas.m.dibusema[i][1] + self.origin[1],col)
                    self.drawSema(i, self.scaling * self.mas.m.dibusema[i+3][0] + self.origin[0], self.scaling * self.mas.m.dibusema[i+3][1] + self.origin[1],col)
                    col = "red"
                    self.drawSema(i, self.scaling * self.mas.m.dibusema[i+1][0] + self.origin[0], self.scaling * self.mas.m.dibusema[i+1][1] + self.origin[1],col)
                    self.drawSema(i, self.scaling * self.mas.m.dibusema[i+2][0] + self.origin[0], self.scaling * self.mas.m.dibusema[i+2][1] + self.origin[1],col)
                if ( j[2] == k and i % 4 == 1 and  l == "vertical" ):
                    col = "green"
                    self.drawSema(i, self.scaling * self.mas.m.dibusema[i][0] + self.origin[0], self.scaling * self.mas.m.dibusema[i][1] + self.origin[1],col)
                    self.drawSema(i, self.scaling * self.mas.m.dibusema[i+1][0] + self.origin[0], self.scaling * self.mas.m.dibusema[i+1][1] + self.origin[1],col)
                    col = "red"
                    self.drawSema(i, self.scaling * self.mas.m.dibusema[i-1][0] + self.origin[0], self.scaling * self.mas.m.dibusema[i-1][1] + self.origin[1],col)
                    self.drawSema(i, self.scaling * self.mas.m.dibusema[i+2][0] + self.origin[0], self.scaling * self.mas.m.dibusema[i+2][1] + self.origin[1],col)
                if ( j[2] == k and i % 4 == 2 and  l == "vertical" ):
                    col = "green"
                    self.drawSema(i, self.scaling * self.mas.m.dibusema[i][0] + self.origin[0], self.scaling * self.mas.m.dibusema[i][1] + self.origin[1],col)
                    self.drawSema(i, self.scaling * self.mas.m.dibusema[i-1][0] + self.origin[0], self.scaling * self.mas.m.dibusema[i-1][1] + self.origin[1],col)
                    col = "red"
                    self.drawSema(i, self.scaling * self.mas.m.dibusema[i-2][0] + self.origin[0], self.scaling * self.mas.m.dibusema[i-2][1] + self.origin[1],col)
                    self.drawSema(i, self.scaling * self.mas.m.dibusema[i+1][0] + self.origin[0], self.scaling * self.mas.m.dibusema[i+1][1] + self.origin[1],col)
                if ( j[2] == k and i % 4 == 3 and  l == "horizontal" ):
                    col = "green"
                    self.drawSema(i, self.scaling * self.mas.m.dibusema[i][0] + self.origin[0], self.scaling * self.mas.m.dibusema[i][1] + self.origin[1],col)
                    self.drawSema(i, self.scaling * self.mas.m.dibusema[i-3][0] + self.origin[0], self.scaling * self.mas.m.dibusema[i-3][1] + self.origin[1],col)
                    col = "red"
                    self.drawSema(i, self.scaling * self.mas.m.dibusema[i-1][0]+ self.origin[0], self.scaling * self.mas.m.dibusema[i-1][1] + self.origin[1],col)
                    self.drawSema(i, self.scaling * self.mas.m.dibusema[i-2][0] + self.origin[0], self.scaling * self.mas.m.dibusema[i-2][1] + self.origin[1],col)
                if ( j[2] == k and l == "VERDE" ):
                    col = "green"
                    self.drawSema(i, self.scaling * self.mas.m.dibusema[i][0] + self.origin[0], self.scaling * self.mas.m.dibusema[i][1] + self.origin[1],col)
                if ( j[2] == k and l == "ROJO" ):
                    col = "red"
                    self.drawSema(i, self.scaling * self.mas.m.dibusema[i][0] + self.origin[0], self.scaling * self.mas.m.dibusema[i][1] + self.origin[1],col)


# ****************************************************************************************************************************************
# ****************************************************************************************************************************************
        # estaba 
        #self.drawCuantos(self.mas.cont_pos, self.mas.cont_vehi)

# ****************************************************************************************************************************************
# ****************************************************************************************************************************************
# *************************************************************************************************
        # for i,j in self.mas.m.dibulabel.items():
        #     self.drawCuantos(i, self.scaling * self.mas.m.dibusema[i][0]+50, self.scaling * self.mas.m.dibusema[i][1]+50,"a")

        # file.write(rpta)
        # file.close()

        for vehiculo in self.mas.vehiculos:
            if vehiculo.actualizar:
                self.updateVehiculo(vehiculo)
                vehiculo.actualizar = False
        # estaba self.after(200, self.update)
        self.after(50, self.update)

    def updateVehiculo(self, vehiculo):
        dx = self.getDX(vehiculo)
        dy = self.getDY(vehiculo)
        self.draw.move(vehiculo.nombre, dx, dy)

    def drawInter(self, label, x, y):
        self.draw.create_rectangle(x-self.tamInter, y-self.tamInter, x+self.tamInter, y+self.tamInter, tags=label, fill="blue")

    def drawSema(self, label, x, y, color): #estaba -15  y   -11
        self.draw.create_oval(x-self.tamInter-2, y-self.tamInter-2, x+self.tamInter-1, y+self.tamInter-1, fill=color)

    # def drawCuantos(self, label, x2, y2,texto): #####label es el indice ******* j es VERDE, ROJO, horizontal, vertical
        # x = self.getXY(vehiculo.posActual)[0] + self.origin[0]
        # y = self.getXY(vehiculo.posActual)[1] + self.origin[1]
        # self.draw.create_rectangle(x - 3, y - 3, x + 3, y + 3, tags=vehiculo.nombre, fill="yellow")

        # Label(self, text=texto).place(x=x2-self.tamInter+13, y=y2-self.tamInter+60)
        # Label(self, text=texto).place(x=x2-self.tamInter-70, y=y2-self.tamInter-20)
        # Label(self, text=texto).place(x=x2-self.tamInter+60, y=y2-self.tamInter+13)
        # Label(self, text=texto).place(x=x2-self.tamInter-20, y=y2-self.tamInter-70)

        # self.draw.create_oval(x-self.tamInter-15, y-self.tamInter-15, x+self.tamInter-11, y+self.tamInter-11, fill="green", width=1)
        # self.draw.create_oval(x-self.tamInter+11, y-self.tamInter+11, x+self.tamInter+15, y+self.tamInter+15, fill="red", width=1)
        # self.draw.create_oval(x-self.tamInter+11, y-self.tamInter-15, x+self.tamInter+15, y+self.tamInter-11, fill="blue", width=1)
        # self.draw.create_oval(x-self.tamInter-15, y-self.tamInter+11, x+self.tamInter-11, y+self.tamInter+15, fill="white", width=1)

        # Label(self, text='1').place(x=x-self.tamInter+13, y=y-self.tamInter+60)
        # Label(self, text='2').place(x=x-self.tamInter-70, y=y-self.tamInter-20)
        # Label(self, text='3').place(x=x-self.tamInter+60, y=y-self.tamInter+13)
        # Label(self, text='4').place(x=x-self.tamInter-20, y=y-self.tamInter-70)

        # self.draw.create_rectangle(x-self.tamInter-12, y-self.tamInter-12, x+self.tamInter-12, y+self.tamInter-12, tags=label, fill="green")
        # self.draw.create_rectangle(x-self.tamInter+12, y-self.tamInter-12, x+self.tamInter+12, y+self.tamInter-12, tags=label, fill="green")
        # self.draw.create_rectangle(x-self.tamInter+12, y-self.tamInter+12, x+self.tamInter+12, y+self.tamInter+12, tags=label, fill="red")
        # self.draw.create_rectangle(x+self.tamInter-12, y+self.tamInter+12, x-self.tamInter-12, y-self.tamInter+12, tags=label, fill="red")

    def drawCalle(self, street):
        x0 = self.mas.m.intersecciones[street[0]][0] * self.scaling + self.origin[0]
        y0 = self.mas.m.intersecciones[street[0]][1] * self.scaling + self.origin[1]
        x1 = self.mas.m.intersecciones[street[1]][0] * self.scaling + self.origin[0]
        y1 = self.mas.m.intersecciones[street[1]][1] * self.scaling + self.origin[1]

        # x = self.mas.m.intersecciones[street[0]][0] * self.scaling + self.origin[0]+5
        # y = self.mas.m.intersecciones[street[0]][1] * self.scaling + self.origin[1]+5
        # x2 = self.mas.m.intersecciones[street[1]][0] * self.scaling + self.origin[0]+5
        # y2 = self.mas.m.intersecciones[street[1]][1] * self.scaling + self.origin[1]+5

        self.draw.create_line(x0, y0, x1, y1, fill="black")
        # self.draw.create_line(x, y, x2, y2, fill="black")

    def drawVehiculo(self, vehiculo):
        x = self.getXY(vehiculo.posActual)[0] + self.origin[0]
        y = self.getXY(vehiculo.posActual)[1] + self.origin[1]
        self.draw.create_rectangle(x - 3, y - 3, x + 3, y + 3, tags=vehiculo.nombre, fill="yellow")
        # self.draw.create_text((x+10, y+10), text="a")

    def drawCuantos(self, labelPos, contVehi):
        texto = ""
        for (v,w), (i,j) in zip(labelPos.items(), contVehi.items()):
                if len(w) > 0:
                    x1 = self.getLabelXY(v, 5)[0] #+ 50
                    y1 = self.getLabelXY(v, 5)[1] #+ 50
                    texto = len(j)
                    Label(self, text=texto).place(x=x1 ,y=y1)
                    # Label(self, text="a").place(x=x1*-1 ,y=y1*-1)

    def getXY(self, vehiculoPos):
        streetID = vehiculoPos[0]
        street = self.mas.m.calles[streetID]
        length = float(street[2])
        x0 = self.mas.m.intersecciones[street[0]][0] * self.scaling
        y0 = self.mas.m.intersecciones[street[0]][1] * self.scaling
        x1 = self.mas.m.intersecciones[street[1]][0] * self.scaling
        y1 = self.mas.m.intersecciones[street[1]][1] * self.scaling
        direction = [x1 - x0, y1 - y0]
        progress = float(vehiculoPos[1])
        return [x0 + progress/length * direction[0], y0 + progress/length * direction[1]]

    def getLabelXY(self, ind, cont):
        streetID = ind
        street = self.mas.m.calles[streetID]
        length = 10
        x0 = self.mas.m.intersecciones[street[0]][0] * self.scaling+ self.origin[0]
        y0 = self.mas.m.intersecciones[street[0]][1] * self.scaling+ self.origin[1]
        x1 = self.mas.m.intersecciones[street[1]][0] * self.scaling+ self.origin[0]
        y1 = self.mas.m.intersecciones[street[1]][1] * self.scaling+ self.origin[1]
        direction = [x1 - x0, y1 - y0]
        progress = float(cont)
        return [x0 + progress/length * direction[0] +3, y0 + progress/length * direction[1] +8]
        # +12  ,   +8

    def getDX(self, vehiculo):
        return self.getXY(vehiculo.posActual)[0] - self.getXY(vehiculo.posAnterior)[0]

    def getDY(self, vehiculo):
        return self.getXY(vehiculo.posActual)[1] - self.getXY(vehiculo.posAnterior)[1]

    def createWidgets(self):
        self.draw = Canvas(self, width=self.width, height=self.height)
        self.draw.pack(side=LEFT)
