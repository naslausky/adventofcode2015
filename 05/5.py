#Desafio do dia 05/12/2015
#a) Receber uma lista de string, e informar quantas destas acatam a um conjunto de regras.
#b) Idem porém com outro conjunto de regras
with open('input.txt') as file:
	strings = file.read().splitlines()
numeroDeStringsQueAtendemARegra = 0
for string in strings:
	atendeARegra1 = True #Regra 1: Conter no minimo 3 vogais.
	vogais = ('a','e','i','o','u')
	numeroDeVogais = 0
	for caracter in string:
		if caracter in vogais:
			numeroDeVogais+=1
	if numeroDeVogais < 3:
		atendeARegra1 = False
	atendeARegra2 = False #Regra 2: Conter no mínimo uma vez dois caracteres iguais seguidos.
	for indiceCaracter in range(len(string)-1):
		if string[indiceCaracter] == string[indiceCaracter+1]:
			atendeARegra2 = True
	atendeARegra3 = True #Regra 3: Não conter nenhuma das strings proibidas.
	stringsProibidas = ('ab','cd','pq','xy')
	for stringProibida in stringsProibidas:
		if stringProibida in string:
			atendeARegra3 = False
	if (atendeARegra1 and atendeARegra2 and atendeARegra3):
		numeroDeStringsQueAtendemARegra+=1
print('Número de strings que atendem ao primeiro conjunto de regras:', numeroDeStringsQueAtendemARegra)
#Parte 2:
numeroDeStringsQueAtendemARegra2=0
for string in strings:
	atendeANovaRegra1 = False #Conter no mínimo um conjunto de 2 caracteres seguidos que se repete.
	for indiceCaracter in range(len(string)-1):
		if string.count(string[indiceCaracter:indiceCaracter+2])>1:
			atendeANovaRegra1=True
			break
	atendeANovaRegra2 = False #Conter no mínimo um conjunto de 3 caracteres seguidos que o primeiro é igual ao último
	for indiceCaracter in range(len(string)-2): 
		if string[indiceCaracter] == string[indiceCaracter+2]:
			atendeANovaRegra2 = True
	if atendeANovaRegra1 and atendeANovaRegra2:
		numeroDeStringsQueAtendemARegra2 +=1
print('Número de strings que atendem ao segundo conjunto de regras:', numeroDeStringsQueAtendemARegra2)
