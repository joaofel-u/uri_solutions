# -*- coding: utf:8 -*-

import math

while True:
    try:
        a, b, c = input().split()
        a = float(a)
        b = float(b)
        c = float(c)
        pi = 3.141592654

        c1 = math.tan(a * pi / 180) * b
        h = c + c1

        qtd = 5*h

        print("%.2f" % qtd)

    except EOFError:
        break
