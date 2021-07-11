#Desafio do dia 09/12/2015
#a) Calcular a menor distância que passa por todos os nós de um grafo com pesos.
#b) Idem para a maior distância.

with open('input.txt') as file:
	linhas = file.read().splitlines()
dicionarioDistancias = {} # Dicionário que relaciona as distancias da forma {A: {B:40,C:30}, B:{A:40...}..}
for linha in linhas: #Popula o dicionário
	distancia = int(linha.split(' = ')[1])
	cidades = linha.split(' = ')[0].split(' to ')
	if (cidades[0] in dicionarioDistancias):
		dicionarioDistancias[cidades[0]][cidades[1]] = distancia
	else:
		dicionarioDistancias[cidades[0]] = {cidades[1]:distancia}
	if (cidades[1] in dicionarioDistancias):
		dicionarioDistancias[cidades[1]][cidades[0]] = distancia
	else:
		dicionarioDistancias[cidades[1]] = {cidades[0]:distancia}
menoresRotas = {}
maioresRotas = {} #Dicionários que relacionam cada cidade com a maior/menor distancia
for cidadeInicial, distancias in dicionarioDistancias.items():
#Parte 1: Calculando a menor rota para esta cidade inicial:
	rotaAteAgora = [cidadeInicial]
	distanciaAteAgora = 0
	while len(rotaAteAgora) != len(dicionarioDistancias):
		distanciaMinima = min(valor for _,valor in dicionarioDistancias[rotaAteAgora[-1]].items() if _ not in rotaAteAgora)
		for cidade,distancia in dicionarioDistancias[rotaAteAgora[-1]].items():
			if cidade not in rotaAteAgora:
				if distanciaMinima == distancia:
					rotaAteAgora.append(cidade)
					distanciaAteAgora+=distancia
	menoresRotas[cidadeInicial] = distanciaAteAgora
#Parte 2: Calculando a maior rota para esta cidade inicial:
	rotaAteAgora = [cidadeInicial]
	distanciaAteAgora = 0
	while len(rotaAteAgora) != len(dicionarioDistancias):
		distanciaMaxima = max(valor for _,valor in dicionarioDistancias[rotaAteAgora[-1]].items() if _ not in rotaAteAgora)
		for cidade,distancia in dicionarioDistancias[rotaAteAgora[-1]].items():
			if cidade not in rotaAteAgora:
				if distanciaMaxima== distancia:
					rotaAteAgora.append(cidade)
					distanciaAteAgora+=distancia
	maioresRotas[cidadeInicial] = distanciaAteAgora
menorDistancia = min([valor for _,valor in menoresRotas.items()])
print('Menor distância percorrida que passa por todas as cidades:', menorDistancia)
maiorDistancia = max([valor for _,valor in maioresRotas.items()])
print('Maior distância percorrida que passa por todas as cidades:', maiorDistancia)
