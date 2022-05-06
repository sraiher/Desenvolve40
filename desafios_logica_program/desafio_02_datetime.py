<<<<<<< Updated upstream
'''
Desafio 2 - Faça um programa que informe a data e a hora para o usuário. 
Para isso use a função datetime.now() do módulo datetime.

Resposta:
'''
from datetime import datetime
now = datetime.now()
print(now.day) 
print(float(now.hour))

'''
Resposta Sugerida
Aqui temos um passo interessante na nossa caminhada: o uso de bibliotecas de funções. 
Calma que eu explico.

Você já está utilizando funções há um bom tempo: 
print(), input(), int(), flot() e quaisquer outras que o seu professor já te apresentou em aula. 
Essas funções vem "de graça" no Python e nós podemos usá-las sem problema algum.

Contudo, existem o que chamamos de "Bibliotecas de Funções" que são pacotes de funções que 
podemos importar para utilizar no nosso código. 
Algumas também já vem junto com o Python de tão famosas que são mas ainda assim precisamos 
importar no nosso código, como é o caso da biblioteca Datetime.

Essa biblioteca traz uma série de funções relacioandas a data e tempo num geral. 
Nós usaremos, preste atenção: a função now() do subconjunto datetime da biblioteca datetime.

Nem todas as biblitecas possuem sub conjuntos e podemos utilizar a função 
fazendo algo como "nomeDaBiblioteca.funcao()" porém aqui nós precisamos considerar o 
subconjunto que pra nos ajudar (ironia), tem o mesmo nome da biblioteca. Veja:
'''
from datetime import datetime # Incluímos a biblioteca datetime
agora = datetime.now() # Chamamos a função now() da biblioteca datetime

# Separamos cada pedaço que precisamos
ano = agora.year
mes = agora.month
dia = agora.day
hora = agora.hour
minuto = agora.minute
segundo = agora.second

# Imprimimos o resultado 
# (Obs: o sep="" quer dizer que o print não vai inserir um espaço entre cada uma das saídas)
print(dia, "/", mes, "/", ano, " ", hora, ":", minuto, ":", segundo, sep="")

# Outra forma
agora = datetime.now()
formato = "%d/%m/%Y %H:%M:%S" # Definimos um formato 
agora_formatado = datetime.strftime(agora,formato) 	# Usamos a função strftime(), 
													# que formata automaticamente o texto
print(agora_formatado)

'''
Aqui apresentamos duas formas de apresentar o resultado certo. 
A primeira faz uso do print comum com um parâmetro sep de "separador" (no original separator) 
igual a "" (string vazia) que retira os espaços entre os parâmetros passados 
(sim, escondemos esse segredinho de você até agora, perdão).

A segunda faz uso da própria função de conversão da biblioteca do formato Datetime 
(sim, é um formato diferente!) para o formato String que estamos acostumados. 
Essa abordagem eu acredito ser mais elegante.
=======
<<<<<<< HEAD
'''
Desafio 2 - Faça um programa que informe a data e a hora para o usuário. 
Para isso use a função datetime.now() do módulo datetime.

Resposta:
'''
from datetime import datetime
now = datetime.now()
print(now.day) 
print(float(now.hour))

'''
Resposta Sugerida
Aqui temos um passo interessante na nossa caminhada: o uso de bibliotecas de funções. 
Calma que eu explico.

Você já está utilizando funções há um bom tempo: 
print(), input(), int(), flot() e quaisquer outras que o seu professor já te apresentou em aula. 
Essas funções vem "de graça" no Python e nós podemos usá-las sem problema algum.

Contudo, existem o que chamamos de "Bibliotecas de Funções" que são pacotes de funções que 
podemos importar para utilizar no nosso código. 
Algumas também já vem junto com o Python de tão famosas que são mas ainda assim precisamos 
importar no nosso código, como é o caso da biblioteca Datetime.

Essa biblioteca traz uma série de funções relacioandas a data e tempo num geral. 
Nós usaremos, preste atenção: a função now() do subconjunto datetime da biblioteca datetime.

Nem todas as biblitecas possuem sub conjuntos e podemos utilizar a função 
fazendo algo como "nomeDaBiblioteca.funcao()" porém aqui nós precisamos considerar o 
subconjunto que pra nos ajudar (ironia), tem o mesmo nome da biblioteca. Veja:
'''
from datetime import datetime # Incluímos a biblioteca datetime
agora = datetime.now() # Chamamos a função now() da biblioteca datetime

# Separamos cada pedaço que precisamos
ano = agora.year
mes = agora.month
dia = agora.day
hora = agora.hour
minuto = agora.minute
segundo = agora.second

# Imprimimos o resultado 
# (Obs: o sep="" quer dizer que o print não vai inserir um espaço entre cada uma das saídas)
print(dia, "/", mes, "/", ano, " ", hora, ":", minuto, ":", segundo, sep="")

# Outra forma
agora = datetime.now()
formato = "%d/%m/%Y %H:%M:%S" # Definimos um formato 
agora_formatado = datetime.strftime(agora,formato) 	# Usamos a função strftime(), 
													# que formata automaticamente o texto
print(agora_formatado)

'''
Aqui apresentamos duas formas de apresentar o resultado certo. 
A primeira faz uso do print comum com um parâmetro sep de "separador" (no original separator) 
igual a "" (string vazia) que retira os espaços entre os parâmetros passados 
(sim, escondemos esse segredinho de você até agora, perdão).

A segunda faz uso da própria função de conversão da biblioteca do formato Datetime 
(sim, é um formato diferente!) para o formato String que estamos acostumados. 
Essa abordagem eu acredito ser mais elegante.
=======
'''
Desafio 2 - Faça um programa que informe a data e a hora para o usuário. 
Para isso use a função datetime.now() do módulo datetime.

Resposta:
'''
from datetime import datetime
now = datetime.now()
print(now.day) 
print(float(now.hour))

'''
Resposta Sugerida
Aqui temos um passo interessante na nossa caminhada: o uso de bibliotecas de funções. 
Calma que eu explico.

Você já está utilizando funções há um bom tempo: 
print(), input(), int(), flot() e quaisquer outras que o seu professor já te apresentou em aula. 
Essas funções vem "de graça" no Python e nós podemos usá-las sem problema algum.

Contudo, existem o que chamamos de "Bibliotecas de Funções" que são pacotes de funções que 
podemos importar para utilizar no nosso código. 
Algumas também já vem junto com o Python de tão famosas que são mas ainda assim precisamos 
importar no nosso código, como é o caso da biblioteca Datetime.

Essa biblioteca traz uma série de funções relacioandas a data e tempo num geral. 
Nós usaremos, preste atenção: a função now() do subconjunto datetime da biblioteca datetime.

Nem todas as biblitecas possuem sub conjuntos e podemos utilizar a função 
fazendo algo como "nomeDaBiblioteca.funcao()" porém aqui nós precisamos considerar o 
subconjunto que pra nos ajudar (ironia), tem o mesmo nome da biblioteca. Veja:
'''
from datetime import datetime # Incluímos a biblioteca datetime
agora = datetime.now() # Chamamos a função now() da biblioteca datetime

# Separamos cada pedaço que precisamos
ano = agora.year
mes = agora.month
dia = agora.day
hora = agora.hour
minuto = agora.minute
segundo = agora.second

# Imprimimos o resultado 
# (Obs: o sep="" quer dizer que o print não vai inserir um espaço entre cada uma das saídas)
print(dia, "/", mes, "/", ano, " ", hora, ":", minuto, ":", segundo, sep="")

# Outra forma
agora = datetime.now()
formato = "%d/%m/%Y %H:%M:%S" # Definimos um formato 
agora_formatado = datetime.strftime(agora,formato) 	# Usamos a função strftime(), 
													# que formata automaticamente o texto
print(agora_formatado)

'''
Aqui apresentamos duas formas de apresentar o resultado certo. 
A primeira faz uso do print comum com um parâmetro sep de "separador" (no original separator) 
igual a "" (string vazia) que retira os espaços entre os parâmetros passados 
(sim, escondemos esse segredinho de você até agora, perdão).

A segunda faz uso da própria função de conversão da biblioteca do formato Datetime 
(sim, é um formato diferente!) para o formato String que estamos acostumados. 
Essa abordagem eu acredito ser mais elegante.
>>>>>>> 52e15950b8515da1dec547f128fcb8e14736a285
>>>>>>> Stashed changes
'''