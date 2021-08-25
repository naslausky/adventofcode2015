#Desafio do dia 24/12/2015:
#a) Receber uma lista de números e dividir em 3 grupos de mesma soma, onde um grupo tenha o menor número de elementos.
#   Calcular o menor produto do menor grupo que satisfaça essas regras.
#b) Idem porém para 4 grupos.
import itertools
with open('input.txt') as file:
	pesos = file.read().splitlines()
	pesos = set(map(int,pesos))

pesoEmCadaParte = sum(pesos) / 3
menorValorQuantico = 10**100
achou = False
for numeroDePresentes in range(1,len(pesos)+1): #Quantidade de presentes no primeiro grupo.
	if achou:
		break
	for combinacao in itertools.combinations(pesos,numeroDePresentes):
		if sum(combinacao) != pesoEmCadaParte:
			continue
		if not achou: #Se não achou, verificar se o que sobrar desse grupo pode se dividir em outros dois grupos válidos.
			pesosRestantes = pesos - set(combinacao)
			for numeroDePresentes2 in range(1, len(pesosRestantes)+1):
				for combinacao2 in itertools.combinations(pesosRestantes,numeroDePresentes2):
					if sum(combinacao2) == pesoEmCadaParte:
						achou = True
						break
				if achou:
					break
		if achou: #Não pode ser else pois pode ser que venha direto do if de cima.
			multiplicacao = 1
			for elemento in  combinacao:
				multiplicacao *= elemento
			menorValorQuantico = min(menorValorQuantico, multiplicacao)
print('Com 3 grupos, o menor valor quântico das disposições que usam o menor número de elementos:', menorValorQuantico)	

#Parte 2:
pesoEmCadaParte = sum(pesos) / 4
menorValorQuantico = 10**100
achou = False
for numeroDePresentes in range(1,len(pesos)+1): #Quantidade de presentes no primeiro grupo.
	if achou:
		break
	for combinacao in itertools.combinations(pesos,numeroDePresentes):
		if sum(combinacao) != pesoEmCadaParte:
			continue
		if not achou: #Se não achou, verificar se o que sobrar desse grupo pode se dividir em outros três grupos válidos.
			pesosRestantes = pesos - set(combinacao)
			for numeroDePresentes2 in range(1, len(pesosRestantes)+1):
				for combinacao2 in itertools.combinations(pesosRestantes,numeroDePresentes2):
					if sum(combinacao2) != pesoEmCadaParte:
						continue
					pesosFinais = pesosRestantes - set(combinacao2)
					for numeroDePresentes3 in range(1,len(pesosFinais)+1):
						if not achou: #Se bobiar nem precisa dessa verificação pois esse último for é pequeno.
							for combinacao3 in itertools.combinations(pesosFinais,numeroDePresentes3):
								if sum(combinacao3) == pesoEmCadaParte:
									achou = True
									break
						if achou:
							break
				if achou:
					break
		if achou: #Não pode ser else pois pode ser que venha direto do if de cima.
			multiplicacao = 1
			for elemento in  combinacao:
				multiplicacao *= elemento
			menorValorQuantico = min(menorValorQuantico, multiplicacao)
print('Com 4 grupos, o menor valor quântico das disposições que usam o menor número de elementos:', menorValorQuantico)	
