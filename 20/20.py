#Desafio do dia 20/12/2015
#a) Calcular o menor número cuja soma de seus fatores é maior do que um dado número.
#b) Idem, porém cada fator só é contado para números.
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
		elfoInicial = 1
		for numeroElfo in range(elfoInicial,limiteSuperior+1):
			if (numeroCasa % numeroElfo) == 0:
				candidatos = (numeroElfo, int(numeroCasa/numeroElfo))
				soma = 0
				if candidatos[0] == candidatos[1]: #Quando for a exata raiz, não calcular 2x
					candidatos = [candidatos[0]]
				for candidato in candidatos:
					if not Parte2 or (candidato > (int(numeroCasa/50))):
							soma+=candidato
				numeroDePresentes += soma * valorDeCadaElfo	
	return numeroCasa
print("Casa de menor valor a alcançar", numeroMinimo, "presentes:", menorNumeroDeCasa(numeroMinimo))
print("Com os elfos entregando até 50 casas, a casa de menor valor é:", menorNumeroDeCasa(numeroMinimo, True))
