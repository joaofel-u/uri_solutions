# -*- coding: utf-8 -*-

while True:
    hexa = False
    entrada = input()
    if len(entrada) > 2 and entrada[1] == 'x':
        hexa = True

    if hexa:
        out = int(entrada, 16)
    else:
        entrada = int(entrada)
        #condicao de parada
        if entrada < 0: break
        else:
            val = hex(entrada)
            s = val[2:].upper()
            out = val[:2] + s


    print(out)
