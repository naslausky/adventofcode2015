#Desafio do dia 14/12/2015
#a)Receber uma lista de renas, onde cada um tem uma velocidade e um tempo de descanso.
#  Calcular a rena que chegou mais longe após uma determinada quantidade de segundos.
#b) Calcular a rena que ficou durante o maior tempo na liderança e retornar quanto tempo ela ficou.
renas = [] #Lista de tuplas onde cada tupla tem os 3 valores referentes aquela rena.
class Rena:
	def __init__(self, tupla):
		self.velocidade, self.tempoCorrendo, self.tempoDescansando = tupla
		self.correndo = True
		self.tempoDeSobraParaCorrer = self.tempoCorrendo
		self.tempoDeSobraParaDescansar = self.tempoDescansando
		self.distanciaPercorrida = 0
		self.pontos = 0 #Parte 2
	def passou1Segundo(self):
		if self.correndo:
			self.distanciaPercorrida += self.velocidade
			self.tempoDeSobraParaCorrer -= 1
			if self.tempoDeSobraParaCorrer==0:
				self.correndo=False
				self.tempoDeSobraParaDescansar = self.tempoDescansando
		else:
			self.tempoDeSobraParaDescansar -= 1
			if self.tempoDeSobraParaDescansar == 0:
				self.correndo = True
				self.tempoDeSobraParaCorrer = self.tempoCorrendo
	
with open('input.txt') as file:
	linhas = file.read().splitlines()
	for linha in linhas:
		palavras = linha.split()
		renas.append(Rena(( int(palavras[3]),
				int(palavras[6]),
				int(palavras[-2]))))
for _ in range(2503):
	for rena in renas:
		rena.passou1Segundo()
	maiorDistanciaPercorrida = max([rena.distanciaPercorrida for rena in renas])
	for rena in renas:
		if rena.distanciaPercorrida == maiorDistanciaPercorrida:
			rena.pontos+=1
maiorDistanciaPercorrida = max([rena.distanciaPercorrida for rena in renas])
print("Maior distância percorrida entre as renas ao término do tempo:", maiorDistanciaPercorrida)
#Parte 2:
maiorPontuacao = max([rena.pontos for rena in renas])
print("Maior pontuação entre as renas:", maiorPontuacao)
