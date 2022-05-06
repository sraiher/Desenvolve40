class Buscador:

    def busca_Sequencial(self, lista, x):
        for i in range(len(lista)):
            if lista[i] == x:
                return i
        return -1


    def busca_binaria(self, lista, x):
        primeiro = 0
        ultimo = len(lista) - 1

        while primeiro <= ultimo:
            meio = (primeiro + ultimo) // 2
            if lista[meio] == x:
                return meio
            else:
                if x < lista[meio]:
                    ultimo = meio-1
                else:
                    primeiro = meio+1
        return -1 #o elemento não está na lista

lista = [-110, 0, 20, 30, 50, 100, 3000, 5000]

b = Buscador()
b.busca_binaria(lista, 100)
print(b.busca_binaria(lista, 100))

