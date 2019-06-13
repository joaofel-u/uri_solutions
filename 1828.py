# -*- coding: utf-8 -*-

casos_teste = int(input())

for i in range(casos_teste):
    sheldon, raj = input().split()

    if sheldon == raj:
        print("Caso #%d: De novo!" % (i+1))
    else:
        if sheldon == 'tesoura' and raj == 'papel':
            print("Caso #%d: Bazinga!" % (i+1))
        elif sheldon == 'papel' and raj == 'pedra':
            print("Caso #%d: Bazinga!" % (i+1))
        elif sheldon == 'pedra' and raj == 'lagarto':
            print("Caso #%d: Bazinga!" % (i+1))
        elif sheldon == 'lagarto' and raj == 'Spock':
            print("Caso #%d: Bazinga!" % (i+1))
        elif sheldon == 'Spock' and raj == 'tesoura':
            print("Caso #%d: Bazinga!" % (i+1))
        elif sheldon == 'tesoura' and raj == 'lagarto':
            print("Caso #%d: Bazinga!" % (i+1))
        elif sheldon == 'lagarto' and raj == 'papel':
            print("Caso #%d: Bazinga!" % (i+1))
        elif sheldon == 'papel' and raj == 'Spock':
            print("Caso #%d: Bazinga!" % (i+1))
        elif sheldon == 'Spock' and raj == 'pedra':
            print("Caso #%d: Bazinga!" % (i+1))
        elif sheldon == 'pedra' and raj == 'tesoura':
            print("Caso #%d: Bazinga!" % (i+1))
        else:
            print("Caso #%d: Raj trapaceou!" % (i+1))
