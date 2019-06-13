# -*- coding: utf-8 -*-

# classe auxiliar para facilitar a comparacao de itens distintos
class Item:
    # construtor parametrizado
    def __init__(self, num, resto):
        self.num_ = num
        self.resto_ = resto

    # sobrecarga do operador '>'
    def __gt__(self, item2):
        if self.resto_ == item2.resto_:
            if self.par():
                if item2.par():
                    return self.num_ > item2.num_
                else:
                    return True
            else:
                if item2.par():
                    return False
                else:
                    return self.num_ < item2.num_
        else:
            return self.resto_ > item2.resto_

    # sobrecarga do operador '<'
    def __lt__(self, item2):
        if self.resto_ == item2.resto_:
            if self.par():
                if item2.par():
                    return self.num_ < item2.num_
                else:
                    return False
            else:
                if item2.par():
                    return True
                else:
                    return self.num_ > item2.num_
        else:
            return self.resto_ < item2.resto_


    # funcao auxiliar que retorna se o item dado eh par ou nao
    def par(self):
        return self.num_ % 2 == 0

# fim da classe Item

# fluxo principal do programa
while True:
    n, m = input().split()
    n = int(n)
    m = int(m)

    # condicao de parada
    if n == 0 and m == 0:
        break

    aux = []

    # leitura da entrada / insercao dos numeros e seus restos em um array auxiliar
    for i in range(n):
        num = int(input())
        resto = num % m

        if num < 0 and resto > 0:
            resto -= m

        aux.append(Item(num, resto))
    # end for

    aux.sort()

    # saida
    print(str(n) + " " + str(m))
    for item in aux:
        print(item.num_)

# end while

print("0 0")
