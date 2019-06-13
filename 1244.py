# -*- coding: utf-8 -*-

n = int(input())

for i in range(n):
    entrada = input().split()

    entrada.sort(key=lambda a: len(a), reverse=True)

    print(" ".join(entrada))
