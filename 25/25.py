#Desafio do dia 25/12/2015
#a)Receber uma regra de geração de números onde cada número se baseia no anterior e fornecer o enésimo elemento, baseado numa disposição dos números em uma grade infinita.
#b)Ligar a máquina e fazer nevar.

with open('input.txt') as file:
	linha = file.read().splitlines()[0]
	palavras = linha.split()
	linha, coluna = palavras[-3], palavras[-1]
	linha = int(linha.replace(',',''))
	coluna = int(coluna.replace('.',''))

indiceLinha = indiceColuna = 1 
ultimoNumeroCalculado = 20151125
while (indiceLinha != linha) or (indiceColuna != coluna):
	#Acha a coordenada do próximo elemento:
	if indiceLinha == 1:
		indiceLinha = indiceColuna + 1
		indiceColuna = 1
	else:
		indiceLinha -= 1
		indiceColuna += 1
	#Calcula o número da vez:
	novoNumero = (ultimoNumeroCalculado * 252533) % 33554393
	ultimoNumeroCalculado = novoNumero
print('O elemento da linha', linha, 'e coluna', coluna, 'é:', ultimoNumeroCalculado)
