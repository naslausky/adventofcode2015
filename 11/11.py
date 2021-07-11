#Desafio do dia 11/12/2015
#a) Incrementar uma string inicial até encontrar a próxima que atende as condições estabelecidas.
#b) Obter a próxima string depois dessa que também atende os mesmos critérios.
with open('input.txt') as file:
	senhaInicial = file.read().strip()
def incrementarString(string): #Função que incrementa uma string. 'aa' -> 'ab' e 'az' -> 'ba'.
	stringIncrementada = ''
	vaiUm = True
	for caracter in reversed(string):
		if vaiUm:
			vaiUm = False
			if caracter == 'z':
				stringIncrementada+='a'
				vaiUm=True
			else:
				stringIncrementada+= chr(ord(caracter)+1)
		else:
			stringIncrementada+=caracter
	return ''.join(reversed(stringIncrementada))
def atendePrimeiraRegra(string): #Precisa conter três caracteres seguidos que sejam consecutivos. ('abc')
	for indice in range (len(string)-2):
		if ((ord(string[indice])+1 == ord(string[indice+1])) and
		    (ord(string[indice+1])+1 == ord(string[indice+2]))):
			return True
	return False
def atendeSegundaRegra(string): #Não pode conter nenhum dos caracteres (i,o,l)
	letrasProibidas = 'iol'
	for letra in letrasProibidas:
		if letra in string:
			return False
	return True
def atendeTerceiraRegra(string):
	numeroDeParesDeCaracteresIguais = 0
	ultimoCaracterRepetido = ''
	indiceCaracter = 0
	while indiceCaracter < len(string)-1:
		if string[indiceCaracter] == string[indiceCaracter+1]:
			if string[indiceCaracter] != ultimoCaracterRepetido:
				ultimoCaracterRepetido = string[indiceCaracter]
				numeroDeParesDeCaracteresIguais += 1
				indiceCaracter+=1
		indiceCaracter+=1
	return numeroDeParesDeCaracteresIguais > 1
senhaDaVez = senhaInicial
proximasSenhasValidas = []
while(len(proximasSenhasValidas)<2):
	senhaDaVez = incrementarString(senhaDaVez)
	if (atendePrimeiraRegra(senhaDaVez) and 
	    atendeSegundaRegra(senhaDaVez) and 
            atendeTerceiraRegra(senhaDaVez)):
		proximasSenhasValidas.append(senhaDaVez)
[print('Próxima senha válida:', senha) for senha in proximasSenhasValidas]
