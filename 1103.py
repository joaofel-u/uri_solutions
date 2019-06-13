# -*- coding: utf-8 -*-

while True:
    h1, m1, h2, m2 = input().split()

    h1 = int(h1)
    m1 = int(m1)
    h2 = int(h2)
    m2 = int(m2)

    if h1 == 0 and m1 == 0 and h2 == 0 and m2 == 0:
        break

    minutos = 0
    hora_cheia = 0 # 0 = false, 1 = true

    if m2 > m1:
        hora_cheia = 1
        minutos += m2 - m1
    else:
        minutos += 60 - m1 + m2

    if h2 > h1 or h2 == h1 and m2 > m1:
        minutos += 60 * (h2 - h1)
    else:
        minutos += 60 * (24 - h1 + h2)

    if hora_cheia == 0: # fator de correcao pelo numero de minutos
        minutos -= 60

    print(str(minutos))
