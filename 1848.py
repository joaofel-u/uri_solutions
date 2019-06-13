# -*- coding: utf-8 -*-

i = 0
num = 0

while i < 3:
    entrada = input()

    if entrada == 'caw caw':
        print(num)
        num = 0
        i += 1
    else:
        if entrada[0] == '*':
            num += 4
        if entrada[1] == '*':
            num += 2
        if entrada[2] == '*':
            num += 1
