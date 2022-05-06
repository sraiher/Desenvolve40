
g = [ 
            [1],           # Vizinhos do vértice 0.
            [2, 3],        # Vizinhos do vértice 1.
            [1, 4],        # Vizinhos do vértice 2.
            [0],           # Vizinhos do vértice 3.
            [1]            # Vizinhos do vértice 4.
            ]


def buscaProfundidade(grafo, vertice=0, visitados=list()):

    print(f"Você está no vértice {vertice}, seus vizinhos são {', '.join([str(x) for x in grafo[vertice]])} ", end = "")
    print(f"e você já visitou os grafos {', '.join([str(x) for x in visitados])}") if len(visitados) > 0 else print()
    
    visitados.append(vertice)
    for vizinho in grafo[vertice]:
        if vizinho not in visitados:
            buscaProfundidade(grafo, vizinho, visitados)

buscaProfundidade(g)


lista=['Curso','Python','Progressivo']

#Unindo as palavras com vírgula
print( ','.join(lista) )

#Unindo as palavras com espaço
print( ' '.join(lista) )

