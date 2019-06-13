# -*- coding: utf-8 -*-

# pegar submissao ja realizada no uri e modificar para corrigir
# -*- coding: utf-8 -*-

# Classe que define um nodo da arvore
class Node:
    def __init__(self, valor):
        self.value = valor
        self.esquerda = None
        self.direita = None

    def insert(self, valor):
        if int(valor) >= int(self.value):
            if self.direita is None:
                self.direita = Node(valor)
            else:
                self.direita.insert(valor)
        else:
            if self.esquerda is None:
                self.esquerda = Node(valor)
            else:
                self.esquerda.insert(valor)

    def pre_order(self, list):
        list.append(str(self.value))
        if self.esquerda is not None:
            self.esquerda.pre_order(list)
        if self.direita is not None:
            self.direita.pre_order(list)

    def in_order(self, list):
        if self.esquerda is not None:
            self.esquerda.in_order(list)
        list.append(str(self.value))
        if self.direita is not None:
            self.direita.in_order(list)

    def post_order(self, list):
        if self.esquerda is not None:
            self.esquerda.post_order(list)
        if self.direita is not None:
            self.direita.post_order(list)
        list.append(str(self.value))

# Fim da classe que define um nodo

# Classe que define uma arvore
class Arvore:
    def __init__(self):
        self.raiz = None

    def insert(self, value):
        if self.raiz is not None:
            self.raiz.insert(value)
        else:
            self.raiz = Node(value)

    def pre_order(self, list):
        if self.raiz is not None:
            self.raiz.pre_order(list)

    def in_order(self, list):
        if self.raiz is not None:
            return self.raiz.in_order(list)

    def post_order(self, list):
        if self.raiz is not None:
            return self.raiz.post_order(list)

# Fim da classe que define uma Arvore

# Codigo principal
casos = int(input())

for i in range(casos):
    print("Case " + str(i + 1) + ":")

    # Recebe os dados e faz as inicializacoes
    entradas = int(input())
    dados = input().split()
    arvore = Arvore()

    for d in dados:
        arvore.insert(int(d))

    # Gera a saida
    pre_order = []
    in_order = []
    post_order = []

    arvore.pre_order(pre_order)
    arvore.in_order(in_order)
    arvore.post_order(post_order)

    print("Pre.: " + " ".join(pre_order))
    print("In..: " + " ".join(in_order))
    print("Post: " + " ".join(post_order))
    print("")
