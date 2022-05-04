'''
arquivo = open('olá.txt', 'w') # além de criar ou abrir, permite a edição 
arquivo.write('Olá mundo!') # escreve "Olá mundo" no arquivo
arquivo.close # fecha e salva o arquivo

arquivo = open('olá.txt', 'r')
conteudo = arquivo.read()
print(conteudo)
arquivo.close()


tabela = [['Aluno', 'Nota1', 'Nota2', 'Presenças'],
		['Luke', 7, 9, 15],
		['Han', 4, 7, 10],
		['Leia', 9, 9, 16]]

print('Imprimindo cada elemento individual da tabela')
for linha in tabela:
	for elemento in linha:
		print(elemento)

print('Imprimendo cada "linha" da tabela')
for linha in tabela:
	print(linha)


print('Imprimindo o elemento na linha 2, coluna 0:')
print(tabela[2][0])


import csv 

tabela = [['Aluno', 'Nota1', 'Nota2', 'Presenças'],
		['Luke', 7, 9, 15],
		['Han', 4, 7, 10],
		['Leia', 9, 9, 16]]

# cria um arquivo csv
arquivo = open('alunos.csv', 'w')

# definindo as regras do nosso CSV:
# ele será escrito no arquivo apontado pela variável 'arquivo'
# seus elementos serão delimitados (delimiter) pelo símbolo ';'
# suas linhas serão encerradas (lineterminator) por uma quebra de linha

escritor = csv.writer(arquivo, delimiter=';', lineterminator='\n')

# escreve uma lista em formato csv
escritor.writerows(tabela)

# fecha e salva o arquivo
arquivo.close()
'''
import csv

arquivo = open('alunos.csv', 'r')

planilha = csv.reader(arquivo, delimiter=';', lineterminator='\n')

for linha in planilha:
    print(linha)

arquivo.close()