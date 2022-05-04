'''
fin = open('words.txt')
fin.readline()
line = fin.readline()
word = line.strip()
print(word)

fin = open('words.txt')
for line in fin:
	word = line.strip
print(word)
fin.close()

Exercício 9.1

Escreva um programa que leia words.txt e imprima palavras com mais de 20 caracteres (sem contar whitespaces)

'''
fin = open('words.txt')



for line in fin:
	word = line.strip
	if len(word) >= 20:
		print(word)