#Desafio do dia 03/12/2015
#a) Receber uma lista de movimentos cartesianos, e contabilizar quantas casas são visitadas.
#b) Idem, porém para a lista de movimentos representando dois conjuntos de instruções separados.

coordenadaAtual = [0,0]
coordenadasVisitadas = {tuple(coordenadaAtual) : 1}
with open('input.txt') as file:
	movimentos = file.read()
for movimento in movimentos:
	if movimento == '^':
		coordenadaAtual[1]+=1
	elif movimento == '>':
		coordenadaAtual[0]+=1
	elif movimento == 'v':
		coordenadaAtual[1]-=1
	else :
		coordenadaAtual[0]-=1
	tupla = tuple(coordenadaAtual)
	if tupla in coordenadasVisitadas:
		coordenadasVisitadas[tupla] +=1
	else:
		coordenadasVisitadas[tupla] = 1
print('Número de casas visitadas:',len(coordenadasVisitadas))
#Parte 2:
coordenadasAtuais = [[0,0],[0,0]]
coordenadasVisitadas = {tuple(coordenadasAtuais[0]):2}
pilotoDaVez = 0
for movimento in movimentos:
	piloto = pilotoDaVez % 2
	if movimento == '^':
		coordenadasAtuais[piloto][1]+=1
	elif movimento == '>':
		coordenadasAtuais[piloto][0]+=1
	elif movimento == 'v':
		coordenadasAtuais[piloto][1]-=1
	else :
		coordenadasAtuais[piloto][0]-=1
	tupla = tuple(coordenadasAtuais[piloto])
	if tupla in coordenadasVisitadas:
		coordenadasVisitadas[tupla]+=1
	else:
		coordenadasVisitadas[tupla] = 1
	pilotoDaVez+=1
print('Número de casas visitadas com a ajuda do robô:', len(coordenadasVisitadas))
