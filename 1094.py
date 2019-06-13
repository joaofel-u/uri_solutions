# -*- coding: utf-8 -*-

testes = int(input())
total_cobaias = 0
total_ratos = 0
total_coelhos = 0
total_sapos = 0

for i in range(testes):
    qtd, cobaia = input().split()
    qtd = int(qtd)

    total_cobaias += qtd
    if cobaia == 'C':
        total_coelhos += qtd
    elif cobaia == 'R':
        total_ratos += qtd
    else:
        total_sapos += qtd

pct_coelhos = total_coelhos / total_cobaias * 100
pct_ratos = total_ratos / total_cobaias * 100
pct_sapos = total_sapos / total_cobaias * 100

print("Total: " + str(total_cobaias) + " cobaias")
print("Total de coelhos: " + str(total_coelhos))
print("Total de ratos: " + str(total_ratos))
print("Total de sapos: " + str(total_sapos))
print("Percentual de coelhos: %.2f" % pct_coelhos + " %")
print("Percentual de ratos: %.2f" % pct_ratos + " %")
print("Percentual de sapos: %.2f" % pct_sapos + " %")
