# -*- coding: utf-8 -*-

n = int(input())

while n > 0:
    n -= 1

    dieta = input()
    dieta = list(dieta)
    cafe = input()
    almoco = input()

    cheater = False

    for c in cafe:
        if c in dieta:
            dieta.remove(c)
        else:
            cheater = True
            break

    if not cheater:
        for c in almoco:
            if c in dieta:
                dieta.remove(c)
            else:
                cheater = True
                break

    dieta.sort()

    if cheater:
        print("CHEATER")
    else:
        print("".join(dieta))
