#Desafio do dia 20/12/2015
#a) Calcular o menor número cuja soma de seus fatores é maior do que um dado número.
#b) Idem, porém cada fator só é contado para números 
import math
with open('input.txt') as file:
	numeroMinimo = int(file.read().splitlines()[0])

def menorNumeroDeCasa(numeroMinimo, Parte2 = False):
	valorDeCadaElfo = 11 if Parte2 else 10
	numeroDePresentes = 0
	maior = 0
	numeroCasa = 0
	while numeroDePresentes < numeroMinimo:
		numeroDePresentes = 0
		numeroCasa += 1
		limiteSuperior = int(math.floor(numeroCasa ** (1/2)))
		elfoInicial = int(math.ceil(numeroCasa/50)) if Parte2 else 1
		for numeroElfo in range(elfoInicial,limiteSuperior+1):
			if (numeroCasa % numeroElfo) == 0:
				numeroDePresentes += numeroElfo*valorDeCadaElfo
				if numeroCasa != numeroElfo**2: #Se ele chegar exatamente na raiz contaria 2x
					numeroDePresentes += int(numeroCasa / numeroElfo) * valorDeCadaElfo
	return numeroCasa
print(menorNumeroDeCasa(numeroMinimo))
#print(menorNumeroDeCasa(numeroMinimo, True))
