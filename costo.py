from typing import Any
import numpy as np
import queue as Queue


tablero=np.loadtxt('matriz.txt',skiprows=0)


def crearMatrixCostoSinMontura(matrizBase):
    matriz = np.zeros(matrizBase.shape)
    for i in range(matrizBase.shape[0]):
        for j in range(matrizBase.shape[1]):
            if matrizBase[i,j] != 2 :
                matriz[i,j] = 1
            else :
                matriz[i,j] = 2
    return matriz

def ubicacionDelJugador(matrizBase):
    for i in range(matrizBase.shape[0]):
        for j in range(matrizBase.shape[1]):
            if matrizBase[i,j] == 1 :
                return [i,j]

def puedeHacia(desde, donde, matriz):
    if donde == "arriba":
        try:
            if desde[0]-1 < 0:
                print("Recorcholis esa posicion esta fuera de los parametros {}".format(donde) + "\n")
                return False
            elif matriz[desde[0]-1, desde[1]] != 3.0 :
                return True
            else:
                return False
        except IndexError:
            print("Recorcholis esa posicion esta fuera de los parametros {}".format(donde) + "\n")
            return False
    elif donde == "abajo":
        try:
            if desde[0]+1 > matriz.shape[0] :
                print("Recorcholis esa posicion esta fuera de los parametros {}".format(donde) + "\n")
                return False
            elif matriz[desde[0]+1, desde[1]] != 3.0:
                return True
            else:
                return False
        except IndexError:
            print("Recorcholis esa posicion esta fuera de los parametros {}".format(donde) + "\n")
            return False
    elif donde == "derecha":
        try:
            if desde[1]+1 > matriz.shape[1] :
                print("Recorcholis esa posicion esta fuera de los parametros {}".format(donde) + "\n")
                return False
            elif matriz[desde[0] , desde[1]+1] != 3.0:
                return True
            else:
                return False
        except IndexError:
            print("Recorcholis esa posicion esta fuera de los parametros {}".format(donde) + "\n")
            return False
    elif donde=="izquierda":
        try:
            if desde[1]-1 < 0 :
                print("Recorcholis esa posicion esta fuera de los parametros {}".format(donde) + "\n")
                return False
            elif matriz[desde[0], desde[1]-1] != 3.0:
                return True
            else:
                return False
        except IndexError:
            print("Recorcholis esa posicion esta fuera de los parametros {}".format(donde) + "\n")
            return False
    else:
        print("ERROR: ingreso valor \"donde\" no valido. Usted ingreso {} \n \n".format(donde) * 3)

def ubicacionHacia(desde, donde, matriz):
    if donde == "arriba":
        try:
            if desde[0]-1 < 0:
                print("Recorcholis esa posicion esta fuera de los parametros {}".format(donde) + "\n")
                return False
            elif matriz[desde[0]-1, desde[1]] != 3.0 :
                return [desde[0]-1, desde[1]]
            else:
                return False
        except IndexError:
            print("Recorcholis esa posicion esta fuera de los parametros {}".format(donde) + "\n")
            return False
    elif donde == "abajo":
        try:
            if desde[0]+1 > matriz.shape[0] :
                print("Recorcholis esa posicion esta fuera de los parametros {}".format(donde) + "\n")
                return False
            elif matriz[desde[0]+1, desde[1]] != 3.0:
                return [desde[0]+1, desde[1]]
            else:
                return False
        except IndexError:
            print("Recorcholis esa posicion esta fuera de los parametros {}".format(donde) + "\n")
            return False
    elif donde == "derecha":
        try:
            if desde[1]+1 > matriz.shape[1] :
                print("Recorcholis esa posicion esta fuera de los parametros {}".format(donde) + "\n")
                return False
            elif matriz[desde[0] , desde[1]+1] != 3.0:
                return [desde[0] , desde[1]+1]
            else:
                return False
        except IndexError:
            print("Recorcholis esa posicion esta fuera de los parametros {}".format(donde) + "\n")
            return False
    elif donde=="izquierda":
        try:
            if desde[1]-1 < 0 :
                print("Recorcholis esa posicion esta fuera de los parametros {}".format(donde) + "\n")
                return False
            elif matriz[desde[0], desde[1]-1] != 3.0:
                return [desde[0], desde[1]-1]
            else:
                return False
        except IndexError:
            print("Recorcholis esa posicion esta fuera de los parametros {}".format(donde) + "\n")
            return False
    else:
        print("ERROR: ingreso valor \"donde\" no valido. Usted ingreso {} \n \n".format(donde) * 3)
                
def ubicacionMeta(matrizBase):
    for i in range(matrizBase.shape[0]):
        for j in range(matrizBase.shape[1]):
            if matrizBase[i,j] == 5 :
                return [i,j]

def ubicacionMontura(matrizBase):
    for i in range(matrizBase.shape[0]):
        for j in range(matrizBase.shape[1]):
            if matrizBase[i,j] == 4 :
                return [i,j]

def pasoPorMontura(lista, ubicacionMontura):
    for i in lista:
        if i == ubicacionMontura:
            return True
    else:
        return False

def expandirNodo(cola, nodoAnterior, nodoactual, ubicacionMontura, matriz, lista, costoAcomulado, matrizCosto):    
    
    if nodoactual == nodoAnterior:
        aux_lista = [nodoactual]
    else:
        aux_lista = []
        for i in range(len(lista)):
            aux_lista[len(lista):]=[lista[i]]
        
    if False:  #temporalmente falso mientras que se prueba, si funciona se borra 
    #if nodoAnterior == 0:
        if puedeHacia(nodoactual,"arriba",matriz):
            if pasoPorMontura(lista,ubicacionMontura):
                aux_lista[len(aux_lista):]=[[ubicacionHacia(nodoactual,"arriba",matriz)]]
                cola.put([costoAcomulado+1,aux_lista])
                print([costoAcomulado+1,aux_lista])                                         #BORRAR DESPUES
                aux_lista = []
                for i in range(len(lista)):
                    aux_lista[len(lista):]=lista[i]
                
            else:
                aux_lista[len(aux_lista):]=[ubicacionHacia(nodoactual,"arriba",matriz)]
                cola.put([costoAcomulado + matrizCosto[ubicacionHacia(nodoactual,"arriba",matriz)[0],ubicacionHacia(nodoactual,"arriba",matriz)[1]],aux_lista])
                print([costoAcomulado+1,aux_lista])                                         #BORRAR DESPUES
                aux_lista=listaaux_lista = []
                for i in range(len(lista)):
                    aux_lista[len(lista):]=lista[i]

        if puedeHacia(nodoactual,"abajo",matriz):
            if pasoPorMontura(lista,ubicacionMontura):
                aux_lista[len(aux_lista):]=[ubicacionHacia(nodoactual,"abajo",matriz)]
                cola.put([costoAcomulado+1,aux_lista])
                print([costoAcomulado+1,aux_lista])                                         #BORRAR DESPUES
                aux_lista = []
                for i in range(len(lista)):
                    aux_lista[len(lista):]=lista[i]

            else:
                aux_lista[len(aux_lista):]=[ubicacionHacia(nodoactual,"abajo",matriz)]
                cola.put([costoAcomulado + matrizCosto[ubicacionHacia(nodoactual,"abajo",matriz)[0],ubicacionHacia(nodoactual,"abajo",matriz)[1]],aux_lista])
                print([costoAcomulado+1,aux_lista])                                         #BORRAR DESPUES
                aux_lista = []
                for i in range(len(lista)):
                    aux_lista[len(lista):]=lista[i]

        if puedeHacia(nodoactual,"derecha",matriz):
            if pasoPorMontura(lista,ubicacionMontura):
                aux_lista[len(aux_lista):]=[ubicacionHacia(nodoactual,"derecha",matriz)]
                cola.put([costoAcomulado+1,aux_lista])
                print([costoAcomulado+1,aux_lista])                                         #BORRAR DESPUES
                aux_lista = []
                for i in range(len(lista)):
                    aux_lista[len(lista):]=lista[i]

            else:
                aux_lista[len(aux_lista):]=[ubicacionHacia(nodoactual,"derecha",matriz)]
                cola.put([costoAcomulado + matrizCosto[ubicacionHacia(nodoactual,"derecha",matriz)[0],ubicacionHacia(nodoactual,"derecha",matriz)[1]],aux_lista])
                print([costoAcomulado+1,aux_lista])                                         #BORRAR DESPUES
                aux_lista = []
                for i in range(len(lista)):
                    aux_lista[len(lista):]=lista[i]
                    
        if puedeHacia(nodoactual,"izquierda",matriz):
            if pasoPorMontura(lista,ubicacionMontura):
                aux_lista[len(aux_lista):]=[ubicacionHacia(nodoactual,"izquierda",matriz)]
                cola.put([costoAcomulado+1,aux_lista])
                print([costoAcomulado+1,aux_lista])                                         #BORRAR DESPUES
                aux_lista = []
                for i in range(len(lista)):
                    aux_lista[len(lista):]=lista[i]

            else:
                aux_lista[len(aux_lista):]=[ubicacionHacia(nodoactual,"izquierda",matriz)]
                cola.put([costoAcomulado + matrizCosto[ubicacionHacia(nodoactual,"abajo",matriz)[0],ubicacionHacia(nodoactual,"abajo",matriz)[1]],aux_lista])
                print([costoAcomulado+1,aux_lista])                                         #BORRAR DESPUES
                aux_lista = []
                for i in range(len(lista)):
                    aux_lista[len(lista):]=lista[i]

    else:
        if puedeHacia(nodoactual,"arriba",matriz):
            if nodoAnterior != ubicacionHacia(nodoactual,"arriba",matriz):
                if pasoPorMontura(lista,ubicacionMontura):
                    aux_lista[len(aux_lista):]=[ubicacionHacia(nodoactual,"arriba",matriz)]
                    cola.put([costoAcomulado+1,aux_lista])
                    print([costoAcomulado+1,aux_lista])                                         #BORRAR DESPUES
                    aux_lista = []
                    if nodoactual == nodoAnterior:
                        aux_lista = [nodoactual]
                    else:
                        aux_lista = []
                        for i in range(len(lista)):
                            aux_lista[len(lista):]=[lista[i]]
                        
                else:
                    aux_lista[len(aux_lista):]=[ubicacionHacia(nodoactual,"arriba",matriz)]
                    cola.put([costoAcomulado + matrizCosto[ubicacionHacia(nodoactual,"arriba",matriz)[0],ubicacionHacia(nodoactual,"arriba",matriz)[1]],aux_lista])
                    print([costoAcomulado+1,aux_lista])                                         #BORRAR DESPUES
                    aux_lista= []
                    if nodoactual == nodoAnterior:
                        aux_lista = [nodoactual]
                    else:
                        aux_lista = []
                        for i in range(len(lista)):
                            aux_lista[len(lista):]=[lista[i]]
                        

        if puedeHacia(nodoactual,"abajo",matriz):
            if nodoAnterior != ubicacionHacia(nodoactual,"abajo",matriz):
                if pasoPorMontura(lista,ubicacionMontura):
                    aux_lista[len(aux_lista):]=[ubicacionHacia(nodoactual,"abajo",matriz)]
                    cola.put([costoAcomulado+1,aux_lista])
                    print([costoAcomulado+1,aux_lista])                                         #BORRAR DESPUES
                    aux_lista= []
                    if nodoactual == nodoAnterior:
                        aux_lista = [nodoactual]
                    else:
                        aux_lista = []
                        for i in range(len(lista)):
                            aux_lista[len(lista):]=[lista[i]]
                        
                else:
                    aux_lista[len(aux_lista):]=[ubicacionHacia(nodoactual,"abajo",matriz)]
                    cola.put([costoAcomulado + matrizCosto[ubicacionHacia(nodoactual,"abajo",matriz)[0],ubicacionHacia(nodoactual,"abajo",matriz)[1]],aux_lista])
                    print([costoAcomulado+1,aux_lista])                                         #BORRAR DESPUES
                    aux_lista= []
                    if nodoactual == nodoAnterior:
                        aux_lista = [nodoactual]
                    else:
                        aux_lista = []
                        for i in range(len(lista)):
                            aux_lista[len(lista):]=[lista[i]]
                        
        if puedeHacia(nodoactual,"derecha",matriz):
            if nodoAnterior != ubicacionHacia(nodoactual,"derecha",matriz):
                if pasoPorMontura(lista,ubicacionMontura):
                    aux_lista[len(aux_lista):]=[ubicacionHacia(nodoactual,"derecha",matriz)]
                    cola.put([costoAcomulado+1,aux_lista])
                    print([costoAcomulado+1,aux_lista])                                         #BORRAR DESPUES
                    aux_lista= []
                    if nodoactual == nodoAnterior:
                        aux_lista = [nodoactual]
                    else:
                        aux_lista = []
                        for i in range(len(lista)):
                            aux_lista[len(lista):]=[lista[i]]
                        
                else:
                    aux_lista[len(aux_lista):]=[ubicacionHacia(nodoactual,"derecha",matriz)]
                    cola.put([costoAcomulado + matrizCosto[ubicacionHacia(nodoactual,"derecha",matriz)[0],ubicacionHacia(nodoactual,"derecha",matriz)[1]],aux_lista])
                    print([costoAcomulado+1,aux_lista])                                         #BORRAR DESPUES
                    aux_lista= []
                    if nodoactual == nodoAnterior:
                        aux_lista = [nodoactual]
                    else:
                        aux_lista = []
                        for i in range(len(lista)):
                            aux_lista[len(lista):]=[lista[i]]
                        
        if puedeHacia(nodoactual,"izquierda",matriz):
            if nodoAnterior != ubicacionHacia(nodoactual,"izquierda",matriz):
                if pasoPorMontura(lista,ubicacionMontura):
                    aux_lista[len(aux_lista):]=[ubicacionHacia(nodoactual,"izquierda",matriz)]
                    cola.put([costoAcomulado+1,aux_lista])
                    print([costoAcomulado+1,aux_lista])                                         #BORRAR DESPUES
                    aux_lista= []
                    if nodoactual == nodoAnterior:
                        aux_lista = [nodoactual]
                    else:
                        aux_lista = []
                        for i in range(len(lista)):
                            aux_lista[len(lista):]=[lista[i]]
                        
                else:
                    aux_lista[len(aux_lista):]=[ubicacionHacia(nodoactual,"izquierda",matriz)]
                    cola.put([costoAcomulado + matrizCosto[ubicacionHacia(nodoactual,"izquierda",matriz)[0],ubicacionHacia(nodoactual,"izquierda",matriz)[1]],aux_lista])
                    print([costoAcomulado+1,aux_lista])                                         #BORRAR DESPUES
                    aux_lista= []
                    if nodoactual == nodoAnterior:
                        aux_lista = [nodoactual]
                    else:
                        aux_lista = []
                        for i in range(len(lista)):
                            aux_lista[len(lista):]=[lista[i]]
                        
def rutaOptima(matriz):
    parada = 0
    matrizCosto = crearMatrixCostoSinMontura(matriz)
    ubicacionDeMeta= ubicacionMeta(matriz)
    colaDePrioridad = Queue.PriorityQueue()
    colaDePrioridad.put([0,[ubicacionDelJugador(matriz)]])
    ubicacionDeMontura = ubicacionMontura(matriz)
    while True:
        nodoMenorcostoAcomulado = colaDePrioridad.get()
        ubicacionActualJugador = nodoMenorcostoAcomulado[1][len(nodoMenorcostoAcomulado[1])-1]
        ubicacionAnteriorDelJugador = nodoMenorcostoAcomulado[1][len(nodoMenorcostoAcomulado[1])-2]
        ruta = nodoMenorcostoAcomulado[1]
        costoAcomulado = nodoMenorcostoAcomulado[0]
        if ubicacionActualJugador == ubicacionDeMeta:
            return nodoMenorcostoAcomulado[1]
        #elif len(nodoMenorcostoAcomulado[1])==1:
            #expandirNodo(colaDePrioridad,0,ubicacionActualJugador, ubicacionDeMontura, matriz, ruta, costoAcomulado, matrizCosto)
        else:
            expandirNodo(colaDePrioridad,ubicacionAnteriorDelJugador,ubicacionActualJugador, ubicacionDeMontura, matriz, ruta, costoAcomulado, matrizCosto)
        if parada == 40:
            break
        else:
            parada = parada + 1

#colaDePrioridad = Queue.PriorityQueue()
#colaDePrioridad.put([0,[ubicacionDelJugador(tablero)]])
#print(colaDePrioridad.get())
print(rutaOptima(tablero))

# ----------- PRUEBAS --------------------------------#
#

"""
a=[[1,2],[1,3],[1,4]]
print(a)
a[len(a):]=[[4,3]]
print(len(a))
print(a)


def prueba():
    i=0
    while i != 3:
        print(i)
        return i
        i=i+1

print(prueba())



print(ubicacionMeta(tablero))


print(puedeHacia(ubicacionDelJugador(tablero), "arriba", tablero))
print(puedeHacia(ubicacionDelJugador(tablero), "abajo", tablero))
print(puedeHacia(ubicacionDelJugador(tablero), "derecha", tablero))
print(puedeHacia(ubicacionDelJugador(tablero), "izquierda", tablero))

print(ubicacionDelJugador(tablero))
print(ubicacionDelJugador(tablero)[0]-1, ubicacionDelJugador(tablero)[1])
print(ubicacionDelJugador(tablero)[1])


#print(tablero)
#print(crearMatrixCostoSinMontura(tablero))
#print(type(tablero.shape[1]))
#print(tablero.shape[1])
"""

