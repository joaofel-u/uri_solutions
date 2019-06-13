# -*- coding: utf-8 -*-

tempo_viagem = int(input())
vel_media = int(input())

consumo_medio = 12  # Km/L

distancia_percorrida = tempo_viagem * vel_media

print("%.3f" % (distancia_percorrida / consumo_medio))
