# -*- coding: utf-8 -*-

casos_teste = int(input())

while(casos_teste > 0):

    w1 = input()
    w2 = input()
    wt = input()

    possivel = False
    marked = False
    for i in range(len(wt)):
        if wt[i] == '_':
            if not marked:
                p1 = w1[i]
                p2 = w2[i]
                marked = True
            else:
                if p1 == w2[i] or p2 == w1[i]:
                    possivel = True

                break

    if possivel: print("Y")
    else: print("N")
    casos_teste -= 1
