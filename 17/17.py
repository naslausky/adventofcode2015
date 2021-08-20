#Desafio do dia 17/12/2015
#a) Dado uma lista de números, e uma soma, calcular quantas combinações desses números tem essa soma.
#b) Idem, porém apenas as combinações que usam a menor quantidade de números possível.

with open('input.txt') as file:
	linhas = file.read().splitlines()
	reservatorios = list(map(int,linhas))
	reservatorios.sort()

menorNumeroDeReservatorios = len(reservatorios)
def quantidadeDeManeiras(litros, reservatorios,numeroDeReservatoriosUsadosAteAgora, parte2 = False):
	global menorNumeroDeReservatorios 
	resposta = 0
	for indice, reservatorio in enumerate(reservatorios):
		if litros - reservatorio == 0:
			if not parte2: #Na parte 2, só contabiliza se for o menor número
				resposta+=1
			elif menorNumeroDeReservatorios == numeroDeReservatoriosUsadosAteAgora:
				resposta+=1
			menorNumeroDeReservatorios = min(numeroDeReservatoriosUsadosAteAgora, menorNumeroDeReservatorios)
		elif litros-reservatorio < 0: #Caso impossível, não contabilizar
			continue
		else: #Chama a função de novo apenas com os reservatórios posteriores
			resposta += quantidadeDeManeiras( litros-reservatorio, 
					reservatorios[indice+1:], 
					numeroDeReservatoriosUsadosAteAgora+1,
					parte2)
	return resposta
#Na primeira passada aproveita e já vê o menor número
print('Maneiras diferentes de guardar 150 litros:', quantidadeDeManeiras(150,reservatorios,0)) 
#Parte 2:#Assim, na segunda só contabilizar esses.
print('Maneiras diferentes de guardar 150 litros usando o mínimo de reservatórios possíveis:', quantidadeDeManeiras(150,reservatorios,0,True))
