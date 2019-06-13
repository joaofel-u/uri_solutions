# -*- coding: utf-8 -*-

def mdc(x, y):
    mod = x % y
    if mod == 0:
        return y
    else:
        return mdc(y, mod)

# fluxo principal
n = int(input())

for i in range(n):
    entrada = input().split()

    l1 = entrada[:3]
    op = entrada[3]
    l2 = entrada[4:]

    n1 = int(l1[0])
    n2 = int(l2[0])
    d1 = int(l1[-1])
    d2 = int(l2[-1])

    if op == '+':
        nr = n1*d2 + n2*d1
        dr = d1*d2
    elif op == '-':
        nr = n1*d2 - n2*d1
        dr = d1*d2
    elif op == '*':
        nr = n1*n2
        dr = d1*d2
    else:
        nr = n1*d2
        dr = n2*d1

    # simplificacao
    if nr >= dr:
        divisor = mdc(nr, dr)
    else:
        divisor = mdc(dr, nr)

    new_nr = int(nr/abs(divisor))
    new_dr = int(dr/abs(divisor))


    print(str(nr)+"/"+str(dr) + " = " + str(new_nr)+"/"+str(new_dr))
