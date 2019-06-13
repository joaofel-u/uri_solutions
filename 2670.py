# -*- coding: utf-8 -*-

entrada = [0] * 3
for i in range(3):
    entrada[i] = int(input())


caso1 = 2*entrada[1] + 4*entrada[2]
caso2 = 2*entrada[0] + 2*entrada[2]
caso3 = 4*entrada[0] + 2*entrada[1]

print(min(caso1, caso2, caso3))
