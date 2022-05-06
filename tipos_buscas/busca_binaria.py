1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15

def buscaBinaria(lista, idxEsquerda, idxDireita, item):
    # Caso base: o elemento não está presente. 
    if idxDireita < idxEsquerda:
        return -1
    meio = (idxDireita + idxEsquerda) // 2
    # Nosso palpite estava certo: o elemento está no meio do arranjo. 
    if lista[meio] == item:
        return meio
    # O palpite estava errado: atualizamos os limites e continuamos a busca. 
    elif lista[meio] > item:
        return buscaBinaria(lista, idxEsquerda, meio - 1, item)
    else: # lista[meio] < item
        return buscaBinaria(lista, meio + 1, idxDireita, item)

A = [0, 10, 20, 30, 40, 50, 60, 70]
print("Pesquisa com sucesso:", buscaBinaria(A, 0, len(A) - 1, 20))
print("Pesquisa com sucesso:", buscaBinaria(A, 0, len(A) - 1, 0))
print("Pesquisa com sucesso:", buscaBinaria(A, 0, len(A) - 1, 70))
print("Pesquisa com sucesso:", buscaBinaria(A, 0, len(A) - 1, 100))