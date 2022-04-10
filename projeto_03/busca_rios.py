'''
matrix = [	[1, 0, 0, 1, 0],
			[1, 0, 1, 0, 0],
			[0, 0, 1, 0, 1],
			[1, 0, 1, 0, 1],
			[1, 0, 1, 1, 0]
		]

matrix = [
    [1, 0],
    [1, 0],
    [0, 0],
    [0, 1],
    [1, 0],
]
'''
matrix = [
    [0, 0, 0, 1, 1],
    [1, 0, 1, 0, 1],
]
def mede_rio(matrix, i, j):
	tamanho = 1
	if i+1 < len(matrix) and matrix[i+1][j] == 1:
		matrix[i+1][j] = 'r'
		tamanho += mede_rio(matrix, i+1, j)
    
	if i-1 >= 0 and matrix[i-1][j] == 1:
		matrix[i-1][j] = 'r'
		tamanho += mede_rio(matrix, i-1, j)

	if j+1 < len(matrix[i]) and matrix[i][j+1] == 1:
			matrix[i][j+1] = 'r'
			tamanho += mede_rio(matrix, i, j+1)

	if j-1 >=0 and matrix[i][j-1] == 1:
		matrix[i][j-1] = 'r'
		tamanho += mede_rio(matrix, i, j-1)
	return tamanho
	
def conta_rios(matrix):
	tamanho_rio = []
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if (matrix[i][j] == 1):
				print(f'rio começa: {i},{j}')
				matrix[i][j] = -1
				tamanho_rio.append(mede_rio(matrix, i, j))		
	return tamanho_rio

conta = conta_rios(matrix)
print(conta)


