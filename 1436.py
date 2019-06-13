# -*- coding: utf-8 -*-

import math

testes = int(input())
cont = 1

while cont <= testes:
    idades = input().split()

    n = int(idades[0])
    idades = idades[1:]

    if n % 2 == 0:
        index = int(n/2);
    else:
        index = math.floor(n/2)

    val = int(idades[index])

    print("Case " + str(cont) + ": " + str(val))

    cont += 1
