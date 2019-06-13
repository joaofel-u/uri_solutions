# -*- coding: utf-8 -*-

INF = 10000

adj = [[-1] * 64 for i in range(64)]
grau = [0] * 64

map = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
dx = [-2, -2, -1, 1, 2, 2, 1, -1]
dy = [-1, 1, 2, 2, 1, -1, -2, -2]


# funcao que valida uma posicao no tabuleiro
def valid(x, y):
    if x < 0 or y < 0 or x > 7 or y > 7: return False
    return True


# BUSCA EM LARGURA
def bfs(s):
    c = [False] * 64
    d = [INF] * 64

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
# construcao do grafo
for i in range(8):
    for j in range(8):
        for k in range(8):
            x = i+dx[k]
            y = j+dy[k]
            index = i*8 + j
            indexAux = x*8 + y
            if valid(x, y) and not (indexAux in adj[index]):
                adj[index][grau[index]] = indexAux
                grau[index] += 1


while True:
    try:
        s, t = input().split()

        origem = map[s[0]]*8 + int(s[1])-1
        destino = map[t[0]]*8 + int(t[1])-1

        # calculo
        d = bfs(origem)

        print("To get from " + s + " to " + t + " takes " + str(d[destino]) + " knight moves.")

    except EOFError:
        break
