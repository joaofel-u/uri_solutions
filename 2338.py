# -*- coding: utf-8 *-

casos_teste = int(input())

for i in range(casos_teste):
    entrada = input().split(".......")
    saida = ""

    for word in entrada:
        letters = word.split("...")
        for letter in letters:
            symbols = letter.split(".")
            cod = ""

            for symbol in symbols:
                if symbol == "=":
                    cod += "."
                else:
                    cod += "-"

            # codigos de cada letra
            if cod == ".-":
                saida += 'a'
            elif cod == "-...":
                saida += 'b'
            elif cod == "-.-.":
                saida += 'c'
            elif cod == "-..":
                saida += 'd'
            elif cod == ".":
                saida += 'e'
            elif cod == "..-.":
                saida += 'f'
            elif cod == "--.":
                saida += 'g'
            elif cod == "....":
                saida += 'h'
            elif cod == "..":
                saida += 'i'
            elif cod == ".---":
                saida += 'j'
            elif cod == "-.-":
                saida += 'k'
            elif cod == ".-..":
                saida += 'l'
            elif cod == "--":
                saida += 'm'
            elif cod == "-.":
                saida += 'n'
            elif cod == "---":
                saida += 'o'
            elif cod == ".--.":
                saida += 'p'
            elif cod == "--.-":
                saida += 'q'
            elif cod == ".-.":
                saida += 'r'
            elif cod == "...":
                saida += 's'
            elif cod == "-":
                saida += 't'
            elif cod == "..-":
                saida += 'u'
            elif cod == "...-":
                saida += 'v'
            elif cod == ".--":
                saida += 'w'
            elif cod == "-..-":
                saida += 'x'
            elif cod == "-.--":
                saida += 'y'
            elif cod == "--..":
                saida += 'z'

        saida += " "

    saida = saida[:-1]
    print(saida)
