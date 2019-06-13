# -*- coding: utf-8 -*-

nome = input()
sal_base = float(input())
vendas = float(input())

total = sal_base + vendas * 0.15

print("TOTAL = R$ %.2f" % (total))
