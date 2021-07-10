#Desafio do dia 08/12/2015
#a) Avaliar a diferença entre número de caracteres exibidos e número de caracteres na descrição de uma string.
#b) Avaliar a diferença entre essa descrição e a descrição da descrição. (Isto é, recodificar)

with open('input.txt') as file:
	strings = file.read().splitlines()
diferencaTotal = 0
diferencaTotalInversa = 0 #Parte 2
for string in strings:
	caracteresNaStringLiteral = len(string)
	caracteresNaStringAvaliada = len(eval(string))
	diferencaTotal += caracteresNaStringLiteral - caracteresNaStringAvaliada
	#Parte 2:
	numeroDeCaracteresExtras = 2
	numeroDeCaracteresExtras += string.count('\\') + string.count('"')
	diferencaTotalInversa +=numeroDeCaracteresExtras
print('Diferença total entre a string e a sua versão decodificada:', diferencaTotal)
print('Diferença total entre a string e a sua versão codificada:', diferencaTotalInversa)
