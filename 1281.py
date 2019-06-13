# -*- coding: utf-8 -*-

n = int(input())

for i in range(n):
    prod_disp = int(input())
    produtos = []

    for j in range(prod_disp):
        produtos.append(input().split())

    prod_adq = int(input())
    valor = 0
    for j in range(prod_adq):
        prod, qtd = input().split()
        qtd = int(qtd)

        for produto in produtos:
            if produto[0] == prod:
                valor += float(produto[1]) * qtd


    print("R$ %.2f" % valor)
