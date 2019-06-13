# -*- coding: utf-8 -*-

while True:
    n1, n2 = input().split()

    if n1 == n2 and n1 == '0': break

    if int(n2) < int(n1):
        aux = n2
        n2 = n1
        n1 = aux


    carries = 0
    carry = 0
    for i in range(1, len(n1)+1):
        aux = int(n1[-i]) + int(n2[-i]) + carry
        carry = int(aux/10)
        if carry > 0:
            carries += 1

    i = len(n1) + 1
    while carry > 0 and i <= len(n2):
        aux = int(n2[-i]) + carry
        carry = int(aux/10)
        if carry > 0:
            carries += 1
        i+=1


    if carries == 0:
        print("No carry operation.")
    elif carries == 1:
        print("1 carry operation.")
    else:
        print("%d carry operations." % carries)
