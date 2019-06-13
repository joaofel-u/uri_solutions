# -*- coding: utf-8 -*-

while True:
    n_gps, n_pilotos = input().split()
    n_gps = int(n_gps)
    n_pilotos = int(n_pilotos)

    # condicao de parada
    if n_gps == 0 and n_pilotos == 0:
        break

    pilotos = [0] * n_pilotos
    classificacoes = []

    # leitura dos resultados de cada corrida
    for i in range(n_gps):
        classificacoes.append(input().split())

    # leitura dos sistemas de pontuacao
    n_sistemas = int(input())

    for i in range(n_sistemas):
        sistema = input().split()
        k = int(sistema[0])

        # atribuicao dos pontos de cada piloto
        for i in range(n_pilotos):
            pontos = 0

            for j in range(n_gps):
                colocacao = int(classificacoes[j][i])
                if colocacao <= k:
                    pontos += int(sistema[colocacao])

            # armazenamento dos pontos do piloto i
            pilotos[i] = [i, pontos]

        # end for

        pilotos.sort(key=lambda a: a[1], reverse=True)

        # avaliacao dos campeoes
        campeoes = []
        pontuacao_campeao = pilotos[0][1]
        for piloto in pilotos:
            if piloto[1] == pontuacao_campeao:
                campeoes.append(str(piloto[0]+1))
            else:
                break
        # end for

        print(" ".join(campeoes))

    #end for

#end while
