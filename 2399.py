# -*- coding: utf-8 -*-

celulas = int(input())
tabuleiro = [0] * celulas

for i in range(celulas):
    tabuleiro[i] = int(input())

for i in range(celulas):
    minas = 0

    if i != 0:
        if tabuleiro[i - 1] == 1:
            minas += 1

    if i != celulas - 1:
        if tabuleiro[i + 1] == 1:
            minas += 1

    if tabuleiro[i] == 1:
        minas += 1

    print(str(minas))
