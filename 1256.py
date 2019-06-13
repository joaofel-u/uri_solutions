# -*- coding: utf-8 -*-

# Classe que define um nodo de encadeamento
class Node:
    def __init__(self, valor):
        self.value = valor
        self.next = None

    def chain(self, valor):
        if self.next is None:
            self.next = Node(valor)
        else:
            self.next.chain(valor)

    def get_chain(self):
        res = self.value + " -> "
        actual = self
        while actual.next is not None:
            actual = actual.next
            res += actual.value + " -> "
        return res

# Fim da classe que define um nodo de encadeamento

# Codigo principal
casos = int(input())

for i in range(casos):
    if i != 0:
        print("")

    enderecos, chaves = input().split()
    lista_chaves = input().split()

    tabela = [None] * int(enderecos)
    for c in lista_chaves:
        alvo = int(c) % int(enderecos)
        if tabela[alvo] is None:
            tabela[alvo] = Node(c)
        else:
            tabela[alvo].chain(c)

    for i in range(int(enderecos)):
        res = str(i) + " -> "
        if tabela[i] is not None:
            res += tabela[i].get_chain()

        res += "\\"
        print(res)
