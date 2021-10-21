from operator import truediv
import numpy as np
#from anytree import Node

tablero=np.loadtxt('matriz.txt',skiprows=0)      
print(tablero)


def coordenadaDeDato(dato, matrizBase):
	for i in range(matrizBase.shape[0]):
		for j in range(matrizBase.shape[1]):
			if matrizBase[i,j] == dato :
				return [i,j]

agente=coordenadaDeDato(1,tablero) #lo necesito para hacer una validación más adelante 

def datoSegunCoordenada(tupla,matrizBase):
	return matrizBase[tupla[0]][tupla[1]]

def esObstaculo(tupla, matrizBase):
	if matrizBase[tupla[0]][tupla[1]] == 3:
		return True
	else: return False

def esMeta(tupla, matrizBase):
	if matrizBase[tupla[0]][tupla[1]] == 5:
		return True
	else: return False

def esLimite(tupla):
	if 0 > tupla[0] or tupla[0] > 3 or  0 > tupla[1] or tupla[1] > 4 :
		return True
	else: return False

def buscarEnLista(lista,valor):
	if valor in lista: # Imprime lo de abajo
		return True

def elementosIguales(lista):
	auxBool=False
	if len(lista)==1:
		aux=lista[0]
		return aux
		
	else:
		aux=lista[0]
		for i in range(1, len(lista)):
			if (lista[i] == aux) :
				print('Alguno Entró en el area MAluca')
				auxBool= True
			else: 
				auxBool=False
	return auxBool
				

		
def vaciarLista(auxParaNuevaRaiz):
	while not (auxParaNuevaRaiz == []):
		auxParaNuevaRaiz.pop()




listaNodosNivel=[]
listaNodosAux=[]

def almacenarCoordenada2(dato,nodosRecorridos):
	if esLimite(dato)== False and esObstaculo(dato,tablero)== False:
		if nodosRecorridos ==[]:
			if not dato==agente: #para que no se me devuelva a la raíz
				listaNodosAux.append(dato)
				#print(listaNodosAux)
				if  esMeta(dato,tablero): 
					return True
		else:
			if not buscarEnLista(nodosRecorridos,dato):
				if not dato==agente: #para que no se me devuelva a la raíz
					listaNodosAux.append(dato)
					#print(listaNodosAux)
					if  esMeta(dato,tablero): 
						return True



#orden: arriba, abajo, derecha, izquierda



def funcionBajar2(nuevaRaiz):
	if esObstaculo(nuevaRaiz,tablero)== False and esLimite(nuevaRaiz) == False:

		arriba=[nuevaRaiz[0]-1,nuevaRaiz[1]]
		abajo=[nuevaRaiz[0]+1,nuevaRaiz[1]]
		derecha=[nuevaRaiz[0],nuevaRaiz[1]+1]
		izquierda=[nuevaRaiz[0],nuevaRaiz[1]-1]

		aux=almacenarCoordenada2(arriba,listaNodosAux)
		if aux == True:
			return True
		aux=almacenarCoordenada2(abajo,listaNodosAux)
		if aux == True:
			return True
		aux=almacenarCoordenada2(derecha,listaNodosAux)
		if aux == True:
			return True
		aux=almacenarCoordenada2(izquierda,listaNodosAux)
		if aux == True:
			return True

		listaNodosNivel.extend(listaNodosAux)
		listaNodosAux.clear

	return False	
			


def encontrarMeta2():

	encontroMeta= False
	contador=5
	listaRecorridoTotal=[]
	listaRecorriendo=[]
	
	

	#while encontroMeta== False:
	for j in range (0, contador):	
		if j == 0:
			listaRecorriendo.append(agente)
			print('lista recorriendo')
			print(listaRecorriendo)

		nodosArecorrer=len(listaRecorriendo)


		for i in range(0,nodosArecorrer ):
			aux=funcionBajar2(listaRecorriendo[i])
			print('aqui')
			print(listaRecorriendo[i])
			if aux==True:
				#encontroMeta=True
				print('se encontró la meta en nivel ' + str(j))
				break
			#listaRecorriendo.clear()
			


		listaRecorridoTotal.extend(listaRecorriendo)
		listaRecorriendo.clear()
		listaRecorriendo.extend(listaNodosNivel)
		listaNodosNivel.clear()
		print('no encontró meta en nivel ' +str(j))
		print('Final antes de iterar nuevamente: lTotal')
		#print(listaRecorridoTotal)
		#print(listaRecorriendo)
		#print(listaNodosNivel)
		#print(contador)

	

		
encontrarMeta2()




