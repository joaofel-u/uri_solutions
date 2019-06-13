# -*- coding: utf-8 -*-

while True:
    entrada = input()

    if entrada == '*':
        break

    entrada = entrada.split("/")[1:-1]
    compassos = [['W',float(1)], ['H',float(1/2)], ['Q',float(1/4)], ['E',float(1/8)], ['S',float(1/16)], ['T',float(1/32)], ['X',float(1/64)]]

    # processamento
    correto = 0

    for entry in entrada:
        soma = float(0)
        last = 'W'
        value = 1
        for c in entry:
            if c == last:
                soma += value
            else:
                for char in compassos:
                    if char[0] == c:
                        soma += char[1]
                        value = char[1]
                        last = char[0]

        if soma == 1:
            correto += 1


    # end for

    print(correto)
