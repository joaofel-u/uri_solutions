# -*- coding: utf-8 -*-

import math

testes = int(input())

while testes > 0:
    testes -= 1

    n = int(input())

    result = int(math.pow(2, n) - 1)

    print(result)
