# -*- coding: utf-8 -*-

div = 1000000007

fac = [1] * 1010
fac[1] = 1
for i in range(2, 1010):
    fac[i] = (fac[i-1] * i) % div

letras = {}
for i in range(26):
    letras[chr(65+i)] = 0

while True:
    try:
        entrada = input()

        for k in letras.keys():
            letras[k] = 0

        # leitura da entrada
        for c in entrada:
            letras[c] += 1

        # contagem das repeticoes
        den = 1
        for k in letras.values():
            if k > 1:
                den = (den*fac[k]) % div

        solution = int( (fac[len(entrada)] * pow(den, div - 2, div)) % div )

        print(solution)

    except EOFError:
        break
