# -*- coding: utf-8 -*-

while True:
    n = int(input())

    if n == 0:
        break

    respostas = ['A', 'B', 'C', 'D', 'E']

    for i in range(n):
        entrada = input().split()

        valida = False
        resposta = -1
        for i in range(5):
            value = int(entrada[i])
            if value <= 127:
                if valida == False:
                    resposta = i
                    valida = True
                else:
                    valida = False
                    break
        # fim da avaliacao dos retangulos

        if valida:
            print(respostas[resposta])
        else:
            print('*')
