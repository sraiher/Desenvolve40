


def buscaBinaria(lista, idxEsquerda, idxDireita, item):
    if idxDireita < idxEsquerda:
        return -1

    meio = (idxDireita + idxEsquerda) // 2

    if lista[meio] == item:
        return meio
    elif lista[meio] > item:
        return buscaBinaria(lista, idxEsquerda, meio - 1, item)
    else:
        return buscaBinaria(lista, meio + 1, idxDireita, item)

A = [0, 10, 20, 30, 40, 50, 60, 70]

print('Pesquisa com sucesso:', buscaBinaria(A, 0, len(A) - 1, 20))
print('Pesquisa com sucesso:', buscaBinaria(A, 0, len(A) - 1, 0))
print('Pesquisa com sucesso:', buscaBinaria(A, 0, len(A) - 1, 70))
print('Pesquisa com sucesso:', buscaBinaria(A, 0, len(A) - 1, 100))

#retorna a posição do número buscado.