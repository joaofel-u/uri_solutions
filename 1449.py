# -*- coding: utf-8 -*-

instancias = int(input())

for instancia in range(instancias):
    m, n = input().split()
    m = int(m)
    n = int(n)

    # cria o dicionario
    entrada = []
    for i in range(m):
        dupla = [""] * 2
        dupla[0] = input()
        dupla[1] = input()
        entrada.append(dupla)


    dicionario = dict(entrada)


    # traduz a letra da musica
    for i in range(n):
        linha = input().split()

        traducao = []
        for palavra in linha:
            if palavra in dicionario:
                traducao.append(dicionario.get(palavra))
            else:
                traducao.append(palavra)

        print(" ".join(traducao))
    # end for

    print()
