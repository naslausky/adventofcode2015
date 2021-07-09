import hashlib
#Desafio do dia 04/12/2015
#a) Receber uma string, e descobrir qual outra string concatenada a ela resulta em uma hash md5 que comeca por 5 zeros.
#b) Idem porem para 6 zeros.
with open('input.txt') as file:
	chaveSecreta = file.read().splitlines()[0]

def encontrarSolucao(n): #Funcao que encontra solucao para dado numero de zeros
	resposta = 0
	while (True):
		resultadoHash = hashlib.md5((chaveSecreta + str(resposta)).encode()).hexdigest()
		if (resultadoHash[:n]) == '0'*n:
			break
		resposta+=1
	return resposta

[print('Menor número para obter', n , 'zeros ao começo da hash md5:', encontrarSolucao(n)) for n in (5,6)]
