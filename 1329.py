# -*- coding: utf-8 -*-

while True:
    n = int(input())

    # condicao de parada
    if n == 0:
        break

    entrada = input().split()

    maria = 0
    joao = 0
    for i in range(n):
        if entrada[i] == '0':
            maria += 1
        else:
            joao += 1

    print("Mary won " + str(maria) + " times and John won " + str(joao) + " times")
