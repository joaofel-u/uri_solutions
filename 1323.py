# -*- coding: utf-8 -*-

while True:
    n = int(input())

    # condicao de parada
    if n == 0:
        break

    # calculo
    quadrados = 0
    size = 0
    while size < n:
        aux = n - size
        quadrados += aux*aux

        size += 1
    # end while

    # saida
    print(quadrados)
