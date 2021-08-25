#Desafio do dia 23/12/2015
#a) Receber um conjunto de instruções que executam sobre dois registradores. 
#   Informar o valor de um dos registradores ao término do programa.
#b) Idem porém com um dos registradores começando com valor inicial 1.
with open('input.txt') as file:
	instrucoes = file.read().splitlines()

def executarInstrucoes(Parte2 = False):#Função que retorna o valor do registrador B para parte 1 ou 2.
	indice=0
	registradorA = 1 if Parte2 else 0
	registradorB = 0
	while indice>=0 and indice<len(instrucoes):
		instrucaoDaVez = instrucoes[indice]
		comando, valor = instrucaoDaVez.split(' ', 1)
		if comando == 'hlf':
			if 'a' in valor:
				registradorA = int(registradorA / 2)
			else:
				registradorB = int(registradorB / 2)
			indice += 1
		elif comando == 'tpl':
			if 'a' in valor:
				registradorA = registradorA * 3 
			else:
				registradorB = registradorB * 3
			indice += 1
			
		elif comando == 'inc':
			if 'a' in valor:
				registradorA += 1 
			else:
				registradorB += 1
			indice += 1
		elif comando == 'jmp':
			offset = int(valor)
			indice += offset
		elif comando == 'jie':
			registrador, offset = valor.split()
			offset = int(offset)
			if 'a' in registrador:
				if registradorA % 2 == 0:
					indice += offset
				else:
					indice += 1
			else:
				if registradorB % 2 == 0:
					indice += offset
				else:
					indice += 1

		elif comando == 'jio':
			registrador, offset = valor.split()
			offset = int(offset)
			if 'a' in registrador:
				if registradorA == 1:
					indice += offset
				else:
					indice += 1
			else:
				if registradorB == 1:
					indice += offset
				else:
					indice += 1
	return registradorB
print('Valor do registrador B caso o registrador A tenha valor inicial nulo:', executarInstrucoes())
print('Valor do registrador B caso o registrador A tenha valor inicial unitário:', executarInstrucoes(True))
