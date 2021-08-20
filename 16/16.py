#Desafio do dia 16/12/2015
#a) Dentre uma lista de caracteristicas, achar o índice que tem melhor combinação dos valores das características com um dado gabarito.
#b) Algumas das entradas do gabarito não representam os valores exatos, mas sim um limite superior ou inferior.
dicionariosTias = []
with open('input.txt') as file:
	linhas = file.read().splitlines()
	for linha in linhas:
		dicionarioDestaTia = {}
		lembrancas = ''.join(linha.split(':')[1:])
		lembrancas = lembrancas.split(',')
		for lembranca in lembrancas:
			chave, valor = lembranca.split()
			dicionarioDestaTia[chave] = int(valor)
		dicionariosTias.append(dicionarioDestaTia)

gabarito = {'children': 3,
'cats': 7,
'samoyeds': 2,
'pomeranians': 3,
'akitas': 0,
'vizslas': 0,
'goldfish': 5,
'trees': 3,
'cars': 2,
'perfumes': 1}

maiorPontuacao = 0
indiceTiaMaiorPontuacao = 0
for indiceTia, dicTia in enumerate(dicionariosTias):
	pontuacaoDestaTia = 0
	for chave, valor in dicTia.items():
		if gabarito[chave]==valor:
			pontuacaoDestaTia += 1	
	if pontuacaoDestaTia > maiorPontuacao:
		maiorPontuacao = pontuacaoDestaTia
		indiceTiaMaiorPontuacao = indiceTia+1
print('Indice da tia com maior número de quantidades corretas:', indiceTiaMaiorPontuacao)

#Parte 2:
maiorPontuacao = 0
indiceTiaMaiorPontuacao = 0
for indiceTia, dicTia in enumerate(dicionariosTias):
	pontuacaoDestaTia = 0
	for chave, valor in dicTia.items():
		if chave == 'cats' or chave == 'trees':
			if gabarito[chave] < valor:
				pontuacaoDestaTia += 1	
		elif chave == 'pomeranians' or chave == 'goldfish':
			if gabarito[chave] > valor:
				pontuacaoDestaTia += 1	
		elif gabarito[chave]==valor:
			pontuacaoDestaTia += 1	
	if pontuacaoDestaTia > maiorPontuacao:
		maiorPontuacao = pontuacaoDestaTia
		indiceTiaMaiorPontuacao = indiceTia+1
print('Indice da tia com maior número de quantidades corretas respeitando os alcances:', indiceTiaMaiorPontuacao)
