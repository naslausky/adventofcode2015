#Problema do dia 19/12/2015
#a) Receber uma palavra e uma lista de substituições. 
# Contar quantos resultados finais podem ser alcançados quando se faz todas as substituições possíveis.
#b)
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

print(len(palavrasResultantesPossiveis))
#Parte 2:
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

#Parte 2:
#conjuntoPalavrasPossiveis = {palavra}
#numeroDePassos = 0
#while 'e' not in conjuntoPalavrasPossiveis:
#	novoConjuntoASeVerificar = set()
#	for palavraDaVez in conjuntoPalavrasPossiveis:
#		for regra in regrasSubstituicoes:
#			novoConjuntoASeVerificar.add(palavraDaVez.replace(regra[1],regra[0]))
#
#	conjuntoPalavrasPossiveis = novoConjuntoASeVerificar
#Parte 2:
#regrasSubstituicoes.sort(key = lambda tupla:len(tupla[1]),reverse = True)
#numeroDePassos = 0
#while palavra != 'e':
#	for regra in regrasSubstituicoes:
#		if regra[1] in palavra:
#			numeroDePassos += 1
#			palavra = palavra.replace(regra[1],regra[0],1)
#			break
#	print(palavra)

#Parte 2:
while palavra != 'e':
	
print(numeroDePassos)
