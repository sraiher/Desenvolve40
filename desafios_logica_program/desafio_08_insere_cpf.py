'''
Desafio 08 -Faça um programa que fique pedindo uma resposta do usuário, entre 1, 2 e 3. 
Se o usuário digitar 1, o programa deve cadastrar um novo usuário e guardar esse cadastro 
num dicionário cuja chave será o CPF da pessoa. Quando o usuário digitar 2, o programa deve imprimir os usuários cadastrados; e se o usuário digitar 3, o programa deve fechar.

Exemplo do dicionário:

‘987.654.321-00’: {‘nome’: Maria, ‘idade’: 20, ‘email’ :             maria@mail.com}

Resposta
'''
print('Para cadastro novo: (1) ') 
print('Para imprimir usuários cadastrados: (2)') 
print('Para fechar o programa digite: (3)')

opcao = int(input('Digite a sua opcao: '))

if opcao != 1 and opcao != 2 and opcao != 3: print('Opção inválida, tente novamente!') print(int(input('Digite a sua opcao: ')))

if opcao == 1: cpf = print(input('Digite o seu CPF:')) 
nome = print(input('Digite o seu nome:' )) 
idade = print(input('Digite a sua idade:' )) 
e_mail = print(input('Digite o seu e_mail:' )) 
dic = {'CPF': cpf, 'Nome' : nome, 'idade': idade, 'email': e_mail } print(dic)

if opcao == 2: print('Cadastro será impresso')

else: print('Encerrar o programa')


# Resposta Sugerida

def cadastraPessoa(nome, idade, email): #função do exercício 5
    return { "nome": nome, "idade": idade, "email": email }

usuarios = {}
entrada = 0 # Começa a variável num valor que entra no loop
while entrada != 3:
    print()
    print("As opções são:")
    print("1 - Cadastrar novo usuário")
    print("2 - Mostrar usuários cadastrados")
    print("3 - Fechar programa")
    entrada = int(input("Escolha uma opção: "))
    print()
    if entrada == 1:
        print("Cadastro de usuário")
        CPF = input("CPF: ")
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        email = input("Email: ")
        usuarios[CPF] = cadastraPessoa(nome, idade, email) 
        print("Usuário Cadastrado")

    elif entrada == 2:
        if len(usuarios) == 0:
            print("Não há usuários cadastrados")
        else:
            print("Lista de usuários cadastrados")
            for i in usuarios.items():
                print(i)