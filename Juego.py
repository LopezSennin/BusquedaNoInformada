import pygame
from pygame import image
from pygame.locals import *
import numpy as np
import time
from threading import *
import costo as busqueda
# se inicializa pygame
pygame.init()

class Juego:
    def __init__(self):
        # ventana
        self.BLANCA=(255, 255, 255)
        self.size=500
        self.ventana = pygame.display.set_mode((self.size,self.size-100))
        pygame.display.set_caption("PRINCESS MONONOKE")
        self.icono=pygame.image.load("icono.jpg")
        pygame.display.set_icon(self.icono)
        self.ventana.fill(self.BLANCA)

    # extraemos un array 2D
    def extraer_matriz (url) : 
        A=np.loadtxt(url,skiprows=0)
        return A 

    # escenario/tablero
    escenario = extraer_matriz("matriz.txt") # matriz del nivel
    matriztemporal  = extraer_matriz("matriz.txt")
    filas = 4
    columnas = 5

    #tiles
    anchoT=100
    altoT=100
    NEGRO=(0, 0, 0)

    #dibujar rejilla
    def rejilla(self):
        for i in range(self.columnas):
            pygame.draw.line(self.ventana,self.NEGRO,(i*self.anchoT,0),(i*self.anchoT,self.size))
        for i in range(self.filas):
            pygame.draw.line(self.ventana,self.NEGRO,(0,i*self.altoT),(self.size,i*self.altoT))

    #se cargan las imagenes
    def cargarImagen(self):
        self.blanco=(pygame.image.load("imagenes/blanco.png"))
        self.mononoke=(pygame.image.load("imagenes/mononoke.png"))
        self.fantasma=(pygame.image.load("imagenes/fantasma.png"))
        self.negro=(pygame.image.load("imagenes/negro.png"))
        self.venado=(pygame.image.load("imagenes/venado.png"))
        self.espiritu=(pygame.image.load("imagenes/espiritu.png"))

    def pintarventana(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.escenario[i][j]==0:
                    escala=pygame.transform.scale(self.blanco,[self.anchoT,self.altoT])
                    self.ventana.blit(escala,[j*100,i*100])
                elif self.escenario[i][j]==1:
                    escala=pygame.transform.scale(self.mononoke,[self.anchoT,self.altoT])
                    self.ventana.blit(escala,[j*100,i*100])
                elif self.escenario[i][j]==2:
                    escala=pygame.transform.scale(self.fantasma,[self.anchoT,self.altoT])
                    self.ventana.blit(escala,[j*100,i*100])
                elif self.escenario[i][j]==3:
                    escala=pygame.transform.scale(self.negro,[self.anchoT,self.altoT])
                    self.ventana.blit(escala,[j*100,i*100])
                elif self.escenario[i][j]==4:
                    escala=pygame.transform.scale(self.venado,[self.anchoT,self.altoT])
                    self.ventana.blit(escala,[j*100,i*100])
                elif self.escenario[i][j]==5:
                    escala=pygame.transform.scale(self.espiritu,[self.anchoT,self.altoT])
                    self.ventana.blit(escala,[j*100,i*100])
        self.rejilla()     
        pygame.display.update()

    #se muestran las imagenes en pantalla segun posicion de la matriz
    def mostrarImagenes(self):
        self.cargarImagen()
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.escenario[i][j]==0:
                    escala=pygame.transform.scale(self.blanco,[self.anchoT,self.altoT])
                    self.ventana.blit(escala,[j*100,i*100])
                elif self.escenario[i][j]==1:
                    escala=pygame.transform.scale(self.mononoke,[self.anchoT,self.altoT])
                    self.ventana.blit(escala,[j*100,i*100])
                elif self.escenario[i][j]==2:
                    escala=pygame.transform.scale(self.fantasma,[self.anchoT,self.altoT])
                    self.ventana.blit(escala,[j*100,i*100])
                elif self.escenario[i][j]==3:
                    escala=pygame.transform.scale(self.negro,[self.anchoT,self.altoT])
                    self.ventana.blit(escala,[j*100,i*100])
                elif self.escenario[i][j]==4:
                    escala=pygame.transform.scale(self.venado,[self.anchoT,self.altoT])
                    self.ventana.blit(escala,[j*100,i*100])
                elif self.escenario[i][j]==5:
                    escala=pygame.transform.scale(self.espiritu,[self.anchoT,self.altoT])
                    self.ventana.blit(escala,[j*100,i*100])
        self.rejilla()     
        pygame.display.update()

    #crear objeto objeto
    def crearObjeto(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.escenario[i][j]==0:
                    self.blanco = Blanco(self.escenario[i][j],j,i)
                elif self.escenario[i][j]==1:
                    self.jugador = Jugador(self.escenario[i][j],j,i)
                elif self.escenario[i][j]==2:
                    self.fantasma = Fantasma(self.escenario[i][j],j,i)
                elif self.escenario[i][j]==3:
                    self.negro = Negro(self.escenario[i][j],j,i)
                elif self.escenario[i][j]==4:
                    self.venado = Venado(self.escenario[i][j],j,i)
                elif self.escenario[i][j]==5:
                    self.espiritu = Espiritu(self.escenario[i][j],j,i)
    lista_mov = [-1,0]

    corre = True
    FPS=60
    reloj = pygame.time.Clock()
    
    def mostrarImagenes2(self,matriz):
        self.cargarImagen()
        for i in range(self.filas):
            for j in range(self.columnas):
                if matriz[i][j]==0:
                    escala=pygame.transform.scale(self.blanco,[self.anchoT,self.altoT])
                    self.ventana.blit(escala,[j*100,i*100])
                elif matriz[i][j]==1:
                    escala=pygame.transform.scale(self.mononoke,[self.anchoT,self.altoT])
                    self.ventana.blit(escala,[j*100,i*100])
                elif matriz[i][j]==2:
                    escala=pygame.transform.scale(self.fantasma,[self.anchoT,self.altoT])
                    self.ventana.blit(escala,[j*100,i*100])
                elif matriz[i][j]==3:
                    escala=pygame.transform.scale(self.negro,[self.anchoT,self.altoT])
                    self.ventana.blit(escala,[j*100,i*100])
                elif matriz[i][j]==4:
                    escala=pygame.transform.scale(self.venado,[self.anchoT,self.altoT])
                    self.ventana.blit(escala,[j*100,i*100])
                elif matriz[i][j]==5:
                    escala=pygame.transform.scale(self.espiritu,[self.anchoT,self.altoT])
                    self.ventana.blit(escala,[j*100,i*100])
        self.rejilla()     
        pygame.display.update()



    def agenteRecorraMatriz(self, lista):
        
        for coordenada in lista:
            ubicacion_del_agente=busqueda.ubicacionDelJugador(self.matriztemporal)
            self.matriztemporal[ubicacion_del_agente[0],ubicacion_del_agente[1]]=0
            self.matriztemporal[coordenada[0],coordenada[1]]=1
            self.mostrarImagenes2(self.matriztemporal)
            pygame.time.wait(1000)

    def run(self):
        self.crearObjeto()
        while self.corre:
            self.eventos()  
            self.agenteRecorraMatriz(busqueda.rutaOptima(self.escenario))
            self.mostrarImagenes()
            #self.jugador.update()
            #self.jugador.mover(self.lista_mov)
            pygame.display.flip()
        self.reloj.tick(self.FPS)
        pygame.quit()

    def eventos(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.corre=False
                        

    
###############################################################################################

class Jugador():
    def __init__(self,pos,y,x):
        self.x = x
        self.y = y
        self.vec = [x,y]
        self.posicionPieza = pos
        print(self.posicionPieza)
        print(self.vec)
        #print("jugador")

    # mueve al jugador
    def update(self):
        #self.posicionPieza+=self.x+1,self.y+1
        self.posicionPieza+=self.x

    def mover(self,lista):
        self.lista = lista
        
        #print(direccion)

###############################################################################################

class Blanco():
    def __init__(self,pos,y,x):
        self.x = x
        self.y = y
        self.vec = [x,y]
        self.posicionPieza = pos
        print(self.posicionPieza)
        print(self.vec)
        #print(self.posicionPieza)
        #print("blanco")

###############################################################################################

class Fantasma():
    def __init__(self,pos,y,x):
        self.x = x
        self.y = y
        self.vec = [x,y]
        self.posicionPieza = pos
        print(self.posicionPieza)
        print(self.vec)
        #print(self.posicionPieza)
        #print("fantasma")
    
###############################################################################################

class Negro():
    def __init__(self,pos,y,x):
        self.x = x
        self.y = y
        self.vec = [x,y]
        self.posicionPieza = pos
        print(self.posicionPieza)
        print(self.vec)
        #print(self.posicionPieza)
        #print("negro")

###############################################################################################

class Venado():
    def __init__(self,pos,y,x):
        self.x = x
        self.y = y
        self.vec = [x,y]
        self.posicionPieza = pos
        print(self.posicionPieza)
        print(self.vec)
        #print(self.posicionPieza)
        #print("venado")

###############################################################################################

class Espiritu():
    def __init__(self,pos,y,x):
        self.x = x
        self.y = y
        self.vec = [x,y]
        self.posicionPieza = pos
        print(self.posicionPieza)
        print(self.vec)
        #print(self.posicionPieza)
        #print("espiritu")

###############################################################################################

juego = Juego()
juego.run()
#matriztemporal  = np.loadtxt("matriz.txt",skiprows=0)
#print(busqueda.ubicacionDelJugador(matriztemporal))
