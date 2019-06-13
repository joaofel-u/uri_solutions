# -*- coding: utf-8 -*-

# funcao auxiliar que retorna se um produto cabe em uma caixa de alguma maneira
def cabe(dim_prod, dim_caixa):
    dim_prod.sort()
    dim_caixa.sort()

    if dim_prod[0] > dim_caixa[0] or dim_prod[1] > dim_caixa[1] or dim_prod[2] > dim_caixa[2]:
        return False
    return True

# fluxo principal do programa
while True:
    # leitura do pedido e num de caixas no estoque
    num_caixas, caixas_estoque = input().split()
    num_caixas = int(num_caixas)
    caixas_estoque = int(caixas_estoque)

    # condicao de parada
    if num_caixas == 0:
        break;

    # dimensoes produto
    x_prod, y_prod, z_prod = input().split()
    x_prod = int(x_prod)
    y_prod = int(y_prod)
    z_prod = int(z_prod)
    vol_prod = x_prod * y_prod * z_prod

    # leitura das caixas disponiveis no estoque
    caixas = []
    for i in range(caixas_estoque):
        caixa = input().split()
        x = int(caixa[0])
        y = int(caixa[1])
        z = int(caixa[2])
        caixa = [x, y, z]
        caixa.sort()

        # verifica se o produto cabe na caixa dada
        if cabe([x_prod, y_prod, z_prod], caixa):
            encaixe = x*y*z - vol_prod
            caixas.append([encaixe, str(caixa)])


    caixas.sort()
    length_caixas = len(caixas)
    possivel = False
    if not(length_caixas < num_caixas):
        melhor_encaixe = caixas[0]
        qtd = 0
        for i in range(length_caixas):
            if caixas[i] == melhor_encaixe:
                qtd += 1
            else:
                melhor_encaixe = caixas[i]
                qtd = 1

            if qtd == num_caixas:
                possivel = True
                break
        #end for

    # avalia a melhor possibilidade de caixas disponiveis para armazenamento
    if not(possivel):
        print("impossible")
    else:
        print(melhor_encaixe[0])
