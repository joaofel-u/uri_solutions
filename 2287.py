# -*- coding: utf-8 -*-

# funcao

cont = 0
while True:
    cont += 1

    n = int(input())

    if n == 0:
        break

    senhas = []

    for i in range(n):
        entrada = input().split()
        associacoes = []

        for i in range(5):
            index = 2*i
            aux = [""] * 2
            aux[0] = entrada[index]
            aux[1] = entrada[index+1]
            associacoes.append(aux)

        letras = entrada[10:16]

        senha1 = []
        senha2 = []
        for i in range(6):
            if letras[i] == 'A':
                valor = 0
            elif letras[i] == 'B':
                valor = 1
            elif letras[i] == 'C':
                valor = 2
            elif letras[i] == 'D':
                valor = 3
            elif letras[i] == 'E':
                valor = 4

            senha1.append(associacoes[valor][0])
            senha2.append(associacoes[valor][1])
        # end for

        senhas.append([senha1, senha2])

    # verificacao de semelhanca de strings
    senha = []
    senha_encontrada = False
    while senha_encontrada == False:
        digito_atual = len(senha)
        possibilidades = []

        for conjunto_senha in senhas:
            possibilidade1 = conjunto_senha[0][digito_atual]
            possibilidade2 = conjunto_senha[1][digito_atual]

            if possibilidade1 == possibilidade2:
                senha.append(possibilidade1)
                break
            else:
                if len(possibilidades) == 0:
                    possibilidades.append(possibilidade1)
                    possibilidades.append(possibilidade2)
                else:
                    if possibilidades[0] == possibilidade1 or possibilidades[1] == possibilidade1:
                        if possibilidades[0] != possibilidade2 and possibilidades[1] != possibilidade2:
                            senha.append(possibilidade1)
                            break
                    else:
                        senha.append(possibilidade2)
                        break
        # end for

        if len(senha) == 6:
            senha_encontrada = True


    print("Teste %d" % cont)
    print(" ".join(senha) + " ")
    print()
