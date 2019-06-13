# -*- coding: utf-8 -*-

import math

testes = int(input())

while testes > 0:
    testes -= 1

    x, y = input().split()
    x = int(x)
    y = int(y)

    solution = int(math.ceil(x / y))

    if solution < 2:
        solution = 2

    print(solution)
