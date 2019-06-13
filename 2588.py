# -*- coding: utf-8 -*-

while True:

    try:
        entrada = input()

        conj = set()
        for c in entrada:
            if c in conj:
                conj.remove(c)
            else:
                conj.add(c)


        tam = len(entrada)
        if len(conj) == 0:
            if (tam/2) % 2 == 0:
                cont = 0
            else:
                cont = 1
        elif (tam % 2 == 1 and len(conj) == 1):
            cont = 0
        elif len(conj) != 0:
            cont = len(conj) - 1

        print(cont)

    except EOFError:
        break
