# -*- coding: utf-8 -*-

while True:
    try:
        n = int(input())
        tarefas = [None] * n

        for i in range(n):
            disp, t = input().split()
            tarefas[i] = [int(disp), int(t)]

        tarefas.sort(key=lambda a: a[0])

        tempo = 1
        for i in range(n):
            if (tarefas[i][0] <= tempo):
                tempo += tarefas[i][1]
            else:
                tempo = tarefas[i][0] + tarefas[i][1]

        print(tempo)

    except EOFError:
        break
