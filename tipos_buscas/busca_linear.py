


def busca(lista, elem):
	
	''' Retorna o índice elem se estiver na lista ou None 
	caso contrário'''

	for i in range(len(lista)):
		if lista[i] == elem:
			return i
	return None

lista_estranha = [8, "5", 32, 0 , "python", 11]
elemento = 32
elemento = 50

indice = busca(lista_estranha, elemento)
if indice is not None:
	print("O índice do elemento {} é {}".format(elemento, indice))
else:
	print("O elemento {} não se encontra na lista".format(elemento))

# Complexidade depende do elemento que estamos procurando.
# Pense no pior caso, quando o elemento procurado não se encontra na lista
# n = tamanho da lista --> 2*n+1 (pode desconsiderar o 1 que é uma posição )
# analisa apenas o termo dominante e o 2 não interessa = é O(n) - linear

# Se a lista estiver ordenada  é melhor usar a BUSCA BINÁRIA - Complexidade O(log(n))