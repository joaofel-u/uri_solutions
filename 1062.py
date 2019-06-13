# -*- coding: utf-8 -*-

while True:
    n = int(input())

    # condicao de parada
    if n == 0:
        break

    while True:
        entrada = input()

        # fim do caso de teste atual
        if entrada == "0":
            print()
            break
        else:
            entrada = entrada.split()


        #organizaco para avaliar saida
        estacao = []
        trem = [0] * n

        for i in range(n):
            trem[i] = i+1

        possivel = "Yes"

        i = 0
        while i < n:
            vagao = int(entrada[i])
            if len(trem) > 0:
                if vagao == trem[0]:
                    trem.pop(0)
                    i += 1
                elif len(estacao) > 0 and estacao[-1] == vagao:
                    estacao.pop()
                    i += 1
                else:
                    estacao.append(trem.pop(0))
            else:
                if estacao.pop() != vagao:
                    possivel = "No"
                    break
                i += 1

        # end while

        print(possivel)
