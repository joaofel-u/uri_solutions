# -*- coding: utf-8 -*-

grau = [0 for i in range(401)]
adj = [[0 for i in range(401)] for j in range(401)];

h, l = input().split()
h = int(h)
l = int(l)

for i in range(h):
    entrada = input().split()

    for j in range(l):
        
