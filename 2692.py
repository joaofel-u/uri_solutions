# -*- coding: utf-8 -*-

n, m = input().split()
n = int(n)
m = int(m)

dic = dict()

for i in range(n):
    k, v = input().split()
    dic[k] = v
    dic[v] = k
    

for i in range(m):
    entrada = input()

    saida = ""
    for c in entrada:
        saida += dic.get(c, c)

    print(saida)
