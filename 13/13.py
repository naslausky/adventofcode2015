#Desafio do dia 13/12/2015:
#a) Receber um grafo e organizar os nós de maneira circular de forma a maximizar a soma dos valores
#b) Adicionar um nó de conexões nulas e re-calcular o resultado. 
# Provavelmente é equivalente a calcular o nó com menor contribuição a soma e remover ele.
import itertools

dicionarioAlegria = {} #Dicionário da forma {Ana : {Bob:32,Carol:12}...}
with open('input.txt') as arquivo:
	linhas = arquivo.read().splitlines()
	for linha in linhas:
		palavras = linha.split()
		nomeRecebedor = palavras[0]
		nomePessoaDoLado = palavras[-1].replace('.','')
		valorAlegria = int(palavras[3])
		if 'lose' in linha:
			valorAlegria *= -1
		if nomeRecebedor not in dicionarioAlegria:
			dicionarioAlegria[nomeRecebedor] = {nomePessoaDoLado : valorAlegria}
		else:
			dicionarioAlegria[nomeRecebedor][nomePessoaDoLado] = valorAlegria

def contabilizarAlegriaTotal (listaPessoas):
	alegriaTotal = 0
	for indicePessoa , _ in enumerate(listaPessoas):
		nomePessoa = listaPessoas[indicePessoa]
		nomePessoaAnterior = listaPessoas[indicePessoa-1]
		nomePessoaPosterior = listaPessoas[(indicePessoa+1) % len(listaPessoas)] 
		alegriaTotal += dicionarioAlegria[nomePessoa][nomePessoaAnterior]
		alegriaTotal += dicionarioAlegria[nomePessoa][nomePessoaPosterior]
	return alegriaTotal
maiorAlegriaTotal = max([contabilizarAlegriaTotal(permutacao) 
			for permutacao in itertools.permutations(dicionarioAlegria)])
print('A maior variação de alegria possível é:', maiorAlegriaTotal)
########### Fazendo sem usar iterTools, da mesma forma que foi feito o dia 9. Obtém a resposta correta, mas acredito que é porque o input é "bonzinho":
#maioresAlegrias = {}
#for pessoaInicial, alegrias in dicionarioAlegria.items():
#	ordemAteAgora = [pessoaInicial]
#	while len(ordemAteAgora) != len(dicionarioAlegria):
#		alegriaMaxima = -10000000
#		pessoaAtual = ordemAteAgora[-1]
#		candidatos = [x for x,_ in dicionarioAlegria.items() if x not in ordemAteAgora]
#		for candidato in candidatos:
#			alegriaPossivel = dicionarioAlegria[pessoaAtual][candidato] + dicionarioAlegria[candidato][pessoaAtual]
#			if alegriaPossivel > alegriaMaxima and (candidato not in ordemAteAgora):
#				alegriaMaxima = alegriaPossivel
#				candidatoComMaiorAlegria = candidato
#		ordemAteAgora.append(candidatoComMaiorAlegria)
#	maioresAlegrias[pessoaInicial] = ordemAteAgora
#print(max([contabilizarAlegriaTotal(x) for _, x in maioresAlegrias.items()]))
###########
#Parte2:
meuNome = 'Naslausky' 
minhasAlegrias = {}
for nome,alegrias in dicionarioAlegria.items():
	alegrias[meuNome] = 0 #Adiciona o novo a todos os dicionários das outras pessoas
	minhasAlegrias[nome] = 0
dicionarioAlegria[meuNome] = minhasAlegrias #Adiciona o meu próprio dicionário de alegrias ao dicionário pai.
maiorAlegriaTotal = max([contabilizarAlegriaTotal(permutacao) 
			for permutacao in itertools.permutations(dicionarioAlegria)])
print('A maior variação de alegria possível comigo incluso é:', maiorAlegriaTotal)
