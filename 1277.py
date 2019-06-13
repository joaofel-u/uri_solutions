# -*- coding: utf-8 -*-

casos_teste = int(input())

while (casos_teste > 0):

    n = int(input())

    estudantes = input().split()
    lista_presenca = input().split()

    fi = []

    for i in range(n):
        p = 0
        a = 0

        for j in lista_presenca[i]:
            if j == 'P':
                p += 1
            elif j == 'A':
                a += 1

        t = p+a
        if p/t < 0.75:
            fi.append(estudantes[i])


    print(" ".join(fi))

    casos_teste -= 1
