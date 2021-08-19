#Desafio do dia 06/12/2015
#a)Receber uma lista de instruções acerca de booleanos dispostos em uma tabela de 1000x1000 elementos.
# Dizer ao final das instruções quantos booleanos estão ativos.
#b)Modificar as instruções para adequar inteiros ao invés de booleanos, e calcular a mesma coisa.

with open('input.txt') as file:
	instrucoes = file.read().splitlines()
tabuleiro = {}
for instrucao in instrucoes:
	elementosDaInstrucao = instrucao.split()
	intervalo = (tuple(map(int, elementosDaInstrucao[-1].split(','))), 
		     tuple(map(int,elementosDaInstrucao[-3].split(','))))
	variacaoHorizontal = sorted((intervalo[0][0],intervalo[1][0]))
	variacaoVertical = sorted((intervalo[0][1],intervalo[1][1]))
	for indiceHorizontal in range(variacaoHorizontal[0], variacaoHorizontal[1]+1):
		for indiceVertical in range(variacaoVertical[0], variacaoVertical[1]+1):
			chave = (indiceHorizontal,indiceVertical)
			if 'turn on' in instrucao:
				tabuleiro[chave] = True
			elif 'turn off' in instrucao:
				tabuleiro[chave] = False
			else: #Toggle
				tabuleiro[chave] = not (tabuleiro.get(chave,False))
numeroDeLuzesLigadas = len([chave for chave,valor in tabuleiro.items() if valor])
print('Número de casas com luzes ligadas:', numeroDeLuzesLigadas)
#Parte 2:
tabuleiro={}
brilhoTotal = 0
for instrucao in instrucoes:
	elementosDaInstrucao = instrucao.split()
	intervalo = (tuple(map(int, elementosDaInstrucao[-1].split(','))), 
		     tuple(map(int,elementosDaInstrucao[-3].split(','))))
	variacaoHorizontal = sorted((intervalo[0][0],intervalo[1][0]))
	variacaoVertical = sorted((intervalo[0][1],intervalo[1][1]))
	for indiceHorizontal in range(variacaoHorizontal[0], variacaoHorizontal[1]+1):
		for indiceVertical in range(variacaoVertical[0], variacaoVertical[1]+1):
			chave = (indiceHorizontal,indiceVertical)
			if 'turn on' in instrucao:
				tabuleiro[chave] = tabuleiro.get(chave,0)+1
			elif 'turn off' in instrucao:
				tabuleiro[chave] = tabuleiro.get(chave,0)-1
				if tabuleiro[chave]<0:
					tabuleiro[chave]=0
			else: #Toggle
				tabuleiro[chave] = tabuleiro.get(chave,0)+2
brilhoTotal = sum([valor for chave, valor in tabuleiro.items()])
print('Brilho total de todas as casas:', brilhoTotal)
