# -*- coding: utf-8 -*-

# entrada
dia_inicio = input().split()
dia_inicio = int(dia_inicio[1])

hora_inicio = input().split()

dia_fim = input().split()
dia_fim = int(dia_fim[1])

hora_fim = input().split()

for i in range(3):
    hora_inicio[i] = int(hora_inicio[2*i])
    hora_fim[i] = int(hora_fim[2*i])

# calculo duracao
dias = dia_fim - dia_inicio

#calculo de horas
if hora_fim[0] < hora_inicio[0]:
    dias -= 1
    horas = 24 - hora_inicio[0] + hora_fim[0]
else:
    horas = hora_fim[0] - hora_inicio[0]

# calculo de minutos
if hora_fim[1] < hora_inicio[1]:
    horas -= 1
    minutos = 60 - hora_inicio[1] + hora_fim[1]
else:
    minutos = hora_fim[1] - hora_inicio[1]

# calculo de segundos
if hora_fim[2] < hora_inicio[2]:
    minutos -= 1
    segundos = 60 - hora_inicio[2] + hora_fim[2]
else:
    segundos = hora_fim[2] - hora_inicio[2]

# saida
print("%d dia(s)" % (dias))
print("%d hora(s)" % (horas))
print("%d minuto(s)" % (minutos))
print("%d segundo(s)" % (segundos))
