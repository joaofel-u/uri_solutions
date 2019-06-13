# -*- coding: utf-8 -*-

n, k = input().split()
n = int(n)
k = int(k)

entrada = input().split()

qtd_rotulos = [0] * k

for i in range(n):
    index = int(entrada[i]) - 1;
    qtd_rotulos[index] += 1


print(min(qtd_rotulos))
