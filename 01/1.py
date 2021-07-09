#Desafio do dia 01/12/2015
#a) Receber uma lista de parênteses e contar a diferença entre o número dos que abrem e os que fecham.
#b) Verificar o índice do primeiro caracter que torna a diferença negativa.

with open('input.txt') as file:
	instrucoes = file.read()
resposta = 0
respostaParte2 = 0
for indice, caracter in enumerate(instrucoes):
	if caracter == '(':
		resposta += 1	
	else:
		resposta -= 1
	if resposta < 0 and not respostaParte2:
		respostaParte2 = indice+1
print("Andar resultante final:", resposta)
print("Índice primeiro caracter que leva para o porão:",respostaParte2)
