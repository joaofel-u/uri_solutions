# -*- coding: utf-8 -*-

while True:
    entrada = input()

    if entrada == '*':
        break

    letra = entrada[0].upper()
    entrada = entrada.split()
    tautogram = True

    for palavra in entrada:
        if palavra[0].upper() != letra:
            tautogram = False

    if tautogram:
        print("Y")
    else:
        print("N")
