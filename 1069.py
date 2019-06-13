# -*- coding: utf-8 -*-

import sys
casos = int(input())

for i in range(casos):
    entrada = sys.stdin.readline()
    aux = []
    diamantes = 0
    opens = 0

    for c in entrada:
        if c == '<' or c == '>':
            aux.append(c)

    for i in range(len(aux)):
        if aux[i] == '<':
            opens += 1

        if aux[i] == '>' and opens > 0:
            opens -= 1
            diamantes += 1

    print(str(diamantes))
