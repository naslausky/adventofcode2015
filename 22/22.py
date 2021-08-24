#Desafio do dia 22/12/2015
#a) Dada uma lista de magias, ver qual o mínimo da mana necessário para matar o boss.
#b) Idem porém sempre perdendo 1 de vida a cada começo de turno seu.
inimigo = {}
with open('input.txt') as file:
	linhas = file.read().splitlines()
	for linha in linhas:
		chave, valor = linha.split(': ')
		inimigo[chave] = int(valor)
	inimigo['Poison Turns'] = 0

movimentos = [
{'Cost': 53, 'Damage': 4, 'Heal': 0, 'Shield Turns': 0, 'Poison Turns': 0,'Regen Turns': 0},
{'Cost': 73, 'Damage': 2, 'Heal': 2, 'Shield Turns': 0, 'Poison Turns': 0,'Regen Turns': 0},
{'Cost': 113, 'Damage': 0, 'Heal': 0, 'Shield Turns': 6, 'Poison Turns': 0,'Regen Turns': 0},
{'Cost': 173, 'Damage': 0, 'Heal': 0, 'Shield Turns': 0, 'Poison Turns': 6,'Regen Turns': 0},
{'Cost': 229, 'Damage': 0, 'Heal': 0, 'Shield Turns': 0, 'Poison Turns': 0,'Regen Turns': 5},
]

def verificarTerminoBatalha(jogador, inimigo): #Método que verifica se o jogo acabou. Retorna um booleano para tal, e outro para indicar quem ganhou.
	if inimigo['Hit Points'] <= 0:
		return True, True #Acabou, inimigo morreu.
	if jogador['Hit Points'] <= 0:
		return True,False #Acabou, jogador morreu.
	return False, False #Não acabou.

def turnoDoInimigo(jogador, inimigo):
	#Verifica as condições especiais:
	verificarEfeitosAtuais(jogador,inimigo)

	acabou,jogadorVenceu = verificarTerminoBatalha(jogador, inimigo) #Verifica se ele morreu nesse veneno.
	if acabou: #O inimigo morreu envenenado.
		return acabou, jogadorVenceu

	#Ataque do inimigo:
	danoCausadoPeloInimigo = inimigo['Damage'] - jogador['Armor']
	danoCausadoPeloInimigo = max(danoCausadoPeloInimigo, 1) #Como o dano do meu input é maior que 7, nem precisaria dessa linha, eu acho.
	jogador['Hit Points'] -= danoCausadoPeloInimigo
	return verificarTerminoBatalha(jogador, inimigo)

def verificarEfeitosAtuais(jogador,inimigo): #Verifica, aplica, e reduz os contadores os efeitos atuais do jogador e do inimigo.
	if jogador['Shield Turns']>0: #Armadura.
		jogador['Armor'] = 7
		jogador['Shield Turns'] -= 1
	else:
		jogador['Armor'] = 0

	if jogador['Regen Turns'] > 0: #Regeneração de mana.
		jogador['Regen Turns'] -= 1
		jogador['Mana'] += 101

	if inimigo['Poison Turns'] > 0: #Veneno.
		inimigo['Hit Points'] -= 3
		inimigo['Poison Turns'] -= 1

minimoAteAgora = 100000
def batalhar(jogador, inimigo, manaGastaAteAgora, Parte2 = False): #Roda um turno do jogador, um turno do inimigo, e segue. Retorna se ganhou, e quanto de mana gastou até o final vitorioso mais econômico.
	global minimoAteAgora
	if manaGastaAteAgora > minimoAteAgora: # Se ele já gastou mais do que uma outra vitória gastou, já para por aqui.
		return False, -1

	if Parte2: #No modo Hard, antes de todo turno seu, você perde 1 de vida.
		jogador['Hit Points'] -= 1
		acabou, _ = verificarTerminoBatalha(jogador,inimigo)
		if acabou:
			return False, -1

	verificarEfeitosAtuais(jogador,inimigo) #Começa verificando os efeitos deles.

	estadosVitoriosos = [] #Lista de inteiros que representam as manas gastas que trouxeram a vitória.

	movimentosQuePodemSerExecutados = [movimento for movimento in movimentos if movimento['Cost'] <= jogador['Mana']] #Só pode executar os que ele tem mana suficiente.

	for movimento in movimentosQuePodemSerExecutados:
		jogadorNesteTurno = jogador.copy() #Pra não atrapalhar os outros movimentos.
		inimigoNesteTurno = inimigo.copy()

		manaDesteMovimento = movimento['Cost'] #Diminui a mana gasta neste movimento e incrementa a mana total gasta até aqui.
		manaTotalAteEsteTurno = manaGastaAteAgora + manaDesteMovimento

		jogadorNesteTurno['Mana'] -= manaDesteMovimento #Executou o movimento, gastou mana.

		if movimento['Damage'] > 0: #Magic Missile ou Life Drain.
			inimigoNesteTurno['Hit Points'] -= movimento['Damage'] 
			jogadorNesteTurno['Hit Points'] += movimento['Heal']

		elif movimento['Shield Turns']>0: #Shield.
			if jogadorNesteTurno['Shield Turns'] > 0: #Não pode usar essa magia enquanto o efeito ainda estiver ativo.
				continue
			else:
				jogadorNesteTurno['Shield Turns'] = movimento['Shield Turns']
				jogadorNesteTurno['Armor'] = 7

		elif movimento['Poison Turns'] > 0: #Poison.
			if inimigoNesteTurno['Poison Turns'] > 0:
				continue
			else:
				inimigoNesteTurno['Poison Turns'] = movimento['Poison Turns']

		else: #Regenação de mana.
			if jogadorNesteTurno['Regen Turns'] > 0:
				continue
			else:
				jogadorNesteTurno['Regen Turns'] = movimento['Regen Turns']

		acabou, jogadorVenceu = verificarTerminoBatalha(jogadorNesteTurno, inimigoNesteTurno) #Pode ter matado no hit no caso do Magic Missile ou do Life Drain.
		if acabou:
			if jogadorVenceu: #Venceu neste turno, neste movimento. Gastou só a mana deste movimento:
				estadosVitoriosos.append(manaTotalAteEsteTurno)

		else: #Segue o baile com o turno do inimigo:
			acabou, jogadorVenceu = turnoDoInimigo(jogadorNesteTurno, inimigoNesteTurno)
			if acabou: #O inimigo pode ter morrido envenenado, ou matado o jogador no ataque
				if jogadorVenceu: #Venceu sem nem precisar turnos seguintes.
					estadosVitoriosos.append(manaTotalAteEsteTurno)
			else: #Segue a batalha:
				ganhou, manaVitoriosa = batalhar(jogadorNesteTurno, inimigoNesteTurno, manaTotalAteEsteTurno, Parte2)
				if ganhou:
					estadosVitoriosos.append(manaVitoriosa)
	if estadosVitoriosos:
		menorManaVitoriosaDesteTurno = min(estadosVitoriosos)
		minimoAteAgora = min(minimoAteAgora, menorManaVitoriosaDesteTurno)
		return True, menorManaVitoriosaDesteTurno #É possível ganhar daqui pra frente, com no mínimo tal mana.
	else:
		return False, -1

jogadorInicial = {'Hit Points' : 50, 'Mana': 500, 'Armor': 0, 'Regen Turns':0, 'Shield Turns': 0}
print('Mínimo de mana necessário para ganhar:', batalhar(jogadorInicial, inimigo, 0)[1])
minimoAteAgora = 100000 #Reinicia o valor mínimo que serve como limitador de recursão.
print('Mínimo de mana necessário para ganhar no modo hard:', batalhar(jogadorInicial, inimigo, 0, True)[1])
