# -*- coding: utf-8 -*-

while True:
    n = int(input())

    # condicao de parada
    if n == 0:
        break

    # leitura de todas submissoes
    submissoes = []
    for i in range(n):
        submissoes.append(input().split())

    submissoes.sort(key=lambda s:s[0])
    print(submissoes)

    # processamento
    corretos = 0
    tempo = 0
    problema_atual = submissoes[0][0]
    tentativas_problemaAtual = 0
    problema_resolvido = False

    # estrutura de uma submissao armazenada
    # [0] - problema
    # [1] - tempo
    # [2] - estado da solucao
    for submissao in submissoes:
        # problema diferente do que vinha sendo avaliado
        if submissao[0] != problema_atual:
            problema_atual = submissao[0]
            tentativas_problemaAtual = 0
            problema_resolvido = False

        # avaliacao da submissao do problema atual
        if not(problema_resolvido):
            # submissao correta
            if submissao[2] == "correct":
                corretos += 1
                tempo += int(submissao[1]) + 20*tentativas_problemaAtual
                problema_resolvido = True

            # submissao incorreta
            else:
                tentativas_problemaAtual += 1

    # end for  (fim da avaliacao das submissoes)

    print(str(corretos) + " " + str(tempo))
