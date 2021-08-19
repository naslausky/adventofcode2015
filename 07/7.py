#Desafio do dia 07/12/2015
#a)Receber um conjunto de operações lógicas entre nós nomeados. Retornar o valor do nó 'a'.
#b)Substituir a resposta da primeira parte como o valor do nó 'b' e re-calcular o valor do nó 'a'.

with open('input.txt') as file:
	conexoes = file.read().splitlines()
instrucoes = {} #Dicionário que relaciona cada nó a sua formação
valores = {} #Dicionário que relaciona cada nó a seu valor, para caso passe duas vezes não calcular de novo
for conexao in conexoes:
	instrucao , nomeDoNo = conexao.split(' -> ')
	instrucoes[nomeDoNo] = instrucao

def valorDoNo(nomeDoNo): #Função recursiva que descobre o valor daquele nó
	if nomeDoNo in valores: #Já obteve o resultado desde nó, não tem porque fazer de novo
		return valores[nomeDoNo]

	if nomeDoNo not in instrucoes: #Recebeu um número que não depende de nenhum outro nó
		valor = int(nomeDoNo)
	else:
		instrucao = instrucoes[nomeDoNo]
		if 'NOT' in instrucao:
			outroNo = instrucao.split()[1]
			valor = ~valorDoNo(outroNo)
		elif 'AND' in instrucao:
			no1, no2 = instrucao.split(' AND ')
			valor = valorDoNo(no1) & valorDoNo(no2)
		elif 'OR' in instrucao:
			no1, no2 = instrucao.split(' OR ')
			valor = valorDoNo(no1) | valorDoNo(no2)
		elif 'RSHIFT' in instrucao:
			no, valorDeslocamento = instrucao.split(' RSHIFT ')
			valor = valorDoNo(no) >> int(valorDeslocamento)
		elif 'LSHIFT' in instrucao:
			no, valorDeslocamento = instrucao.split(' LSHIFT ')
			valor = valorDoNo(no) << int(valorDeslocamento)
		else: # Recebe sinal de outro nó
			valor = valorDoNo(instrucao)
	valores[nomeDoNo] = valor #Salva em uma tabela para não precisar calcular de novo
	return valor
valorDoNoA = valorDoNo('a')
print('Valor obtido no Nó A:', valorDoNoA)
#Parte 2:
instrucoes['b'] = str(valorDoNoA)
valores = {}
valorDoNoA = valorDoNo('a')
print('Valor obtido no Nó A após a substituição do valor do Nó B:', valorDoNoA)
