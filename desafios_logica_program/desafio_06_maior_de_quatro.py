<<<<<<< Updated upstream
'''
Desafio 6 - Faça o mesmo programa do exercício anterior, porém com 4 números.

Resposta
'''
n1 = float(input('Digite o primeiro número: ')) 
n2 = float(input('Digite o segundo número: ')) 
n3 = float(input('Digite o terceiro número: ')) 
n4 = float(input('Digite o quarto número: '))

if (n1 > n2 and n1 > n3) and n1 > n4: print('O maior número é:', n1) 
elif (n2 > n1 and n2 > n3) and n2 > n4: print(('O maior número é:', n2)) 
elif (n3> n1 and n3 > n2) and n3 > n4: print('O maior número é:,', n3) 
else: print('O maior número é:,', n4)

'''
Resposta Sugerida
Eita, e agora? Dá pra utilizar o mesmo método que realizamos para comparar 3 valores? 
Sim, mas fica bem mais confuso. Aqui podemos usar uma abordagem bem mais simples e, 
na verdade, mais elegante.

Vamos começar assumindo ao acaso qual é o maior número colocado. Aqui, escolhemos o primeiro. Ou seja, logo após as entradas do usuário, guardamos a primeira na variável maior_numero.

Depois, uma a uma, verificamos se as outras são maiores que o valor guardado na variável. 
Se for, trocamos. Assim, a cada comparação sempre temos armazenado o maior valor entre todos já verificado com certeza.

Ao final, temos o maior valor na variável maior_numero.

Pelo desafio anterior, podemos perceber que essa estrutura é insustentável para muitos números.
Podemos fazer o exercício de uma forma diferente.
'''

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))
numero3 = int(input("Digite outro número: "))
numero4 = int(input("Digite outro número: "))

maior_numero = numero1
if numero2 > maior_numero:
    maior_numero = numero2
if numero3 > maior_numero:
    maior_numero = numero3
if numero4 > maior_numero:
    maior_numero = numero4

print("O maior número é", maior_numero)
'''
Apesar de parecer estranho, não é algo incomum. 
Em cálculos probabilísticos e/ou estatísticos, geralmente assumimos hipoteses verdadeiras no 
início dos cálculos para depois de uma série de experimentações, chegar a um resultado mais correto.
=======
<<<<<<< HEAD
'''
Desafio 6 - Faça o mesmo programa do exercício anterior, porém com 4 números.

Resposta
'''
n1 = float(input('Digite o primeiro número: ')) 
n2 = float(input('Digite o segundo número: ')) 
n3 = float(input('Digite o terceiro número: ')) 
n4 = float(input('Digite o quarto número: '))

if (n1 > n2 and n1 > n3) and n1 > n4: print('O maior número é:', n1) 
elif (n2 > n1 and n2 > n3) and n2 > n4: print(('O maior número é:', n2)) 
elif (n3> n1 and n3 > n2) and n3 > n4: print('O maior número é:,', n3) 
else: print('O maior número é:,', n4)

'''
Resposta Sugerida
Eita, e agora? Dá pra utilizar o mesmo método que realizamos para comparar 3 valores? 
Sim, mas fica bem mais confuso. Aqui podemos usar uma abordagem bem mais simples e, 
na verdade, mais elegante.

Vamos começar assumindo ao acaso qual é o maior número colocado. Aqui, escolhemos o primeiro. Ou seja, logo após as entradas do usuário, guardamos a primeira na variável maior_numero.

Depois, uma a uma, verificamos se as outras são maiores que o valor guardado na variável. 
Se for, trocamos. Assim, a cada comparação sempre temos armazenado o maior valor entre todos já verificado com certeza.

Ao final, temos o maior valor na variável maior_numero.

Pelo desafio anterior, podemos perceber que essa estrutura é insustentável para muitos números.
Podemos fazer o exercício de uma forma diferente.
'''

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))
numero3 = int(input("Digite outro número: "))
numero4 = int(input("Digite outro número: "))

maior_numero = numero1
if numero2 > maior_numero:
    maior_numero = numero2
if numero3 > maior_numero:
    maior_numero = numero3
if numero4 > maior_numero:
    maior_numero = numero4

print("O maior número é", maior_numero)
'''
Apesar de parecer estranho, não é algo incomum. 
Em cálculos probabilísticos e/ou estatísticos, geralmente assumimos hipoteses verdadeiras no 
início dos cálculos para depois de uma série de experimentações, chegar a um resultado mais correto.
=======
'''
Desafio 6 - Faça o mesmo programa do exercício anterior, porém com 4 números.

Resposta
'''
n1 = float(input('Digite o primeiro número: ')) 
n2 = float(input('Digite o segundo número: ')) 
n3 = float(input('Digite o terceiro número: ')) 
n4 = float(input('Digite o quarto número: '))

if (n1 > n2 and n1 > n3) and n1 > n4: print('O maior número é:', n1) 
elif (n2 > n1 and n2 > n3) and n2 > n4: print(('O maior número é:', n2)) 
elif (n3> n1 and n3 > n2) and n3 > n4: print('O maior número é:,', n3) 
else: print('O maior número é:,', n4)

'''
Resposta Sugerida
Eita, e agora? Dá pra utilizar o mesmo método que realizamos para comparar 3 valores? 
Sim, mas fica bem mais confuso. Aqui podemos usar uma abordagem bem mais simples e, 
na verdade, mais elegante.

Vamos começar assumindo ao acaso qual é o maior número colocado. Aqui, escolhemos o primeiro. Ou seja, logo após as entradas do usuário, guardamos a primeira na variável maior_numero.

Depois, uma a uma, verificamos se as outras são maiores que o valor guardado na variável. 
Se for, trocamos. Assim, a cada comparação sempre temos armazenado o maior valor entre todos já verificado com certeza.

Ao final, temos o maior valor na variável maior_numero.

Pelo desafio anterior, podemos perceber que essa estrutura é insustentável para muitos números.
Podemos fazer o exercício de uma forma diferente.
'''

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))
numero3 = int(input("Digite outro número: "))
numero4 = int(input("Digite outro número: "))

maior_numero = numero1
if numero2 > maior_numero:
    maior_numero = numero2
if numero3 > maior_numero:
    maior_numero = numero3
if numero4 > maior_numero:
    maior_numero = numero4

print("O maior número é", maior_numero)
'''
Apesar de parecer estranho, não é algo incomum. 
Em cálculos probabilísticos e/ou estatísticos, geralmente assumimos hipoteses verdadeiras no 
início dos cálculos para depois de uma série de experimentações, chegar a um resultado mais correto.
>>>>>>> 52e15950b8515da1dec547f128fcb8e14736a285
>>>>>>> Stashed changes
'''