# -*- coding: utf-8 -*-


frase = input().split()

for i in range(len(frase)):
    palavra = frase[i]
    if len(palavra) >= 4:
        if palavra[0:1] == palavra[2:3]:
            palavra = palavra[2:]
            frase[i] = palavra

print(" ".join(frase))
