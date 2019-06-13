# -*- coding: utf-8 -*-

while True:

    try:
        entrada_vogais = input()
        list = ['0'] * len(entrada_vogais)
        for i in range(len(entrada_vogais)):
            list[i] = entrada_vogais[i]

        vogais = set(list)

        count = 0
        frase = input().split()
        for palavra in frase:
            for letra in palavra:
                if letra in vogais:
                    count += 1


        print(count)

    except EOFError:
        break
