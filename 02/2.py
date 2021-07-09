#Desafio do dia 02/12/2020
#a) Receber uma lista de dimensões de caixas.
#   Para cada conjunto de dimensões, e calcular a quantidade de papel de embrulho necessário.
#b) Calcular o comprimento necessário para fazer o laço.

with open('input.txt') as file:
	listaDeDimensoes = file.read().splitlines()
totalDePapelNecessario = 0
comprimentoTotalDeLacoNecessario = 0
for dimensoes in listaDeDimensoes:
	listaDimensoes = [int(dimensao) for dimensao in dimensoes.split('x')]
	listaDimensoes.sort()
	totalDePapelNecessario += (2 * listaDimensoes[0] * listaDimensoes[1] +
				  2 * listaDimensoes[1] * listaDimensoes[2] +
				  2 * listaDimensoes[0] * listaDimensoes[2])
	totalDePapelNecessario += listaDimensoes[0]*listaDimensoes[1]
#Parte 2:
	comprimentoTotalDeLacoNecessario += 2 * listaDimensoes[0] + 2 * listaDimensoes[1] 
	comprimentoTotalDeLacoNecessario += listaDimensoes[0] * listaDimensoes[1] * listaDimensoes[2]
print("Total de papel de embrulho necessário:", totalDePapelNecessario)
print("Comprimento total de laço necessário:", comprimentoTotalDeLacoNecessario)
