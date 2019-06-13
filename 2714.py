# -*- coding: utf-8 -*-

n = int(input())

while n > 0:
    n -= 1

    entrada = input()

    accepted = True

    if entrada[0:2] != "RA" or len(entrada) != 20:
        accepted = False

    index = 0
    if accepted:
        for i in range(2, 20):
            if entrada[i] != '0':
                index = i
                break

    if accepted and i != 0:
        print(entrada[i:20])
    else:
        print("INVALID DATA")
