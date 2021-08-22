#Desafio do dia 22/12/2015
#a) Dada uma lista de magias, ver qual o mínimo da mana necessário para matar o boss
#b) 
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

def batalhar(jogador, inimigo, manaGastaAteAgora): #Roda um turno do jogador, um turno do inimigo, e segue. Retorna se ganhou, e quanto de mana gastou no mínimo
	print('Iniciando Turno')
	print(jogador,'\n',inimigo, manaGastaAteAgora)
	input()
	menorManaGastaQueGanha = 100000
	consegueGanhar = False
	movimentosQuePodemSerExecutados = [movimento for movimento in movimentos if movimento['Cost'] < jogador['Mana']]
	for movimento in movimentosQuePodemSerExecutados:

		jogadorNesteTurno = jogador.copy() #Para não atrapalhar as outras recursões
		inimigoNesteTurno = inimigo.copy()

		def verificarTerminoBatalha():
			if inimigoNesteTurno['Hit Points'] <= 0:
				return True, True #Acabou, inimigoMorreu
			if jogadorNesteTurno['Hit Points'] <= 0:
				return True,False #Acabou, jogador morreu
			return False, False #Não acabou

		def turnoDoInimigo():
			if inimigoNesteTurno['Poison Turns'] > 0:
				inimigoNesteTurno['Hit Points'] -= 3
				inimigoNesteTurno['Poison Turns'] -= 1
			ganhou,jogadorVenceu = verificarTerminoBatalha()
			if ganhou: #Morreu envenenado
				return ganhou, jogadorVenceu
			danoCausadoPeloInimigo = inimigoNesteTurno['Damage'] - jogadorNesteTurno['Armor']
			danoCausadoPeloInimigo = max(danoCausadoPeloInimigo, 1) #O dano mínimo é 1. O dano do meu input é maior que 7, nem precisa.
			jogadorNesteTurno['Hit Points'] -= danoCausadoPeloInimigo
			return verificarTerminoBatalha()
		
		##Verifica os efeitos atuais do jogador
		if jogadorNesteTurno['Shield Turns']>0:
			jogadorNesteTurno['Armor'] = 7
			jogadorNesteTurno['Shield Turns'] -= 1
		else:
			jogadorNesteTurno['Armor'] = 0

		if jogadorNesteTurno['Regen Turns'] > 0:
			jogadorNesteTurno['Regen Turns'] -= 1
			jogadorNesteTurno['Mana'] += 101

		if movimento['Damage'] > 0: #MM ou Life Drain
			inimigoNesteTurno['Hit Points'] -= movimento['Damage'] 
			jogadorNesteTurno['Hit Points'] += movimento['Heal']
			manaTotal = manaGastaAteAgora + movimento['Cost']
			jogadorNesteTurno['Mana'] -= movimento['Cost']
			acabou, inimigoMorreu = verificarTerminoBatalha()
			if acabou:
				if inimigoMorreu:
					consegueGanhar = True
					menorManaGastaQueGanha = min(manaTotal, menorManaGastaQueGanha)
			else: #Turno do inimigo:
				acabou,jogadorVivo = turnoDoInimigo()
				if acabou: #Ou morreu envenenado, ou o hit do boss matou o jogador.
					if jogadorVivo:
						consegueGanhar = True
						menorManaGastaQueGanha = min(manaTotal, menorManaGastaQueGanha)
				else: #segue a batalha
					ganhou,menorManaDaquiPraFrente = batalhar(jogadorNesteTurno, inimigoNesteTurno, manaTotal)
					if ganhou:
						consegueGanhar = True
						menorManaGastaQueGanha = min(menorManaDaquiPraFrente, menorManaGastaQueGanha)
					

		elif movimento['Shield Turns']>0:
			if jogadorNesteTurno['Shield Turns'] > 0:
				continue
			else:
				jogadorNesteTurno['Shield Turns'] = movimento['Shield Turns']
				manaTotal = manaGastaAteAgora + movimento['Cost']
				jogadorNesteTurno['Mana'] -= movimento['Cost']
				acabou,jogadorVivo = turnoDoInimigo()
				if acabou: #Ou morreu envenenado, ou o hit do boss matou o jogador.
					if jogadorVivo:
						consegueGanhar = True
						menorManaGastaQueGanha = min(manaTotal, menorManaGastaQueGanha)
				else:
					ganhou, menorManaDaquiPraFrente = batalhar(jogadorNesteTurno, inimigoNesteTurno, manaTotal)
					if ganhou:
						consegueGanhar = True
						menorManaGastaQueGanha = min(menorManaDaquiPraFrente, menorManaGastaQueGanha)

		elif movimento['Poison Turns'] > 0:
			if inimigoNesteTurno['Poison Turns'] > 0:
				continue
			else:
				inimigoNesteTurno['Poison Turns'] = movimento['Poison Turns']
				manaTotal = manaGastaAteAgora + movimento['Cost']
				jogadorNesteTurno['Mana'] -= movimento['Cost']
				acabou,jogadorVivo = turnoDoInimigo()
				if acabou: #Ou morreu envenenado, ou o hit do boss matou o jogador.
					if jogadorVivo:
						consegueGanhar = True
						menorManaGastaQueGanha = min(manaTotal, menorManaGastaQueGanha)
				else:
					ganhou, menorManaDaquiPraFrente = batalhar(jogadorNesteTurno, inimigoNesteTurno, manaTotal)
					if ganhou:
						consegueGanhar = True
						menorManaGastaQueGanha = min(menorManaDaquiPraFrente, menorManaGastaQueGanha)
		else: #Regen
			if jogadorNesteTurno['Regen Turns'] > 0:
				continue
			else:
				jogadorNesteTurno['Regen Turns'] = movimento['Regen Turns']
				manaTotal = manaGastaAteAgora + movimento['Cost']
				jogadorNesteTurno['Mana'] -= movimento['Cost']
				acabou,jogadorVivo = turnoDoInimigo()
				if acabou: #Ou morreu envenenado, ou o hit do boss matou o jogador.
					if jogadorVivo:
						consegueGanhar = True
						menorManaGastaQueGanha = min(manaTotal, menorManaGastaQueGanha)
				else:
					ganhou, menorManaDaquiPraFrente = batalhar(jogadorNesteTurno, inimigoNesteTurno, manaTotal)
					if ganhou:
						consegueGanhar = True
						menorManaGastaQueGanha = min(menorManaDaquiPraFrente, menorManaGastaQueGanha)
	return consegueGanhar, menorManaGastaQueGanha

jogadorInicial = {'Hit Points' : 50, 'Mana': 500, 'Armor': 0, 'Regen Turns':0, 'Shield Turns': 0}
print(batalhar(jogadorInicial, inimigo, 0)) #1235 too high

