



def somaTudo(lista):
    soma = 0
    for elemento in lista:
        if type(elemento) == int:
            soma += elemento
        else:
            soma += somaTudo(elemento)
    return soma

listaGabarito = [[0, 3, 5, 1], 2, 3, [2, [5, 6, 7, [1, 4, 6]], 3], 2, [3, 5, 10, [6]]]
print(somaTudo(listaGabarito))