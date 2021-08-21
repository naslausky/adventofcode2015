#Desafio do dia 21/12/2015
#a)Receber uma lista de itens e calcular o menor custo que você ganha a batalha com o inimigo.
#b)Calcular o maior custo que ainda sim você perde a batalha contra o inimigo.

inimigo = {}
with open('input.txt') as file:
	linhas = file.read().splitlines()
	for linha in linhas:
		chave, valor = linha.split(': ')
		inimigo[chave] = int(valor)
armas = [
{'Cost': 8, 'Damage': 4, 'Armor': 0},
{'Cost': 10, 'Damage': 5, 'Armor': 0},
{'Cost': 25, 'Damage': 6, 'Armor': 0},
{'Cost': 40, 'Damage': 7, 'Armor': 0},
{'Cost': 74, 'Damage': 8, 'Armor': 0},
]

armaduras = [
{'Cost': 0, 'Damage': 0, 'Armor': 0}, #Uma armadura vazia pois é opcional
{'Cost': 13, 'Damage': 0, 'Armor': 1},
{'Cost': 31, 'Damage': 0, 'Armor': 2},
{'Cost': 53, 'Damage': 0, 'Armor': 3},
{'Cost': 75, 'Damage': 0, 'Armor': 4},
{'Cost': 102, 'Damage': 0, 'Armor': 5},
]

aneis = [
{'Cost': 25, 'Damage': 1, 'Armor': 0},
{'Cost': 50, 'Damage': 2, 'Armor': 0},
{'Cost': 100, 'Damage': 3, 'Armor': 0},
{'Cost': 20, 'Damage': 0, 'Armor': 1},
{'Cost': 40, 'Damage': 0, 'Armor': 2},
{'Cost': 80, 'Damage': 0, 'Armor': 3},]

def batalhar(jogador): #Método que retorna True se o jogador ganhou
	vezDoJogador = True
	danoCausadoPeloInimigo = inimigo['Damage'] - jogador['Armor']
	danoCausadoPeloInimigo = max(danoCausadoPeloInimigo, 1)
	danoCausadoPeloJogador = jogador['Damage'] - inimigo['Armor']
	danoCausadoPeloJogador = max(danoCausadoPeloJogador, 1)
	vidaInimigo = inimigo['Hit Points']
	vidaJogador = 100 
	while (vidaJogador > 0) and (vidaInimigo > 0):
		if vezDoJogador:
			vidaInimigo -= danoCausadoPeloJogador
		else:
			vidaJogador -= danoCausadoPeloInimigo
		vezDoJogador = not vezDoJogador	
	return vidaJogador > 0

menorPreco = 400
maiorPreco = 0
def batalharEVerificarPreco(jogador):
	global menorPreco
	global maiorPreco
	precoGasto = jogador['Cost']
	if batalhar(jogador): #Salva o menor se ele ganhou.
		menorPreco = min(precoGasto, menorPreco)
	else: #Salva o maior se ele perdeu.
		maiorPreco = max(precoGasto, maiorPreco)

#Escolhendo os equipamentos:
for arma in armas: #Obrigatório comprar uma arma, já foi escolhida.
	for armadura in armaduras:
		#Seus atributos já começam com o da arma, e vao incrementando com o resto:
		jogadorComArma = arma.copy()
		for chave in armadura:
			jogadorComArma[chave] += armadura[chave] #incrementa os status do jogador.
		jogadorComArmaEArmadura = jogadorComArma
		for numeroDeAneis in range(3): #Anel é opcional, no máximo dois.
			if numeroDeAneis == 2:
				for anel1 in aneis:
					for anel2 in aneis:
						if anel1 != anel2:
							jogadorComTudo = jogadorComArmaEArmadura.copy()
							for chave in anel1:
								jogadorComTudo[chave] += (anel1[chave] + anel2[chave])
							batalharEVerificarPreco(jogadorComTudo)
			elif numeroDeAneis == 1:
				for anel1 in aneis:
					jogadorComTudo = jogadorComArmaEArmadura.copy()
					for chave in anel1:
						jogadorComTudo[chave] += anel1[chave]
					batalharEVerificarPreco(jogadorComTudo)
			else:	
				batalharEVerificarPreco(jogadorComArmaEArmadura)

print('Menor preço gasto que ainda resulta em vitória:', menorPreco)
print('Maior preço gasto que ainda resulta em derrota:', maiorPreco) 
