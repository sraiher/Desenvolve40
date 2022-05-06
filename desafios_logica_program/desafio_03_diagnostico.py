<<<<<<< Updated upstream
'''
Desafio 3 - Um hospital quer fazer o diagnóstico de gripe ou dengue a partir de um 
questionário de sintomas, tendo as perguntas abaixo, 
faça um programa que faça o diagnóstico deste hospital:
a. Sente dor no corpo?
b. Você tem febre?
c. Você tem tosse?
d. Está com congestão nasal?
e. Tem manchas pelo corpo?
Para o diagnóstico ele tem a seguinte tabela:

A	B	C	D	E	Resultado
Sim	Sim	Não	Não	Sim	Dengue
Sim	Sim	Sim	Sim	Não	Gripe
Não	Sim	Sim	Sim	Não	Gripe
Sim	Não	Não	Não	Não	Sem doenças
Não	Não	Não	Não	Não	Sem doenças

Resposta
'''
dor = (input('Sente dor, sim ou não: ')) 
febre = (input('Tem febre, sim ou não: ')) 
tosse = (input('Está tossindo, sim ou não: ')) 
congestao = (input('Está congestionado, sim ou não: ')) 
manchas = (input('Tem manchas pelo corpo?, sim ou não: '))

# Sim Sim Não Não Sim Dengue
if dor == 'sim' and febre == 'sim' and tosse != 'sim' and congestao != 'sim' and manchas == 'sim': print('dengue')

# Sim Sim Sim Sim Não Gripe
elif dor == 'sim' and febre == 'sim' and tosse == 'sim' and congestao == 'sim' and manchas != 'sim': print('gripe')

# Não Sim Sim Sim Não Gripe
elif dor !='sim' and febre == 'sim' and tosse == 'sim' and congestao == 'sim' and manchas != 'sim': print('gripe')

# Sim Não Não Não Não Sem doenças
elif dor =='sim' and febre != 'sim' and tosse != 'sim' and congestao != 'sim' and manchas != 'sim': (print)('sem doença')

# Não Não Não Não Não Sem doenças
elif dor !='sim' and febre != 'sim' and tosse != 'sim' and congestao != 'sim' and manchas != 'sim': print('sem doenca') 
else: print('doença não identificada')

'''
Resposta Sugerida
Lembra do exercício de investigação? Pois é, agora temos mais um. 
Aqui, porém, é um pouco diferente. 
Nós recebemos respostas de "Sim" ou "Não" para várias perguntas relacioandas a sintomas de saúde 
e ao final, passamos um diagnóstico.

Aqui, nós verificamos combinações de ambos "Sim" e "Não" a fim de chegar no diagnóstico correto. 
Dessa vez, não podemos usar uma só variável para contabilizar porque as respostas significam 
coisas diferentes e a ordem das perguntas influenciam no resultado final.

Para fazer isso nós podemos, por exemplo, fazer IFs e ELIFs com várias condições unidas por operadores lógicos a fim de identificar a enfermidade.
'''
A = input("Sente dor no corpo? ")
B = input("Você tem febre? ")
C = input("Você tem tosse? ")
D = input("Está com congestão nasal? ")
E = input("Tem manchas pelo corpo? ")

# Uma das formas de resolver o problema:
if B == 'Não' and C == 'Não' and D == 'Não' and E == 'Não':
    print("Sem doenças")
elif B == 'Sim' and C == 'Sim' and D == 'Sim' and E == 'Não':
    print("Gripe")
elif A == 'Sim' and B == 'Sim' and C == 'Não' and D == 'Não' and E == 'Sim':
    print("Dengue")
else:
    print("Sem diagnóstico possível")

'''
Assim, cada linha de IF ou ELIF busca identificar uma das possibilidades 
("Sem doenças", "Gripe" ou "Dengue") e o ELSE, se ocorrer, informa que não foi possível chegar a 
um diagnóstico exato.

Apesar de parecer um sistema bastante precário, em um nível mais elevado poderíamos 
usar uam abordagem parecida para prever diagnósticos com auxílio da Inteligência Artificial e 
do Aprendizado de Máquinas. Utilizando vários dados do paciente e comparando com modelos preditivos 
realizados com auxílio de um enorme banco de dados de diagnósticos e sintomas, 
poderíamos obter resultados interessantes.
=======
<<<<<<< HEAD
'''
Desafio 3 - Um hospital quer fazer o diagnóstico de gripe ou dengue a partir de um 
questionário de sintomas, tendo as perguntas abaixo, 
faça um programa que faça o diagnóstico deste hospital:
a. Sente dor no corpo?
b. Você tem febre?
c. Você tem tosse?
d. Está com congestão nasal?
e. Tem manchas pelo corpo?
Para o diagnóstico ele tem a seguinte tabela:

A	B	C	D	E	Resultado
Sim	Sim	Não	Não	Sim	Dengue
Sim	Sim	Sim	Sim	Não	Gripe
Não	Sim	Sim	Sim	Não	Gripe
Sim	Não	Não	Não	Não	Sem doenças
Não	Não	Não	Não	Não	Sem doenças

Resposta
'''
dor = (input('Sente dor, sim ou não: ')) 
febre = (input('Tem febre, sim ou não: ')) 
tosse = (input('Está tossindo, sim ou não: ')) 
congestao = (input('Está congestionado, sim ou não: ')) 
manchas = (input('Tem manchas pelo corpo?, sim ou não: '))

# Sim Sim Não Não Sim Dengue
if dor == 'sim' and febre == 'sim' and tosse != 'sim' and congestao != 'sim' and manchas == 'sim': print('dengue')

# Sim Sim Sim Sim Não Gripe
elif dor == 'sim' and febre == 'sim' and tosse == 'sim' and congestao == 'sim' and manchas != 'sim': print('gripe')

# Não Sim Sim Sim Não Gripe
elif dor !='sim' and febre == 'sim' and tosse == 'sim' and congestao == 'sim' and manchas != 'sim': print('gripe')

# Sim Não Não Não Não Sem doenças
elif dor =='sim' and febre != 'sim' and tosse != 'sim' and congestao != 'sim' and manchas != 'sim': (print)('sem doença')

# Não Não Não Não Não Sem doenças
elif dor !='sim' and febre != 'sim' and tosse != 'sim' and congestao != 'sim' and manchas != 'sim': print('sem doenca') 
else: print('doença não identificada')

'''
Resposta Sugerida
Lembra do exercício de investigação? Pois é, agora temos mais um. 
Aqui, porém, é um pouco diferente. 
Nós recebemos respostas de "Sim" ou "Não" para várias perguntas relacioandas a sintomas de saúde 
e ao final, passamos um diagnóstico.

Aqui, nós verificamos combinações de ambos "Sim" e "Não" a fim de chegar no diagnóstico correto. 
Dessa vez, não podemos usar uma só variável para contabilizar porque as respostas significam 
coisas diferentes e a ordem das perguntas influenciam no resultado final.

Para fazer isso nós podemos, por exemplo, fazer IFs e ELIFs com várias condições unidas por operadores lógicos a fim de identificar a enfermidade.
'''
A = input("Sente dor no corpo? ")
B = input("Você tem febre? ")
C = input("Você tem tosse? ")
D = input("Está com congestão nasal? ")
E = input("Tem manchas pelo corpo? ")

# Uma das formas de resolver o problema:
if B == 'Não' and C == 'Não' and D == 'Não' and E == 'Não':
    print("Sem doenças")
elif B == 'Sim' and C == 'Sim' and D == 'Sim' and E == 'Não':
    print("Gripe")
elif A == 'Sim' and B == 'Sim' and C == 'Não' and D == 'Não' and E == 'Sim':
    print("Dengue")
else:
    print("Sem diagnóstico possível")

'''
Assim, cada linha de IF ou ELIF busca identificar uma das possibilidades 
("Sem doenças", "Gripe" ou "Dengue") e o ELSE, se ocorrer, informa que não foi possível chegar a 
um diagnóstico exato.

Apesar de parecer um sistema bastante precário, em um nível mais elevado poderíamos 
usar uam abordagem parecida para prever diagnósticos com auxílio da Inteligência Artificial e 
do Aprendizado de Máquinas. Utilizando vários dados do paciente e comparando com modelos preditivos 
realizados com auxílio de um enorme banco de dados de diagnósticos e sintomas, 
poderíamos obter resultados interessantes.
=======
'''
Desafio 3 - Um hospital quer fazer o diagnóstico de gripe ou dengue a partir de um 
questionário de sintomas, tendo as perguntas abaixo, 
faça um programa que faça o diagnóstico deste hospital:
a. Sente dor no corpo?
b. Você tem febre?
c. Você tem tosse?
d. Está com congestão nasal?
e. Tem manchas pelo corpo?
Para o diagnóstico ele tem a seguinte tabela:

A	B	C	D	E	Resultado
Sim	Sim	Não	Não	Sim	Dengue
Sim	Sim	Sim	Sim	Não	Gripe
Não	Sim	Sim	Sim	Não	Gripe
Sim	Não	Não	Não	Não	Sem doenças
Não	Não	Não	Não	Não	Sem doenças

Resposta
'''
dor = (input('Sente dor, sim ou não: ')) 
febre = (input('Tem febre, sim ou não: ')) 
tosse = (input('Está tossindo, sim ou não: ')) 
congestao = (input('Está congestionado, sim ou não: ')) 
manchas = (input('Tem manchas pelo corpo?, sim ou não: '))

# Sim Sim Não Não Sim Dengue
if dor == 'sim' and febre == 'sim' and tosse != 'sim' and congestao != 'sim' and manchas == 'sim': print('dengue')

# Sim Sim Sim Sim Não Gripe
elif dor == 'sim' and febre == 'sim' and tosse == 'sim' and congestao == 'sim' and manchas != 'sim': print('gripe')

# Não Sim Sim Sim Não Gripe
elif dor !='sim' and febre == 'sim' and tosse == 'sim' and congestao == 'sim' and manchas != 'sim': print('gripe')

# Sim Não Não Não Não Sem doenças
elif dor =='sim' and febre != 'sim' and tosse != 'sim' and congestao != 'sim' and manchas != 'sim': (print)('sem doença')

# Não Não Não Não Não Sem doenças
elif dor !='sim' and febre != 'sim' and tosse != 'sim' and congestao != 'sim' and manchas != 'sim': print('sem doenca') 
else: print('doença não identificada')

'''
Resposta Sugerida
Lembra do exercício de investigação? Pois é, agora temos mais um. 
Aqui, porém, é um pouco diferente. 
Nós recebemos respostas de "Sim" ou "Não" para várias perguntas relacioandas a sintomas de saúde 
e ao final, passamos um diagnóstico.

Aqui, nós verificamos combinações de ambos "Sim" e "Não" a fim de chegar no diagnóstico correto. 
Dessa vez, não podemos usar uma só variável para contabilizar porque as respostas significam 
coisas diferentes e a ordem das perguntas influenciam no resultado final.

Para fazer isso nós podemos, por exemplo, fazer IFs e ELIFs com várias condições unidas por operadores lógicos a fim de identificar a enfermidade.
'''
A = input("Sente dor no corpo? ")
B = input("Você tem febre? ")
C = input("Você tem tosse? ")
D = input("Está com congestão nasal? ")
E = input("Tem manchas pelo corpo? ")

# Uma das formas de resolver o problema:
if B == 'Não' and C == 'Não' and D == 'Não' and E == 'Não':
    print("Sem doenças")
elif B == 'Sim' and C == 'Sim' and D == 'Sim' and E == 'Não':
    print("Gripe")
elif A == 'Sim' and B == 'Sim' and C == 'Não' and D == 'Não' and E == 'Sim':
    print("Dengue")
else:
    print("Sem diagnóstico possível")

'''
Assim, cada linha de IF ou ELIF busca identificar uma das possibilidades 
("Sem doenças", "Gripe" ou "Dengue") e o ELSE, se ocorrer, informa que não foi possível chegar a 
um diagnóstico exato.

Apesar de parecer um sistema bastante precário, em um nível mais elevado poderíamos 
usar uam abordagem parecida para prever diagnósticos com auxílio da Inteligência Artificial e 
do Aprendizado de Máquinas. Utilizando vários dados do paciente e comparando com modelos preditivos 
realizados com auxílio de um enorme banco de dados de diagnósticos e sintomas, 
poderíamos obter resultados interessantes.
>>>>>>> 52e15950b8515da1dec547f128fcb8e14736a285
>>>>>>> Stashed changes
'''