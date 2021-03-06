from typing import Any
import numpy as np
import queue as Queue
from numpy.core.fromnumeric import shape

from numpy.lib import shape_base


tablero = np.loadtxt('matriz.txt', skiprows=0)


def crearMatrizCostoSinMontura(matrizBase):
    """
    Descripcion de crearMatrizCostoSinMontura
    Funcion retorna matriz del mismop formato que matrizBase 
    pero este contiene el costo de cada casilla 

    Args:
        matrizBase (undefined): matriz del tablero

    """
    matriz = np.zeros(matrizBase.shape)
    for i in range(matrizBase.shape[0]):
        for j in range(matrizBase.shape[1]):
            if matrizBase[i, j] != 2:
                matriz[i, j] = 1
            else:
                matriz[i, j] = 2
    return matriz


def ubicacionDelJugador(matrizBase):
    """
    Description of ubicacionDelJugador
    Retorna la ubicacion del jugador en la matriz que se ingrese 
    Args:
        matrizBase (undefined): matriz del tablero

    """
    for i in range(matrizBase.shape[0]):
        for j in range(matrizBase.shape[1]):
            if matrizBase[i, j] == 1:
                return [i, j]


def puedeIrHacia(desde, hacia, matriz):
    if hacia == "arriba":
        try:
            if desde[0]-1 < 0:
                #print("Recorcholis esa posicion esta fuera de los parametros {}".format(hacia) + "\n")
                return False
            elif matriz[desde[0]-1, desde[1]] != 3.0:
                return True
            else:
                return False
        except IndexError:
                #print("Recorcholis esa posicion esta fuera de los parametros {}".format(hacia) + "\n")
            return False
    elif hacia == "abajo":
        try:
            if desde[0]+1 > matriz.shape[0]:
                #print("Recorcholis esa posicion esta fuera de los parametros {}".format(hacia) + "\n")
                return False
            elif matriz[desde[0]+1, desde[1]] != 3.0:
                return True
            else:
                return False
        except IndexError:
            #print("Recorcholis esa posicion esta fuera de los parametros {}".format(hacia) + "\n")
            return False
    elif hacia == "derecha":
        try:
            if desde[1]+1 > matriz.shape[1]:
                #print("Recorcholis esa posicion esta fuera de los parametros {}".format(hacia) + "\n")
                return False
            elif matriz[desde[0], desde[1]+1] != 3.0:
                return True
            else:
                return False
        except IndexError:
            #print("Recorcholis esa posicion esta fuera de los parametros {}".format(hacia) + "\n")
            return False
    elif hacia == "izquierda":
        try:
            if desde[1]-1 < 0:
                #print("Recorcholis esa posicion esta fuera de los parametros {}".format(hacia) + "\n")
                return False
            elif matriz[desde[0], desde[1]-1] != 3.0:
                return True
            else:
                return False
        except IndexError:
            print("Recorcholis esa posicion esta fuera de los parametros {}".format(hacia) + "\n")
            return False
    else:
        print("ERROR: ingreso valor \"hacia\" no valido. Usted ingreso {} \n \n".format(hacia) * 3)


def ubicacionHacia(desde, hacia, matriz):
    if hacia == "arriba":
        try:
            if desde[0]-1 < 0:
                #print("Recorcholis esa posicion esta fuera de los parametros {}".format(hacia) + "\n")
                return False
            elif matriz[desde[0]-1, desde[1]] != 3.0:
                return [desde[0]-1, desde[1]]
            else:
                return False
        except IndexError:
            #print("Recorcholis esa posicion esta fuera de los parametros {}".format(hacia) + "\n")
            return False
    elif hacia == "abajo":
        try:
            if desde[0]+1 > matriz.shape[0]:
                #print("Recorcholis esa posicion esta fuera de los parametros {}".format(hacia) + "\n")
                return False
            elif matriz[desde[0]+1, desde[1]] != 3.0:
                return [desde[0]+1, desde[1]]
            else:
                return False
        except IndexError:
            #print("Recorcholis esa posicion esta fuera de los parametros {}".format(hacia) + "\n")
            return False
    elif hacia == "derecha":
        try:
            if desde[1]+1 > matriz.shape[1]:
                #print("Recorcholis esa posicion esta fuera de los parametros {}".format(hacia) + "\n")
                return False
            elif matriz[desde[0], desde[1]+1] != 3.0:
                return [desde[0], desde[1]+1]
            else:
                return False
        except IndexError:
            #print("Recorcholis esa posicion esta fuera de los parametros {}".format(hacia) + "\n")
            return False
    elif hacia == "izquierda":
        try:
            if desde[1]-1 < 0:
                #print("Recorcholis esa posicion esta fuera de los parametros {}".format(hacia) + "\n")
                return False
            elif matriz[desde[0], desde[1]-1] != 3.0:
                return [desde[0], desde[1]-1]
            else:
                return False
        except IndexError:
            print("Recorcholis esa posicion esta fuera de los parametros {}".format(hacia) + "\n")
            return False
    else:
        print("ERROR: ingreso valor \"hacia\" no valido. Usted ingreso {} \n \n".format(hacia) * 3)


def ubicacionMeta(matrizBase):
    for i in range(matrizBase.shape[0]):
        for j in range(matrizBase.shape[1]):
            if matrizBase[i, j] == 5:
                return [i, j]


def ubicacionMontura(matrizBase):
    for i in range(matrizBase.shape[0]):
        for j in range(matrizBase.shape[1]):
            if matrizBase[i, j] == 4:
                return [i, j]


def pasoPorMontura(lista, ubicacionMontura):
    for i in lista:
        if i == ubicacionMontura:
            return True
    else:
        return False


def copiarListaEnOtraLista_aux(lista_fuente, lista_destino, nodo_actual, nodo_anterior):
    if nodo_actual == nodo_anterior:
        lista_destino = [nodo_actual]
    else:
        lista_destino = []
        for i in range(len(lista_fuente)):
            lista_destino[len(lista_fuente):] = [lista_fuente[i]]

def copiarMatrizEnOtraMatriz_aux(matriz_fuente, matriz_destino):
    for i in range(matriz_fuente.shape[0]):
        for j in range(matriz_fuente.shape[1]):
            matriz_fuente[i,j]=matriz_destino[i,j]

def expandirNodoHacia(cola,nivel,lista,desde,hacia, matriz):
    ubicacion_meta=ubicacionMeta(matriz)
    prioridadHacia=10
    if hacia == "arriba":
        prioridadHacia=1
    elif hacia=="derecha":
        prioridadHacia=2
    elif hacia=="abajo":
        prioridadHacia=3
    elif hacia=="izquierda":
        prioridadHacia=4
    else:
        print("erro en expandirNodoHacia() se ingrso {} ".format(hacia))
    if puedeIrHacia(desde, hacia, matriz):
        aux_lista = []
        for i in range(len(lista)):
            aux_lista[len(lista):] = [lista[i]]
        aux_lista[len(aux_lista):]=[ubicacionHacia(desde, hacia, matriz)]
        cola.put([nivel,prioridadHacia,aux_lista])
        ubicacion_actual_jugador=aux_lista[len(aux_lista)-1]
        if ubicacion_actual_jugador==ubicacion_meta:
            return aux_lista

def expandirNodo(cola, nodoAnterior, nodoactual, ubicacionMontura, matriz, lista, costoAcomulado, matrizCosto):

    if nodoactual == nodoAnterior:
        aux_lista = [nodoactual]
    else:
        aux_lista = []
        for i in range(len(lista)):
            aux_lista[len(lista):] = [lista[i]]

    if puedeIrHacia(nodoactual, "arriba", matriz):
        if nodoAnterior != ubicacionHacia(nodoactual, "arriba", matriz):
            if pasoPorMontura(lista, ubicacionMontura):
                aux_lista[len(aux_lista):] = [
                    ubicacionHacia(nodoactual, "arriba", matriz)]
                cola.put([costoAcomulado+1, aux_lista])
                #print([costoAcomulado+1, aux_lista])  # BORRAR DESPUES
                aux_lista = []
                if nodoactual == nodoAnterior:
                    aux_lista = [nodoactual]
                else:
                    aux_lista = []
                    for i in range(len(lista)):
                        aux_lista[len(lista):] = [lista[i]]

            else:
                aux_lista[len(aux_lista):] = [
                    ubicacionHacia(nodoactual, "arriba", matriz)]
                cola.put([costoAcomulado + matrizCosto[ubicacionHacia(nodoactual, "arriba",matriz)[0], ubicacionHacia(nodoactual, "arriba", matriz)[1]], aux_lista])
                #print([costoAcomulado+1, aux_lista])  # BORRAR DESPUES
                aux_lista = []
                if nodoactual == nodoAnterior:
                    aux_lista = [nodoactual]
                else:
                    aux_lista = []
                    for i in range(len(lista)):
                        aux_lista[len(lista):] = [lista[i]]

    if puedeIrHacia(nodoactual, "abajo", matriz):
        if nodoAnterior != ubicacionHacia(nodoactual, "abajo", matriz):
            if pasoPorMontura(lista, ubicacionMontura):
                aux_lista[len(aux_lista):] = [
                    ubicacionHacia(nodoactual, "abajo", matriz)]
                cola.put([costoAcomulado+1, aux_lista])
                #print([costoAcomulado+1, aux_lista])  # BORRAR DESPUES
                aux_lista = []
                if nodoactual == nodoAnterior:
                    aux_lista = [nodoactual]
                else:
                    aux_lista = []
                    for i in range(len(lista)):
                        aux_lista[len(lista):] = [lista[i]]

            else:
                aux_lista[len(aux_lista):] = [
                    ubicacionHacia(nodoactual, "abajo", matriz)]
                cola.put([costoAcomulado + matrizCosto[ubicacionHacia(nodoactual, "abajo",matriz)[0], ubicacionHacia(nodoactual, "abajo", matriz)[1]], aux_lista])
                #print([costoAcomulado+1, aux_lista])  # BORRAR DESPUES
                aux_lista = []
                if nodoactual == nodoAnterior:
                    aux_lista = [nodoactual]
                else:
                    aux_lista = []
                    for i in range(len(lista)):
                        aux_lista[len(lista):] = [lista[i]]

    if puedeIrHacia(nodoactual, "derecha", matriz):
        if nodoAnterior != ubicacionHacia(nodoactual, "derecha", matriz):
            if pasoPorMontura(lista, ubicacionMontura):
                aux_lista[len(aux_lista):] = [
                    ubicacionHacia(nodoactual, "derecha", matriz)]
                cola.put([costoAcomulado+1, aux_lista])
                #print([costoAcomulado+1, aux_lista])  # BORRAR DESPUES
                aux_lista = []
                if nodoactual == nodoAnterior:
                    aux_lista = [nodoactual]
                else:
                    aux_lista = []
                    for i in range(len(lista)):
                        aux_lista[len(lista):] = [lista[i]]

            else:
                aux_lista[len(aux_lista):] = [
                    ubicacionHacia(nodoactual, "derecha", matriz)]
                cola.put([costoAcomulado + matrizCosto[ubicacionHacia(nodoactual, "derecha",matriz)[0], ubicacionHacia(nodoactual, "derecha", matriz)[1]], aux_lista])
                #print([costoAcomulado+1, aux_lista])  # BORRAR DESPUES
                aux_lista = []
                if nodoactual == nodoAnterior:
                    aux_lista = [nodoactual]
                else:
                    aux_lista = []
                    for i in range(len(lista)):
                        aux_lista[len(lista):] = [lista[i]]

    if puedeIrHacia(nodoactual, "izquierda", matriz):
        if nodoAnterior != ubicacionHacia(nodoactual, "izquierda", matriz):
            if pasoPorMontura(lista, ubicacionMontura):
                aux_lista[len(aux_lista):] = [ubicacionHacia(
                    nodoactual, "izquierda", matriz)]
                cola.put([costoAcomulado+1, aux_lista])
                #print([costoAcomulado+1, aux_lista])  # BORRAR DESPUES
                aux_lista = []
                if nodoactual == nodoAnterior:
                    aux_lista = [nodoactual]
                else:
                    aux_lista = []
                    for i in range(len(lista)):
                        aux_lista[len(lista):] = [lista[i]]

            else:
                aux_lista[len(aux_lista):] = [ubicacionHacia(
                    nodoactual, "izquierda", matriz)]
                cola.put([costoAcomulado + matrizCosto[ubicacionHacia(nodoactual, "izquierda",matriz)[0], ubicacionHacia(nodoactual, "izquierda", matriz)[1]], aux_lista])
                #print([costoAcomulado+1, aux_lista])  # BORRAR DESPUES
                aux_lista = []
                if nodoactual == nodoAnterior:
                    aux_lista = [nodoactual]
                else:
                    aux_lista = []
                    for i in range(len(lista)):
                        aux_lista[len(lista):] = [lista[i]]


def rutaOptima(matriz):
    parada = 0
    matrizCosto = crearMatrizCostoSinMontura(matriz)
    ubicacionDeMeta = ubicacionMeta(matriz)
    colaDePrioridad = Queue.PriorityQueue()
    colaDePrioridad.put([0, [ubicacionDelJugador(matriz)]])
    ubicacionDeMontura = ubicacionMontura(matriz)
    while True:
        nodoMenorcostoAcomulado = colaDePrioridad.get()
        ubicacionActualJugador = nodoMenorcostoAcomulado[1][len(
            nodoMenorcostoAcomulado[1])-1]
        ubicacionAnteriorDelJugador = nodoMenorcostoAcomulado[1][len(
            nodoMenorcostoAcomulado[1])-2]
        ruta = nodoMenorcostoAcomulado[1]
        costoAcomulado = nodoMenorcostoAcomulado[0]
        if ubicacionActualJugador == ubicacionDeMeta:
            return nodoMenorcostoAcomulado[1]
        else:
            expandirNodo(colaDePrioridad, ubicacionAnteriorDelJugador, ubicacionActualJugador,ubicacionDeMontura, matriz, ruta, costoAcomulado, matrizCosto)
        if parada == 40:
            break
        else:
            parada = parada + 1

#def profindidadInteractiva(matriz):
    parada=2
    ubicacion_meta=ubicacionMeta(matriz)
    

    while True:
        a=[]
        cola_de_prioridad=Queue.PriorityQueue()
        cola_de_prioridad.put([0,0,[ubicacionDelJugador(matriz)]])
        while True:
            print("a")
            nodo_mayor_prioridad=cola_de_prioridad.get()
            if nodo_mayor_prioridad[0]+1==parada:
                cola_de_prioridad.put(nodo_mayor_prioridad)
                break
            ubicacion_actual_jugador=nodo_mayor_prioridad[2][len(nodo_mayor_prioridad[2])-1]
            a=expandirNodoHacia(cola_de_prioridad, nodo_mayor_prioridad[0]+1, nodo_mayor_prioridad[2],ubicacion_actual_jugador,"arriba", matriz)
            a=expandirNodoHacia(cola_de_prioridad, nodo_mayor_prioridad[0]+1, nodo_mayor_prioridad[2],ubicacion_actual_jugador,"derecha", matriz)
            a=expandirNodoHacia(cola_de_prioridad, nodo_mayor_prioridad[0]+1, nodo_mayor_prioridad[2],ubicacion_actual_jugador,"abajo", matriz)
            a=expandirNodoHacia(cola_de_prioridad, nodo_mayor_prioridad[0]+1, nodo_mayor_prioridad[2],ubicacion_actual_jugador,"izquierda", matriz)
        parada=parada+1
        print(parada)
        if a != [] and a!= None:
            return a

#print(profindidadInteractiva(tablero))
# ----------- PRUEBAS --------------------------------#
#print(rutaOptima(tablero))  # prueba de funcion rutaOptima(matriz)


#colaDePrioridad = Queue.PriorityQueue()
# colaDePrioridad.put([0,[ubicacionDelJugador(tablero)]])
##print(colaDePrioridad.get())

"""
a=[[1,2],[1,3],[1,4]]
print(a)
a[len(a):]=[[4,3]]
print(len(a))
print(a)


def prueba():
    i=0
    while i != 3:
    #print(i)
        return i
        i=i+1

print(prueba())



print(ubicacionMeta(tablero))


print(puedeIrHacia(ubicacionDelJugador(tablero), "arriba", tablero))
print(puedeIrHacia(ubicacionDelJugador(tablero), "abajo", tablero))
print(puedeIrHacia(ubicacionDelJugador(tablero), "derecha", tablero))
print(puedeIrHacia(ubicacionDelJugador(tablero), "izquierda", tablero))

print(ubicacionDelJugador(tablero))
print(ubicacionDelJugador(tablero)[0]-1, ubicacionDelJugador(tablero)[1])
print(ubicacionDelJugador(tablero)[1])


#print(tablero)
#print(crearMatrizCostoSinMontura(tablero))
#print(type(tablero.shape[1]))
#print(tablero.shape[1])
"""
