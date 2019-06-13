# -*- coding: utf-8 -*-

n = int(input())
tempo_total = 0
prox_desligamento = 0

for i in range(n):
    tempo_atual = int(input())

    if tempo_atual < prox_desligamento:
        tempo_total += 10 - prox_desligamento + tempo_atual
    else:
        tempo_total += 10

    prox_desligamento = tempo_atual + 10

# end for

print(tempo_total)
