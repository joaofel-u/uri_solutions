# -*- coding: utf-8 -*-

n = int(input())
pares = []
impares = []

for i in range(n):
    entrada = int(input())

    if entrada % 2 == 0:
        pares.append(entrada)
    else:
        impares.append(entrada)

pares.sort()
impares.sort(reverse=True)

saida = pares + impares

for num in saida:
    print(num)
