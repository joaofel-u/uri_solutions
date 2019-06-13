# -*- coding:utf-8 -*-

# funcao auxiliar que compara se um nome eh menor que outro (ordem lexicografica)
def str_compare(str1, str2):
    len_str1 = len(str1)
    len_str2 = len(str2)
    menor = min(len_str1, len_str2)

    for i in range(menor):
        if str1[i] < str2[i]:
            return True
        elif str1[i] > str2[i]:
            return False

    return len_str1 < len_str2


# classe que define um tipo de entrada do quadro de medalhas
class Pais:
    # construtor de um pais do quadro
    def __init__(self, nome, ouros, pratas, bronzes):
        self.nome_ = nome
        self.ouros_ = ouros
        self.pratas_ = pratas
        self.bronzes_ = bronzes

    # define a forma de string de um pais
    def __str__(self):
        return self.nome_ + " " + str(self.ouros_) + " " + str(self.pratas_) + " " + str(self.bronzes_)

    # define a igualdade de dois paises no quadro de medalhas
    def __eq__(self, pais2):
        return self.nome_ == pais2.nome_

    # define se um pais esta atras de outro no quadro
    def __lt__(self, pais2):
        if self.ouros_ == pais2.ouros_:
            if self.pratas_ == pais2.pratas_:
                if self.bronzes_ == pais2.bronzes_:
                    return not(str_compare(self.nome_, pais2.nome_))
                else:
                    return self.bronzes_ < pais2.bronzes_
            else:
                return self.pratas_ < pais2.pratas_
        else:
            return self.ouros_ < pais2.ouros_

    # define se um pais esta a frente de outro no quadro
    def __gt__(self, pais2):
        if self.ouros_ == pais2.ouros_:
            if self.pratas_ == pais2.pratas_:
                if self.bronzes_ == pais2.bronzes_:
                    return str_compare(self.nome_, pais2.nome_)
                else:
                    return self.bronzes_ > pais2.bronzes_
            else:
                return self.pratas_ > pais2.pratas_
        else:
            return self.ouros_ > pais2.ouros_

# fim da classe Pais

# fluxo principal do programa
participantes = int(input())
paises = []

# faz a leitura dos paises participantes
for i in range(participantes):
    nome, ouros, pratas, bronzes = input().split()
    paises.append(Pais(nome, int(ouros), int(pratas), int(bronzes)))

paises.sort(reverse=True)

for pais in paises:
    print(pais)
