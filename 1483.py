# -*- coding:utf-8 -*-

import math

while True:
    aposta, numero_apostado, numero_sorteado = input().split()

    # condicao de parada
    if aposta == '0' and numero_apostado == '0' and numero_sorteado == '0':
        break

    # padronizacao da entrada
    aposta = float(aposta)
    numero_apostado = ("0000" + numero_apostado)[-4:]
    numero_sorteado = ("0000" + numero_sorteado)[-4:]


    if numero_apostado == numero_sorteado:
        premio = aposta * 3000
    elif numero_apostado[-3:] == numero_sorteado[-3:]:
        premio = aposta * 500
    elif numero_apostado[-2:] == numero_sorteado[-2:]:
        premio = aposta * 50
    else:
        numero_apostado = int(numero_apostado[-2:])
        numero_sorteado = int(numero_sorteado[-2:])
        if numero_apostado == 0:
            numero_apostado = 100
        elif numero_sorteado == 0:
            numero_sorteado = 100


        if math.ceil(numero_apostado/4) == math.ceil(numero_sorteado/4):
            premio = aposta * 16
        else:
            premio = 0
    #end if

    print("%.2f" % premio)
