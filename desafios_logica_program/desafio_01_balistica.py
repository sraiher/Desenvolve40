<<<<<<< Updated upstream
'''
Desafio 1 - Peça para o usuário digitar uma velocidade inicial (em m/s), 
uma posição inicial (em m) e um instante de tempo (em s) e imprima a posição 
de um projétil nesse instante de tempo.

Use a fórmula matemática:

y(t) = y(0) + v(0)*t + (g*(t**2)/2)

Onde, g é a aceleração da gravidade (-10m/s²), y(t) é a posição final, 
y(0) é a posição inicial, v(0) é a velocidade inicial e t é o instante de tempo.

Resposta
'''
velocidade_inicial = float(input('Digite a velocidade inicial: ')) 
posicao_inicial = float(input('Digite a posição inicial: ')) 
tempo = float(input('Digite o instante de tempo: ')) 
g = -10 # aceleração gravitacional

posicao = posicao_inicial + (velocidade_inicial*tempo) + (g/2*tempo**2)

print(posicao, "m")

'''
Resposta Sugerida

Você pode estar se perguntando: "QUÊ?!" Mas calma, a dificuldade desse exercício não é diferente 
dos outros de conversão de temperatura ou cálculo da área de um círculo por exemplo. 
É apenas uma fórmula da Cinemática (parte da Física que estuda o movimento dos corpos) 
utilizada para calcular a posição de um projétil balístico.
 
Aqui consideramos a velocidade e posição inicial, a aceleração da gravidade e o 
instante de tempo que se quer analizar. 
Para isso pedimos 3 dessas 4 informações uma vez que a aceleração da gravidade 
é uma constante física que aproximamos aqui para -10 m/s².
'''
y0 = float(input("Digite a posição inicial: "))
v0 = float(input("Digite a velocidade inicial: "))
t = float(input("Digite um instante no tempo: "))
g = -10

y = y0 + v0*t + 0.5*g*t**2

print("A posição no instante t =", t, "é", y)

'''
Mas por que eu estou fazendo um código pra isso?" 
Bom, primeiro para exercitar a programação. 
Mas um fato interessante é que a computação passou por um importante período de 
desenvolvimento durante a Segunda Guerra Mundial e um dos primeiros computadores 
eletromecânicos criados tinha como objetivo justamente realizar cálculos balísticos. 
O nome dele é ENIAC (Electronic Numerical Integrator and Computer), 
pesava 30 toneladas e ocupava 180m² além de não ter poder maior que uma calculadora 
de bolso hoje em dia.
=======
<<<<<<< HEAD
'''
Desafio 1 - Peça para o usuário digitar uma velocidade inicial (em m/s), 
uma posição inicial (em m) e um instante de tempo (em s) e imprima a posição 
de um projétil nesse instante de tempo.

Use a fórmula matemática:

y(t) = y(0) + v(0)*t + (g*(t**2)/2)

Onde, g é a aceleração da gravidade (-10m/s²), y(t) é a posição final, 
y(0) é a posição inicial, v(0) é a velocidade inicial e t é o instante de tempo.

Resposta
'''
velocidade_inicial = float(input('Digite a velocidade inicial: ')) 
posicao_inicial = float(input('Digite a posição inicial: ')) 
tempo = float(input('Digite o instante de tempo: ')) 
g = -10 # aceleração gravitacional

posicao = posicao_inicial + (velocidade_inicial*tempo) + (g/2*tempo**2)

print(posicao, "m")

'''
Resposta Sugerida

Você pode estar se perguntando: "QUÊ?!" Mas calma, a dificuldade desse exercício não é diferente 
dos outros de conversão de temperatura ou cálculo da área de um círculo por exemplo. 
É apenas uma fórmula da Cinemática (parte da Física que estuda o movimento dos corpos) 
utilizada para calcular a posição de um projétil balístico.
 
Aqui consideramos a velocidade e posição inicial, a aceleração da gravidade e o 
instante de tempo que se quer analizar. 
Para isso pedimos 3 dessas 4 informações uma vez que a aceleração da gravidade 
é uma constante física que aproximamos aqui para -10 m/s².
'''
y0 = float(input("Digite a posição inicial: "))
v0 = float(input("Digite a velocidade inicial: "))
t = float(input("Digite um instante no tempo: "))
g = -10

y = y0 + v0*t + 0.5*g*t**2

print("A posição no instante t =", t, "é", y)

'''
Mas por que eu estou fazendo um código pra isso?" 
Bom, primeiro para exercitar a programação. 
Mas um fato interessante é que a computação passou por um importante período de 
desenvolvimento durante a Segunda Guerra Mundial e um dos primeiros computadores 
eletromecânicos criados tinha como objetivo justamente realizar cálculos balísticos. 
O nome dele é ENIAC (Electronic Numerical Integrator and Computer), 
pesava 30 toneladas e ocupava 180m² além de não ter poder maior que uma calculadora 
de bolso hoje em dia.
=======
'''
Desafio 1 - Peça para o usuário digitar uma velocidade inicial (em m/s), 
uma posição inicial (em m) e um instante de tempo (em s) e imprima a posição 
de um projétil nesse instante de tempo.

Use a fórmula matemática:

y(t) = y(0) + v(0)*t + (g*(t**2)/2)

Onde, g é a aceleração da gravidade (-10m/s²), y(t) é a posição final, 
y(0) é a posição inicial, v(0) é a velocidade inicial e t é o instante de tempo.

Resposta
'''
velocidade_inicial = float(input('Digite a velocidade inicial: ')) 
posicao_inicial = float(input('Digite a posição inicial: ')) 
tempo = float(input('Digite o instante de tempo: ')) 
g = -10 # aceleração gravitacional

posicao = posicao_inicial + (velocidade_inicial*tempo) + (g/2*tempo**2)

print(posicao, "m")

'''
Resposta Sugerida

Você pode estar se perguntando: "QUÊ?!" Mas calma, a dificuldade desse exercício não é diferente 
dos outros de conversão de temperatura ou cálculo da área de um círculo por exemplo. 
É apenas uma fórmula da Cinemática (parte da Física que estuda o movimento dos corpos) 
utilizada para calcular a posição de um projétil balístico.
 
Aqui consideramos a velocidade e posição inicial, a aceleração da gravidade e o 
instante de tempo que se quer analizar. 
Para isso pedimos 3 dessas 4 informações uma vez que a aceleração da gravidade 
é uma constante física que aproximamos aqui para -10 m/s².
'''
y0 = float(input("Digite a posição inicial: "))
v0 = float(input("Digite a velocidade inicial: "))
t = float(input("Digite um instante no tempo: "))
g = -10

y = y0 + v0*t + 0.5*g*t**2

print("A posição no instante t =", t, "é", y)

'''
Mas por que eu estou fazendo um código pra isso?" 
Bom, primeiro para exercitar a programação. 
Mas um fato interessante é que a computação passou por um importante período de 
desenvolvimento durante a Segunda Guerra Mundial e um dos primeiros computadores 
eletromecânicos criados tinha como objetivo justamente realizar cálculos balísticos. 
O nome dele é ENIAC (Electronic Numerical Integrator and Computer), 
pesava 30 toneladas e ocupava 180m² além de não ter poder maior que uma calculadora 
de bolso hoje em dia.
>>>>>>> 52e15950b8515da1dec547f128fcb8e14736a285
>>>>>>> Stashed changes
'''