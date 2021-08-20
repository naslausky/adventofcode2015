#Desafio do dia 15/12/2015
#a)Receber uma lista de ingredientes onde cada um deles possui pontuações em características. 
#Calcular a melhor combinação de 100 ingredientes que retornam a melhor pontuação nas características.
#b) Idem porém levando em consideração apenas combinações que somem 500 calorias.
caracteristicas = []
with open('input.txt') as file:
	linhas = file.read().splitlines()
	for linha in linhas:
		palavras = linha.split()
		nomeIngrediente = palavras[0][:-1]
		valores = (palavras[2][:-1], 
				palavras[4][:-1],
				palavras[6][:-1],
				palavras[8][:-1],
				palavras[10])
		valores = tuple(map(int,valores))
		caracteristicas.append(valores)

def calcularPontuacao(qtdIngredientes, considerarCalorias = False):
	pontuacao = 1
	for indiceCaracteristica in range(len(caracteristicas[0])-1): #-1 pois calorias não entra
		pontuacaoDessaCaracteristica = 0
		for indiceIngrediente, qtdIngrediente in enumerate(qtdIngredientes):
			pontuacaoDessaCaracteristica += caracteristicas[indiceIngrediente][indiceCaracteristica] * qtdIngrediente
		pontuacaoDessaCaracteristica = max(pontuacaoDessaCaracteristica, 0)
		pontuacao*= pontuacaoDessaCaracteristica
	if considerarCalorias:
		totalDeCalorias = 0
		for indiceIngrediente,qtdIngrediente in enumerate(qtdIngredientes):
			totalDeCalorias += caracteristicas[indiceIngrediente][4] * qtdIngrediente
		if totalDeCalorias != 500:
			return 0 #Presumindo que a resposta vai ser maior que 0
	return pontuacao

pontuacoes = [ calcularPontuacao((qtd1,qtd2,qtd3,(100-qtd1-qtd2-qtd3))) for qtd1 in range(100) 
				for qtd2 in range(100)
				for qtd3 in range(100)]
print("A melhor combinação de ingredientes retorna uma pontuação de", max(pontuacoes))
#Parte 2:
pontuacoes = [ calcularPontuacao((qtd1,qtd2,qtd3,(100-qtd1-qtd2-qtd3)),True) for qtd1 in range(100) 
				for qtd2 in range(100)
				for qtd3 in range(100)]
print("A melhor combinação de ingredientes com 500 calorias retorna uma pontuação de", max(pontuacoes))
