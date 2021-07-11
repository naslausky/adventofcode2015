#Desafio do dia 10/12/2015
#a) Calcular o 40º elemento de uma sequência que o elemento se baseia na leitura verbal do elemento anterior
#b) Idem, porém para o 50º elemento.
with open('input.txt') as file:
	numeroInicial = file.read().strip()

numeroDaVez = numeroInicial
print(numeroDaVez)
for _ in range(50): #Repetir 40 vezes
	proximoNumero = ''
	contagemDeDigitosRepetidos = 0
	ultimoDigito = numeroDaVez[0]
	for digito in numeroDaVez:
		if digito == ultimoDigito:
			contagemDeDigitosRepetidos += 1
		else:
			proximoNumero+=str(contagemDeDigitosRepetidos) + ultimoDigito
			contagemDeDigitosRepetidos = 1
			ultimoDigito = digito
	proximoNumero+=str(contagemDeDigitosRepetidos) + ultimoDigito
	numeroDaVez = proximoNumero
	if (_ == 39):
		print('O comprimento do elemento após 40 iterações é:', len(numeroDaVez))
print('O comprimento do elemento após 50 iterações é:', len(numeroDaVez))
