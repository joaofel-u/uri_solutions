# -*- coding:utf-8 -*-

while True:
    try:
        entrada = input()

        pilha = 0
        correct = True
        for c in entrada:
            if c == '(':
                pilha += 1
            elif c == ')':
                pilha -= 1

            if pilha < 0:
                correct = False
                break

        if correct and pilha == 0:
            print("correct")
        else:
            print("incorrect")

    except EOFError:
        break
