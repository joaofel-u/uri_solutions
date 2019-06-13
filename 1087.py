#-*- coding: utf-8 -*-

while True:
    x1, y1, x2, y2 = input().split()
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)

    if x1 == 0 and x2 == 0 and y1 == 0 and y2 == 0:
        break

    if x1 == x2 and y1 == y2:  # já se encontra na casa alvo
        print(0)
    elif x1 == x2 or y1 == y2:  # esta numa posicao ortogonal ao alvo
        print(1)
    elif abs(x2-x1) == abs(y2-y1):  # esta numa diagonal
        print(1)
    else:
        print(2)
