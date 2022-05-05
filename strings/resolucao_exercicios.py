# Exercício 9.1

fin = open('words.txt')
for line in fin:
	word = line.strip()
	if len(word) >= 20:
		print(word)


# Exercício 9.2

def has_no_e(word):
	for letter in word:
		if letter == 'e':
			return False
	return True

has_no_e('Sandra')