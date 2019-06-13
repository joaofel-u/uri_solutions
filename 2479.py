# -*- coding: utf-8 -*-

n = int(input())

criancas = [""] * n
comportadas = 0
nao_comportadas = 0

for i in range(n):
    crianca = input().split()

    if crianca[0] == '+':
        comportadas += 1
    else:
        nao_comportadas += 1

    criancas[i] = crianca[1]

criancas.sort()

print("\n".join(criancas))
print("Se comportaram: " + str(comportadas) + " | Nao se comportaram: " + str(nao_comportadas))
