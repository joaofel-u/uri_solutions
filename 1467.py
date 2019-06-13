# -*- coding: utf-8 -*-

while True:
    try:
        entrada = input().split()

        if entrada[0] == entrada[1] and entrada[1] == entrada[2]:
            print('*')
        elif entrada[0] != entrada[1] and entrada[0] != entrada[2]:
            print('A')
        elif entrada[0] != entrada[1]:
            print('B')
        else:
            print('C')

    except EOFError:
        break
