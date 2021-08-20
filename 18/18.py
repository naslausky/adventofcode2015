#Desafio do dia 18/12/2015
#a) Receber uma matriz de booleanos como estado inicial. 
#   Seguir uma regra de transição 100 vezes e contabilizar o número de True no final.
#b) Idem porém com os cantos da matriz fixos em True.

with open('input.txt') as file:
	mapa = file.read().splitlines()
grade = {}
for indiceLinha in range (100):
	for indiceColuna in range(100):
		grade[(indiceLinha,indiceColuna)] = True if mapa[indiceLinha][indiceColuna] == '#' else False
gradeOriginal = grade.copy() #Para reusar na parte 2
def numeroDeLuzesAoRedor(coordenada):
	x,y = coordenada
	numeroDeLuzesAcesas = 0
	for dx in range(-1,2):
		for dy in range (-1,2):
			tuplaAVerificar = (x+dx, y+dy)
			if tuplaAVerificar == coordenada:
				continue
			if grade.get(tuplaAVerificar, False):
				numeroDeLuzesAcesas += 1
	return numeroDeLuzesAcesas

for _ in range(100): #Fazer 100 vezes
	novosValores = {} #As luzes atualizam-se simultaneamente. Salvar as alterações para realizar de uma vez depois.
	for chave, valor in grade.items():
		numeroDeLuzesAcesasAoRedor = numeroDeLuzesAoRedor(chave)
		if valor:#Uma luz acesa desliga se o numero for diferente de 2 ou 3
			if numeroDeLuzesAcesasAoRedor != 2 and numeroDeLuzesAcesasAoRedor != 3:
				novosValores[chave] = False
		else: #Uma luz apagada acende quando tem 3 acesas ao redor
			if numeroDeLuzesAcesasAoRedor == 3:
				novosValores[chave] = True
	grade.update(novosValores)
print('Número de luzes acesas após 100 iterações:', sum([valor for _,valor in grade.items()]))
#Parte 2:
def acenderOsCantos():
	grade.update({(0,0):True,
			(0,99):True,
			(99,0):True,
			(99,99):True})

grade = gradeOriginal
acenderOsCantos()
for _ in range(100): #Fazer 100 vezes
	novosValores = {} #As luzes atualizam-se simultaneamente. Salvar as alterações para realizar de uma vez depois.
	for chave, valor in grade.items():
		numeroDeLuzesAcesasAoRedor = numeroDeLuzesAoRedor(chave)
		if valor:#Uma luz acesa desliga se o numero for diferente de 2 ou 3
			if numeroDeLuzesAcesasAoRedor != 2 and numeroDeLuzesAcesasAoRedor != 3:
				novosValores[chave] = False
		else: #Uma luz apagada acende quando tem 3 acesas ao redor
			if numeroDeLuzesAcesasAoRedor == 3:
				novosValores[chave] = True
	grade.update(novosValores)
	acenderOsCantos()
print('Número de luzes acesas após 100 iterações com os 4 cantos quebrados:',sum([valor for _,valor in grade.items()]))
