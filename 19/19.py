#Problema do dia 19/12/2015
#a)Receber uma palavra e uma lista de substituições. 
#  Contar quantos resultados finais podem ser alcançados quando se faz todas as substituições possíveis.
#b)Dado um elemento inicial, qual o número mínimo de substituições que precisa para alcançar a palavra.

regrasSubstituicoes = []
with open('input.txt') as file:
	linhasSubstituicoes, palavra = file.read().split('\n\n')
	palavra = palavra.strip()
	linhasSubstituicoes = linhasSubstituicoes.splitlines()
	for linha in linhasSubstituicoes:
		anterior, proximo = linha.split(' => ')
		regrasSubstituicoes.append((anterior,proximo))

palavrasResultantesPossiveis = set()
for regra in regrasSubstituicoes:
	tamanhoDaRegra = len(regra[0])
	for indiceLetra in range(len(palavra) - tamanhoDaRegra +1):
		if palavra[indiceLetra : indiceLetra+tamanhoDaRegra] == regra[0]:
			palavraResultante = palavra[:indiceLetra] + regra[1] + palavra[indiceLetra+tamanhoDaRegra:]
			palavrasResultantesPossiveis.add(palavraResultante)
print('Número de combinações possíveis após uma substituição:', len(palavrasResultantesPossiveis))

#Parte 2:
numeroDeYs = palavra.count('Y')
numeroDeRns = palavra.count('Rn')
numeroDeArs = palavra.count('Ar') #Igual ao valor de cima
palavra = palavra.replace('Ar','') #Como esses elementos só existem do lado direito das substituições,
palavra = palavra.replace('Rn','') #eles não devem ser considerados na contagem de elementos.
palavra = palavra.replace('Y','') 

#Cada elemento é uma letra maiúscula (depois de removidos os Ar, Rn, e Y)
numeroDeElementos = sum([1 for letra in palavra if letra.isupper()] )

#As operações normais (as que não são com Ar e Rn) transformam 1 elemento em 2:
#Logo, pra transformar X elementos em 1, precisa de X - 1:
numeroDeOperacoes = numeroDeElementos - 1

#Cada conjunto de Ars + Rns vai virar um elemento só, 
#e como eles sempre tem algo entre eles, 
# essa operação ja tá contabilizada na linha de cima quando eu contei os elementos de dentro.

# Para cada Y, diminui a necessidade de necessidade de 1 operação pq ele já junta de brinde.
# Nas fórmulas Rn __ Y __ (Y__(Y__)) Ar ele junta o elemento da esquerda com o da direita.
numeroDeOperacoes -= numeroDeYs
print('Número mínimo de passos necessário para chegar à molecula desejada:', numeroDeOperacoes)

##Outras tentativas:
## Força bruta: - Muito dispendioso
#conjuntoPalavrasPossiveis = {'e'}
#palavrasJaVerificadas = set()
#numeroDePassos = 0
#while palavra not in conjuntoPalavrasPossiveis:
#	novoConjuntoASeVerificar = set()
#	for palavraDaVez in (conjuntoPalavrasPossiveis - palavrasJaVerificadas):
#		for regra in regrasSubstituicoes:
#			tamanhoDaRegra = len(regra[0])
#			for indiceLetra in range(len(palavraDaVez) - tamanhoDaRegra +1):
#				if palavraDaVez[indiceLetra : indiceLetra+tamanhoDaRegra] == regra[0]:
#					palavraResultante = palavraDaVez[:indiceLetra] + regra[1] + palavraDaVez[indiceLetra+tamanhoDaRegra:]
#					novoConjuntoASeVerificar.add(palavraResultante)
#			
#		palavrasJaVerificadas.add(palavraDaVez)
#	conjuntoPalavrasPossiveis = novoConjuntoASeVerificar
#	numeroDePassos += 1
#	print(numeroDePassos)

##  Sair substituindo os maiores possíveis primeiro, até chegar no mínimo.
##  Provavelmente funcionária se ao invés de tentar o maiores, ficasse chutando quais substituições fazer.
#regrasSubstituicoes.sort(key = lambda tupla:len(tupla[1]),reverse = True)
#conjuntoPalavrasPossiveis = {palavra}
#numeroDePassos = 0
#while 'e' not in conjuntoPalavrasPossiveis:
#	novoConjuntoASeVerificar = set()
#	for palavraDaVez in conjuntoPalavrasPossiveis:
#		for regra in regrasSubstituicoes:
#			novoConjuntoASeVerificar.add(palavraDaVez.replace(regra[1],regra[0]))
#
#	conjuntoPalavrasPossiveis = novoConjuntoASeVerificar

## Fazer exatamente a conta que eu fiz acima, mas contando 1 de cada vez.
## Era pra funcionar, mas errei alguma coisa.
#def acharSubPalavras(palavra):
#	novasPalavras = []
#	#Depois que todas as internas funcionarem, ainda sobra ela se for do tipo Rn - Y - Ar
#	#porém todas as regras que comecam com Rn, tem um elemento a esquerda
#	#Se essa sub palavra começa direto com Rn, 
	#não é pra contar pois ela ainda vai juntar com um elemento que sobrar de outra
#	operacoesNecessariasNessaPalavra = 0
#	indiceInicio = palavra.find('Rn')
#	if indiceInicio>0:
#		operacoesNecessariasNessaPalavra = 1
#	if indiceInicio < 0:
#		novasPalavras.append(palavra)
#	else:
#		novasPalavras.extend(palavra[indiceInicio+2:-2].split('Y'))
#	for p in novasPalavras:
#		numeroDeElementos = sum([1 for c in p if c.isupper()])
#		#Cada operacao reduz 1 elemento, e precisa restar 1
#		operacoesNecessariasNessaPalavra += numeroDeElementos - 1
#	return operacoesNecessariasNessaPalavra
#palavras = palavra.split('Ar')
#for indice, p in enumerate(palavras):
#	if indice != len(palavras)-1:
#		palavras[indice] += 'Ar'
#numeroDePassos = 0
#novasPalavras = []
#for palavra in palavras:
#	indiceComeco = palavra.find('Rn')
#	if indiceComeco<0:
#		novasPalavras.append(palavra)
#	elif indiceComeco == 0:
#		if palavra:
#			novasPalavras.append(palavra)
#		
#	else:
#		if palavra[indiceComeco-1].islower():
#			indiceComeco -= 1
#		indiceComeco -= 1
#		if palavra[:indiceComeco]:
#			novasPalavras.append(palavra[:indiceComeco])
#		if palavra[indiceComeco:]:
#			novasPalavras.append(palavra[indiceComeco:])
#for x in novasPalavras:
#	print(x)
#	print(acharSubPalavras(x))
#somaDeOperacoes = sum([acharSubPalavras(x) for x in novasPalavras]) 
#Agora cada palavra em palavraNova virou 1 elemento, precisa reduzir esses:
#somaDeOperacoes += (len(novasPalavras) - 1)
#print(somaDeOperacoes) # 223 too high
