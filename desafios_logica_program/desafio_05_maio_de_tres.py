<<<<<<< Updated upstream
'''
Desafio 5 - Faça um programa que leia 3 números e informe o maior deles.

Resposta
'''
n1 = float(input('Digite o primeiro número: ')) 
n2 = float(input('Digite o segundo número: ')) 
n3 = float(input('Digite o terceiro número: '))

if n1 > n2 and n1 > n3: print('O maior número é:', n1) 
elif n2 > n1 and n2 > n3: print(('O maior número é:', n2)) 
else: print('O maior número é:,', n3)

'''
Resposta Sugerida
Nós já fizemos um programa que verificava qual era o maior entre dois números. Agora só precisamos fazer com três. Simples, né?

Qual é o desafio aqui então?

Bom, é possível que você tenha resolvido de maneira simples e obtido os resultados corretos. Contudo, vamos utilizar aqui um método que funciona bem para 3 valores que servirá para exercitar uma abordagem diferente.

Nesse caso, pensamos em encadear condicionais para verificar os 3 números seguindo alguma ordem como: primeiro verifico o primeiro com o segundo, depois o maior deles com o terceiro. Entre as possíveis combinações, seguiremos com essa. Veja:
'''
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))
if numero1 > numero2:
    if numero1 > numero3:
        print(numero1)
    else:
        print(numero3)
else:
    if numero2 > numero3:
        print(numero2)
    else:
        print(numero3)

'''
Olha que interessante. Primeiro precisamos verificar, entre dois valores, qual é o maior. 
Depois pegamos o maior deles e comparamos com o terceiro. Assim saberemos qual é o maior de todos.

Para isso nós utilizamos um IF para verificar se o numero1 era maior que o numero2. 
Se for, ele entraria num IF dentro do primeiro que verificaria se ele era maior que o numero3. 
Caso fosse, seria o maior dos 3. Caso contrário, o numero3 seria o maior.

Caso caíssemos no ELSE do primeiro IF, o numero2 seria maior que o numero1 e nós 
realizamos o mesmo processo no IF dentro do ELSE agora, e descobririamos se o 
maior de todos é o numero2 ou o numero3.

Fez sentido? Espero que sim!
=======
'''
Desafio 5 - Faça um programa que leia 3 números e informe o maior deles.

Resposta
'''
n1 = float(input('Digite o primeiro número: ')) 
n2 = float(input('Digite o segundo número: ')) 
n3 = float(input('Digite o terceiro número: '))

if n1 > n2 and n1 > n3: print('O maior número é:', n1) 
elif n2 > n1 and n2 > n3: print(('O maior número é:', n2)) 
else: print('O maior número é:,', n3)

'''
Resposta Sugerida
Nós já fizemos um programa que verificava qual era o maior entre dois números. Agora só precisamos fazer com três. Simples, né?

Qual é o desafio aqui então?

Bom, é possível que você tenha resolvido de maneira simples e obtido os resultados corretos. Contudo, vamos utilizar aqui um método que funciona bem para 3 valores que servirá para exercitar uma abordagem diferente.

Nesse caso, pensamos em encadear condicionais para verificar os 3 números seguindo alguma ordem como: primeiro verifico o primeiro com o segundo, depois o maior deles com o terceiro. Entre as possíveis combinações, seguiremos com essa. Veja:
'''
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))
if numero1 > numero2:
    if numero1 > numero3:
        print(numero1)
    else:
        print(numero3)
else:
    if numero2 > numero3:
        print(numero2)
    else:
        print(numero3)

'''
Olha que interessante. Primeiro precisamos verificar, entre dois valores, qual é o maior. 
Depois pegamos o maior deles e comparamos com o terceiro. Assim saberemos qual é o maior de todos.

Para isso nós utilizamos um IF para verificar se o numero1 era maior que o numero2. 
Se for, ele entraria num IF dentro do primeiro que verificaria se ele era maior que o numero3. 
Caso fosse, seria o maior dos 3. Caso contrário, o numero3 seria o maior.

Caso caíssemos no ELSE do primeiro IF, o numero2 seria maior que o numero1 e nós 
realizamos o mesmo processo no IF dentro do ELSE agora, e descobririamos se o 
maior de todos é o numero2 ou o numero3.

Fez sentido? Espero que sim!
>>>>>>> Stashed changes
'''