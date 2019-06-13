# -*- coding: utf-8 -*-

x = int(input())
y = int(input())


mat = [["" for i in range(x)] for j in range(y)]
visited = [[False for i in range(x)] for j in range(y)]

for i in range(y):
    entrada = input()

    for j in range(x):
        mat[i][j] = entrada[j]


treasure = False
i = 0
j = 0
direction = 'R'
while True:
    if i >= y or j >= x or i < 0 or j < 0 or visited[i][j]:
        break

    c = mat[i][j]
    visited[i][j] = True

    if c == '.':
        if direction == 'L':
            j-=1
        elif direction == 'R':
            j+=1
        elif direction == 'B':
            i+=1
        elif direction == 'U':
            i-=1

    elif c == '>':
        j+=1
        direction = 'R'
    elif c == '<':
        j-=1
        direction = 'L'
    elif c == 'v':
        i+=1
        direction = 'B'
    elif c == '^':
        i-=1
        direction = 'U'

    elif c == '*':
        treasure = True
        break

if treasure:
    print("*")
else:
    print("!")
