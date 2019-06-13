# -*- coding: utf-8 -*-

while True:
    n = int(input())

    # condicao de parada
    if n == 0:
        break

    # entrada
    jogadores = input().split()

    baralho = []
    for i in range(4):
        baralho.extend(input().split())

    # cfg inicial da partida
    vencedor = False
    ativos = jogadores.copy()
    cartas_restantes = 52

    # inicio do turno
    while not(vencedor):
        inicio = 52 - cartas_restantes
        fim = inicio + len(ativos)
        if fim > 52:
            break

        turno = baralho[inicio:fim]

        menor = 15
        indices = []
        for i in range(len(turno)):
            if int(turno[i]) < menor:
                menor = int(turno[i])
                indices = [i]
            elif int(turno[i]) == menor:
                indices.append(i)

        # identifica empate e declara os ativos vencedores
        if len(indices) == len(ativos):
            vencedor = True
            break

        # remove os jogadores eliminados
        indices.sort(reverse=True)
        for i in indices:
            ativos.pop(i)

        # atualiza os jogadores que participam do proximo turno
        if len(ativos) == 1:
            vencedor = True
            break
        elif len(ativos) == 0:
            ativos = jogadores.copy()

        cartas_restantes -= len(turno)


    # resultado
    print(" ".join(ativos) + " ")
