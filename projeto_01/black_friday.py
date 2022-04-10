import json
import os.path
import sys
import pprint


def obter_dados():
    
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados


def listar_categorias(dados):
    
    categ_list = []
    for categoria in dados:
        if (categoria['categoria']) not in categ_list:
            categ_list.append(categoria['categoria'])
    categ_list.sort()
    return categ_list
    
dados = obter_dados() 


def listar_por_categoria(dados, categoria):
                            
    list_categorias = []
    for produto in dados:
        if produto['categoria'] == categoria:
            list_categorias.append({'id': produto['id'], 'preco': produto['preco']})
    return list_categorias
dados = obter_dados()


def produto_mais_caro(dados, categoria):

    list_preco = []
    prod_caro = {}
    for produto in dados:
        if produto['categoria'] == categoria:
            list_preco.append(float(produto['preco']))
    mais_caro = max(list_preco)
    preco = str(mais_caro)
    for produto in dados:
        if produto['preco'] == preco:
            prod_caro.update( {'id': produto['id'], 'preco': preco } )
            
    return prod_caro
dados = obter_dados()


def produto_mais_barato(dados, categoria):

    list_preco = []
    prod_barato = {}
    for produto in dados:
        if produto['categoria'] == categoria:
            list_preco.append(float(produto['preco']))
    mais_barato = min(list_preco)
    preco = str(mais_barato)
    for produto in dados:
        if produto['preco'] == preco:
            prod_barato.update( {'id': produto['id'], 'preco': mais_barato } )
    return prod_barato
dados = obter_dados()


def top_10_caros(dados):
    preco_top_caros = []
    maior = 0
 
    for produto in dados:
        produto['preco'] = float(produto['preco'])
        if produto ['preco'] > maior:
            maior = produto['preco']
            preco_top_caros.append({produto['preco'], produto ['id'], produto['categoria']})
            preco_top_caros.sort(reverse=False)
    return preco_top_caros
dados = obter_dados()

  
def top_10_baratos(dados):  
    preco_top_baratos = []
    menor = 1000 
 
    for produto in dados:
        produto['preco'] = float(produto['preco'])
        if produto ['preco'] < menor:
            menor = produto['preco']
            preco_top_baratos.append({produto['preco'], produto ['id'], produto['categoria']})
            preco_top_baratos.sort(reverse=False)         
    
    return preco_top_baratos
top_10_baratos(dados)
dados = obter_dados()


import pprint



def menu(dados):

    print('')
    print ('----------Menu de Opções----------')
    print('')
    print('(1) Listar categorias')
    print('(2) Listar produtos de uma categoria')
    print('(3) Produto mais caro por categoria')
    print('(4) Produto mais barato por categoria')
    print('(5) Top 10 mais caros')
    print('(6) Top 10 mais baratos')
    print('(0) SAIR')
   
    opcao = 999

    while opcao != 0:
        opcao = int(input('Escolha uma das opções: '))  
        
        if opcao == 1:
            listar_categorias(dados).insert(0,dados)
            pprint.pprint(listar_categorias(dados))
                
        elif opcao == 2:
            categoria = input('Digite a categoria: ')
            if categoria not in (listar_categorias(dados)):
                print('Categoria inválida')
            else:
                pprint.pprint(listar_por_categoria(dados, categoria))

        elif opcao == 3:
            categoria = input('Digite a categoria: ')
            produto_mais_caro(dados, categoria)
            if categoria not in (listar_categorias(dados)):
                print('Categoria inválida')
            else:
                print(f'O produto mais caro da categoria {categoria} é {produto_mais_caro(dados, categoria)}.')

        elif opcao == 4:
            categoria = input('Digite a categoria: ')
            print(produto_mais_barato(dados, categoria))
            if categoria not in (listar_categorias(dados)):
                print('Categoria inválida')
            else:
                print(f'O produto mais barato da categoria {categoria} é {produto_mais_barato(dados, categoria)}.')

        elif opcao == 5:
            top_10_caros(dados)
            print('Os 10 produtos mais caros são:')
            pprint.pprint(top_10_caros(dados))
            
        elif opcao == 6:
            top_10_baratos(dados)
            print('Os 10 produtos mais baratos são:')
            pprint.pprint(top_10_baratos(dados))
        
        elif opcao == 0:
            print('FIM!')

        else:
            opcao != 1 or opcao != 2 or opcao != 3 or opcao != 4 or opcao != 5 or opcao != 6 or opcao != 0
            print('Opção Inválida!')
            
            
            

# Programa Principal - não modificar!
d = obter_dados()
menu(d)
