#Desafio do dia 12/12/2015
#a) Receber um json e contar quantos números ele tem.
#b) Idem, porém desconsiderar quaisquer objetos com o valor "red"
import json
with open('input.txt') as file:
	jsonString = file.read().strip()
dicJson = json.loads(jsonString)
def contabilizarNumeros(json, parte2 = False): #Função que soma os números dentro do Json informado.
	somaDosNumeros = 0
	if type(json) is dict:
		if parte2:
			if 'red' in json.values(): #Parte2: Ignorar os que possuem o valor 'red'
				return 0
		for chave,valor in json.items():
			if type(valor) is int or type(valor) is float:
				somaDosNumeros+= valor
			elif type(valor) is dict or type(valor) is list:
				somaDosNumeros+=contabilizarNumeros(valor,parte2)
	else: # É uma lista
		for elemento in json:
			if type(elemento) is int or type(elemento) is float:
				somaDosNumeros+=elemento
			elif type(elemento) is dict or type(elemento) is list:
				somaDosNumeros+=contabilizarNumeros(elemento,parte2)
	return somaDosNumeros
print('Soma de todos os números no Json:', contabilizarNumeros(dicJson))
print('Soma de todos os números no Json, ignorando os dicionários que contem "red":', contabilizarNumeros(dicJson, True))
