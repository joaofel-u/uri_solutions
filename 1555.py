# -*- coding: utf-8 -*-

testes = int(input())

while testes > 0:
    testes -= 1

    x, y = input().split()
    x = int(x)
    y = int(y)

    rafael = 9*x*x + y*y
    beto = 2*x*x + 25*y*y
    carlos = -100*x + y*y*y

    if beto > carlos and beto > rafael:
        print("Beto ganhou")
    elif carlos > rafael:
        print("Carlos ganhou")
    else:
        print("Rafael ganhou")
