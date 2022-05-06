matrix = [[1, 0, 0, 1, 0],
[1, 0, 1, 0, 0],
[0, 0, 1, 0, 1],
[1, 0, 1, 0, 1],
[1, 0, 1, 1, 0]
]

def bfs(matrix, vertice_fonte):
		visitados, fila = list(), [vertice_fonte]
		while fila:
			vertice = fila.pop(0)
			if vertice not in visitados:
				visitados.append(vertice)
				fila.extend([x for x in matrix[vertice] if x not in visitados])
		return visitados

print(visitados)