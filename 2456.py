# -*- coding: utf-8 -*-

entrada = input().split()


if int(entrada[1]) >= int(entrada[0]):
    ordenacao = 'C'
elif int(entrada[1]) <= int(entrada[0]):
    ordenacao = 'D'

valida = True
anterior = int(entrada[1])
for i in range(2, len(entrada)):
    if int(entrada[i]) > anterior and ordenacao == 'D':
        valida = False
        break
    elif int(entrada[i]) < anterior and ordenacao == 'C':
        valida = False
        break

    anterior = int(entrada[i])

# saida
if valida:
    print(ordenacao)
else:
    print("N")
