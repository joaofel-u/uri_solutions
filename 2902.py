#-*- coding: utf-8 -*-

class Pilha:
	def __init__(self):
		self.tam_ = 0
		self.topo_ = -1

# end of class Pilha


while True:
	n, j = input().split()
	n = int(n)
	j = int(j)

	# condicao de parada
	if n == 0 and j == 0:
		break

	# inicializacao
	pilha_compra = input().split()

	jogadores = [None] * j
	for i in range(j):
		jogadores[i] = Pilha()

	# inicio do jogo
	jogador_atual = 0
	monte_descarte = []
	pilha_atual = jogadores[0]

	# executa enquanto houver cartas na pilha de compra
	for carta in pilha_compra:
		value = int(carta)
		keep_playing = False

		# carta da vez encontrada na area de descarte
		if value in monte_descarte:
			monte_descarte.remove(value)
			pilha_atual.topo_ = value
			pilha_atual.tam_ += 2
			keep_playing = True

		# verifica se a carta da vez esta no topo de algum outro monte caso nao estivesse no descarte
		if not(keep_playing):
			for monte in jogadores:
				if monte.topo_ == value and pilha_atual != monte:
					pilha_atual.tam_ += monte.tam_ + 1
					pilha_atual.topo_ = value
					monte.tam_ = 0
					monte.topo_ = -1
					keep_playing = True
					# possibilidade de break???

		# carta da vez igual ao topo do seu proprio monte
		if not(keep_playing):
			if value == pilha_atual.topo_:
				pilha_atual.tam_ += 1
				keep_playing = True

		# fim da jogada
		if not(keep_playing):
			monte_descarte.append(value)

			jogador_atual += 1
			if jogador_atual == j:
				jogador_atual = 0

			pilha_atual = jogadores[jogador_atual]

	# end for

	vencedores = ""
	tam_monte_vencedor = -1

	# verifica quem venceu o jogo
	for i in range(j):
		tam = jogadores[i].tam_

		if tam > tam_monte_vencedor:
			vencedores = str(i+1)
			tam_monte_vencedor = tam

		elif tam == tam_monte_vencedor:
			vencedores += " " + str(i+1)
	# end for

	print(str(tam_monte_vencedor) + " " + vencedores)
