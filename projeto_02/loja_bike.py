
from datetime import datetime


data = (datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
print(data)

catalogo = [
    [ 'da5', 'azul', 'D'],
    [ 'db5', 'amarela', 'D'],
    [ 'dc5', 'vermelha', 'D'],
    [ 'dd5', 'prata', 'D'],
    [ 'de5', 'rosa', 'D'],
    [ 'df5', 'laranja', 'D']]  

        
class LojaBici:

    def __init__(self):
        self.catalogo = catalogo 

    def listar_bicicletas(self):
        print(f'As bicicletas cadastradas na loja são:')
        for bici in catalogo:
            print(bici)                  
            
    def pedido_bicicletas(self, modalidade):
        self.modalidade = modalidade
        quantas = int(input('Quantas bikes quer alugar?  '))
        contador = 0
        while contador < quantas:
            escolha = input('Digite o código da bicicleta escolhida:  ')
            for bicicleta in self.catalogo:
                if bicicleta[0] == escolha and bicicleta[2] == 'D':
                    bicicleta[2] = 'I'
                    contador +=1
                    print(f'Código: {bicicleta[0]}, Cor: {bicicleta[1]}, Disponibilidade: {bicicleta[2]}\n')                
                elif bicicleta[0] == escolha and bicicleta[2] == 'I':
                    print ('Bicicleta indisponível. Escolha outro modelo.\n')

    def devolucao(self):
      
        contador = 0
        quantas = int(input('Quantas bicicletas quer devolver?  '))
        while contador < quantas:
            retorno = input('Digite o código da bicicleta devolvida:  ')
            for bicicleta in self.catalogo:    
                if bicicleta[0] == retorno and bicicleta[2] == 'I':
                    bicicleta[2] = 'D'
                    contador +=1
            
        modalidade = input('Em qual modalidade foi locada, (H) para hora, (D) para dia, (S) para semana ')
        
        if modalidade == 'H' or modalidade == 'h':
            horas = int(input('Digite o número de horas:  '))
            
            if quantas >= 3:
                valor_loc = horas * 5 * quantas * 0.7
                print(f'O valor da fatura com desconto é R$  {valor_loc}')
            else: 
                valor_loc = horas * 5 * quantas
                print(f'O valor da fatura é R$  {valor_loc}')

        elif modalidade == 'D' or modalidade == 'd':
            dias = int(input('Digite o número de dias:  '))
            
            if quantas >= 3:
                valor_loc = dias * 25 * quantas * 0.7
                print(f'O valor da fatura com desconto é R$  {valor_loc}')
            else: 
                valor_loc = dias * 25 * quantas
                print(f'O valor da fatura é R$  {valor_loc}')

        elif modalidade == 'S' or modalidade == 's':
            semanas = int(input('Digite o número de semanas:  '))
            
            if quantas >= 3:
                valor_loc = semanas * 100 * quantas * 0.7
                print(f'O valor da fatura com desconto é R$  {valor_loc}')
            else: 
                valor_loc = semanas * 100 * quantas
                print(f'O valor da fatura é R$  {valor_loc}')
                                
    def __len__(self):
        return len(self.catalogo)

class Cliente:
    def __init__(self, nome, email, quantas):
        self.nome = nome
        self.email = email
        self.quantas = quantas

cliente1 = ('Sandra', 'sandra@email.com', 3)
cliente2 = ('Eliana', 'eliana@email.com', 2)
print(cliente1, cliente2)


loja1 = LojaBici()
loja1.listar_bicicletas()
loja1.pedido_bicicletas(catalogo)
loja1.devolucao()




