<<<<<<< Updated upstream
'''
Desafio 4 - Calcule a soma de até mil termos da série 1 + 1/2 + 1/4 + 1/8 + 1/16 + ...

Dica: Use três variáveis:
• um contador, que começa em zero;
• uma variável para a soma de todos os termos, que também começa em zero;
• uma variável para cada termo, que começa em 1 e a cada loop é dividida por 2.
A repetição da soma de mil termos pode ser feita com a função while contador < 1000.

Resposta
'''
contador = 1 
soma = 0 
valor = 1 
fatorial = 1

while contador < 1000: 
	fatorial *= contador 
valor = 1/fatorial 
soma += valor 
contador +=1

print(soma)
'''
Resposta Sugerida
Apesar de ser um desafio, a programação é bem simples. 
Talvez a maior dificuldade seja entender o "matematiquês". 
Se você lembra da matemática do colégio, esse código simplesmente calcula a soma de todos os 
termos de uma P.G. (progressão geométrica) de razão 1/2 (meio).

Veja a implementação seguindo as dicas do problema:
'''
contador = 0
soma = 0
valor = 1 

while contador < 1000:
  soma += valor
  valor /= 2
  contador +=1 

print(soma)
'''
E é só isso. Se você teve como resultado o número 2 
(ou algo muito próximo como 1.99999999 por questões computacionais), você acertou.

Um pouco mais de matematiquês: se você estranhou o fato de chegar a um número inteiro pequeno, 
perceba que a cada repetição você está somando números cada vez menores a ponto de se tornarem 
desprezíveis: 1 + 1/2 + 1/4 + 1/8 + 1/16 + 1/32... Se trata de uma série geométrica convergente 
(razão < 1) majorada em 2 (isso é BEM matematiquês, não se preocupe).

Se você trocar a operação de divisão por multiplicação por exemplo, você vai ter uma 
P.G. de razão 2 e a soma vai crescer infinitamente uma vez que você está somando números 
cada vez maiores: 1 + 2 + 4 + 8 + 16 + 32...

Outras P.G. poderiam ser calculadas aqui, basta mudar o divisor (ou multiplicador) 
que aqui é 2 mas poderia ser 3, 4, 10, 20, etc.

Super Desafio! - Calcule a soma de mil termos dos inversos dos fatoriais: 
1/(1!) + 1/(2!) + 1/(3!) + 1/(4!) + ...

Dica: Assim como no exercício anterior use três variáveis: 
um contador; uma variável para a soma; e uma variável para os termos. 
Lembre-se de que 4! = 4*3*2*1 que também é igual a 4*3!.

Resposta
'''
contador = 0
fator = 1.0
soma = 0.0
while contador < 1000: fator = fator * (contador + 1)
soma = soma + (1 / fator)
contador = contador + 1
print('A soma de mil termos dos inversos dos fatoriais: 1/(1!) + 1/(2!) + 1/(3!) + ... é', soma)

'''
Resposta Sugerida
Esse super desafio é a união do desafio de Progressão Geométrica de razão 1/2 com o exercício de 
Fatorial. Matematicamente falando, teremos uma série de razão 1/n! (1 sobre fatorial de n). 
Seguindo a ideia do primeiro desafio, essa série será uma soma de valores cada vez menores e tende a se estabilizar depois de um número de iterações (repetições).

Nesse caso, além das variáveis do primeiro desafio, adicionei uma variável fatorial igual 
ao exercício de Fatorial, iniciando em 1. A cada iteração, calculamos o novo fatorial 
(que é sempre o fatorial anterior multiplicado pelo contador atual). Veja:
'''
contador = 1
soma = 0
valor = 1 
fatorial = 1

while contador < 1000:
  fatorial *= contador
  valor = 1/fatorial
  soma += valor
  contador +=1 

print(soma)
'''
Assim apenas adicionamos um passo a mais em relação ao desafio de P.G. que é calcular o fatorial 
e usá-lo na divisão no lugar do 2 (no desafio de P.G.).
=======
<<<<<<< HEAD
'''
Desafio 4 - Calcule a soma de até mil termos da série 1 + 1/2 + 1/4 + 1/8 + 1/16 + ...

Dica: Use três variáveis:
• um contador, que começa em zero;
• uma variável para a soma de todos os termos, que também começa em zero;
• uma variável para cada termo, que começa em 1 e a cada loop é dividida por 2.
A repetição da soma de mil termos pode ser feita com a função while contador < 1000.

Resposta
'''
contador = 1 
soma = 0 
valor = 1 
fatorial = 1

while contador < 1000: 
	fatorial *= contador 
valor = 1/fatorial 
soma += valor 
contador +=1

print(soma)
'''
Resposta Sugerida
Apesar de ser um desafio, a programação é bem simples. 
Talvez a maior dificuldade seja entender o "matematiquês". 
Se você lembra da matemática do colégio, esse código simplesmente calcula a soma de todos os 
termos de uma P.G. (progressão geométrica) de razão 1/2 (meio).

Veja a implementação seguindo as dicas do problema:
'''
contador = 0
soma = 0
valor = 1 

while contador < 1000:
  soma += valor
  valor /= 2
  contador +=1 

print(soma)
'''
E é só isso. Se você teve como resultado o número 2 
(ou algo muito próximo como 1.99999999 por questões computacionais), você acertou.

Um pouco mais de matematiquês: se você estranhou o fato de chegar a um número inteiro pequeno, 
perceba que a cada repetição você está somando números cada vez menores a ponto de se tornarem 
desprezíveis: 1 + 1/2 + 1/4 + 1/8 + 1/16 + 1/32... Se trata de uma série geométrica convergente 
(razão < 1) majorada em 2 (isso é BEM matematiquês, não se preocupe).

Se você trocar a operação de divisão por multiplicação por exemplo, você vai ter uma 
P.G. de razão 2 e a soma vai crescer infinitamente uma vez que você está somando números 
cada vez maiores: 1 + 2 + 4 + 8 + 16 + 32...

Outras P.G. poderiam ser calculadas aqui, basta mudar o divisor (ou multiplicador) 
que aqui é 2 mas poderia ser 3, 4, 10, 20, etc.

Super Desafio! - Calcule a soma de mil termos dos inversos dos fatoriais: 
1/(1!) + 1/(2!) + 1/(3!) + 1/(4!) + ...

Dica: Assim como no exercício anterior use três variáveis: 
um contador; uma variável para a soma; e uma variável para os termos. 
Lembre-se de que 4! = 4*3*2*1 que também é igual a 4*3!.

Resposta
'''
contador = 0
fator = 1.0
soma = 0.0
while contador < 1000: fator = fator * (contador + 1)
soma = soma + (1 / fator)
contador = contador + 1
print('A soma de mil termos dos inversos dos fatoriais: 1/(1!) + 1/(2!) + 1/(3!) + ... é', soma)

'''
Resposta Sugerida
Esse super desafio é a união do desafio de Progressão Geométrica de razão 1/2 com o exercício de 
Fatorial. Matematicamente falando, teremos uma série de razão 1/n! (1 sobre fatorial de n). 
Seguindo a ideia do primeiro desafio, essa série será uma soma de valores cada vez menores e tende a se estabilizar depois de um número de iterações (repetições).

Nesse caso, além das variáveis do primeiro desafio, adicionei uma variável fatorial igual 
ao exercício de Fatorial, iniciando em 1. A cada iteração, calculamos o novo fatorial 
(que é sempre o fatorial anterior multiplicado pelo contador atual). Veja:
'''
contador = 1
soma = 0
valor = 1 
fatorial = 1

while contador < 1000:
  fatorial *= contador
  valor = 1/fatorial
  soma += valor
  contador +=1 

print(soma)
'''
Assim apenas adicionamos um passo a mais em relação ao desafio de P.G. que é calcular o fatorial 
e usá-lo na divisão no lugar do 2 (no desafio de P.G.).
=======
'''
Desafio 4 - Calcule a soma de até mil termos da série 1 + 1/2 + 1/4 + 1/8 + 1/16 + ...

Dica: Use três variáveis:
• um contador, que começa em zero;
• uma variável para a soma de todos os termos, que também começa em zero;
• uma variável para cada termo, que começa em 1 e a cada loop é dividida por 2.
A repetição da soma de mil termos pode ser feita com a função while contador < 1000.

Resposta
'''
contador = 1 
soma = 0 
valor = 1 
fatorial = 1

while contador < 1000: 
	fatorial *= contador 
valor = 1/fatorial 
soma += valor 
contador +=1

print(soma)
'''
Resposta Sugerida
Apesar de ser um desafio, a programação é bem simples. 
Talvez a maior dificuldade seja entender o "matematiquês". 
Se você lembra da matemática do colégio, esse código simplesmente calcula a soma de todos os 
termos de uma P.G. (progressão geométrica) de razão 1/2 (meio).

Veja a implementação seguindo as dicas do problema:
'''
contador = 0
soma = 0
valor = 1 

while contador < 1000:
  soma += valor
  valor /= 2
  contador +=1 

print(soma)
'''
E é só isso. Se você teve como resultado o número 2 
(ou algo muito próximo como 1.99999999 por questões computacionais), você acertou.

Um pouco mais de matematiquês: se você estranhou o fato de chegar a um número inteiro pequeno, 
perceba que a cada repetição você está somando números cada vez menores a ponto de se tornarem 
desprezíveis: 1 + 1/2 + 1/4 + 1/8 + 1/16 + 1/32... Se trata de uma série geométrica convergente 
(razão < 1) majorada em 2 (isso é BEM matematiquês, não se preocupe).

Se você trocar a operação de divisão por multiplicação por exemplo, você vai ter uma 
P.G. de razão 2 e a soma vai crescer infinitamente uma vez que você está somando números 
cada vez maiores: 1 + 2 + 4 + 8 + 16 + 32...

Outras P.G. poderiam ser calculadas aqui, basta mudar o divisor (ou multiplicador) 
que aqui é 2 mas poderia ser 3, 4, 10, 20, etc.

Super Desafio! - Calcule a soma de mil termos dos inversos dos fatoriais: 
1/(1!) + 1/(2!) + 1/(3!) + 1/(4!) + ...

Dica: Assim como no exercício anterior use três variáveis: 
um contador; uma variável para a soma; e uma variável para os termos. 
Lembre-se de que 4! = 4*3*2*1 que também é igual a 4*3!.

Resposta
'''
contador = 0
fator = 1.0
soma = 0.0
while contador < 1000: fator = fator * (contador + 1)
soma = soma + (1 / fator)
contador = contador + 1
print('A soma de mil termos dos inversos dos fatoriais: 1/(1!) + 1/(2!) + 1/(3!) + ... é', soma)

'''
Resposta Sugerida
Esse super desafio é a união do desafio de Progressão Geométrica de razão 1/2 com o exercício de 
Fatorial. Matematicamente falando, teremos uma série de razão 1/n! (1 sobre fatorial de n). 
Seguindo a ideia do primeiro desafio, essa série será uma soma de valores cada vez menores e tende a se estabilizar depois de um número de iterações (repetições).

Nesse caso, além das variáveis do primeiro desafio, adicionei uma variável fatorial igual 
ao exercício de Fatorial, iniciando em 1. A cada iteração, calculamos o novo fatorial 
(que é sempre o fatorial anterior multiplicado pelo contador atual). Veja:
'''
contador = 1
soma = 0
valor = 1 
fatorial = 1

while contador < 1000:
  fatorial *= contador
  valor = 1/fatorial
  soma += valor
  contador +=1 

print(soma)
'''
Assim apenas adicionamos um passo a mais em relação ao desafio de P.G. que é calcular o fatorial 
e usá-lo na divisão no lugar do 2 (no desafio de P.G.).
>>>>>>> 52e15950b8515da1dec547f128fcb8e14736a285
>>>>>>> Stashed changes
'''