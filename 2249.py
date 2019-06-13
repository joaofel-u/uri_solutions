# -*- coding: utf-8 -*-

INF = 10000
LIM = 1000

def sort_func(x):
    x = x.split(". ")
    return x[1] + " " + x[0]


# BUSCA EM LARGURA
def bfs(s, adj, grau):
    c = [False] * LIM
    d = [INF] * LIM

    c[s] = True
    d[s] = 0

    fila = []
    fila.append(s)

    while len(fila) > 0:
        u = fila.pop(0)

        for i in range(grau[u]):
            v = adj[u][i]
            if not c[v]:
                c[v] = True
                d[v] = d[u] + 1
                fila.append(v)

    return d


# FLUXO PRINCIPAL
teste = 0

while True:
    a = int(input())
    if a == 0: break

    teste += 1
    print("Teste %d" %teste)

    map = dict()
    adj = [[0] * LIM for i in range(LIM)]
    grau = [0] * LIM

    map["P. Erdos"] = 0

    # construcao do grafo
    for i in range(a):
        entrada = input()
        entrada = entrada[:-1].split(", ")

        for autor in entrada:
            if not(autor in map):
                map[autor] = len(map)

        for j in range(len(entrada)):
            autor = entrada[j]
            index = map[autor]

            for k in range(j, len(entrada)):
                autor2 = entrada[k]
                index2 = map[autor2]

                adj[index][grau[index]] = index2
                adj[index2][grau[index2]] = index

                grau[index] += 1
                grau[index2] += 1
    # END FOR

    # calculo
    d = bfs(0, adj, grau)

    lista = list(map)
    lista.sort(key=sort_func)

    for autor in lista:
        if autor != "P. Erdos":
            val = str(d[map[autor]])
            if int(val) == INF: val = "infinito"
            print(autor + ": " + str(val))

    print()
