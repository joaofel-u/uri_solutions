# -*- coding: utf-8 -*-

while True:
    try:
        alfabeto = input()
        qtd_letras = int(input())
        letras = input().split()
        saida = []

        for i in range(qtd_letras):
            saida.append(alfabeto[int(letras[i]) - 1])

        print(''.join(saida))

    except EOFError:
        break
