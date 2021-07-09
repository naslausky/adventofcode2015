#Desafio do dia 07/12/2015
#a)Receber um conjunto de operações lógicas entre nós nomeados. Retornar o valor do nó 'a'.
#b)

with open('input.txt') as file:
	conexoes = file.read().splitlines()

instrucoes = {} #Dicionário que relaciona cada nó a sua formação
valores = {} #Dicionário que relaciona cada nó a seu valor, para caso passe duas vezes não calcular de novo
for conexao in conexoes:
	instrucao , nomeDoNo = conexao.split(' -> ')
	instrucoes[nomeDoNo] = instrucao

def valorDoNo(nomeDoNo): #Função recursiva que descobre o valor daquele nó
	if nomeDoNo in valores:
		return valores[nomeDoNo]

	if nomeDoNo not in instrucoes: #Recebeu um valor puro
		valores[nomeDoNo] = int(nomeDoNo)
		return int(nomeDoNo)

	instrucao = instrucoes[nomeDoNo]
	if 'NOT' in instrucao:
		outroNo = instrucao.split()[1]
		valores[nomeDoNo] = ~valorDoNo(outroNo)
		return ~valorDoNo(outroNo)
	elif 'AND' in instrucao:
		no1, no2 = instrucao.split(' AND ')
		valores[nomeDoNo] = valorDoNo(no1) & valorDoNo(no2)
		return valorDoNo(no1) & valorDoNo(no2)
	elif 'OR' in instrucao:
		no1, no2 = instrucao.split(' OR ')
		valores[nomeDoNo] = valorDoNo(no1) | valorDoNo(no2)
		return valorDoNo(no1) | valorDoNo(no2)
	elif 'RSHIFT' in instrucao:
		no, valorDeslocamento = instrucao.split(' RSHIFT ')
		valores[nomeDoNo] = valorDoNo(no) >> int(valorDeslocamento)
		return valorDoNo(no) >> int(valorDeslocamento)
	elif 'LSHIFT' in instrucao:
		no, valorDeslocamento = instrucao.split(' LSHIFT ')
		valores[nomeDoNo] = valorDoNo(no) << int(valorDeslocamento)
		return valorDoNo(no) << int(valorDeslocamento)
	else: # Recebe sinal de outro nó
		valores[nomeDoNo] = valorDoNo(instrucao)
		return valorDoNo(instrucao)
print(valorDoNo('a'))
