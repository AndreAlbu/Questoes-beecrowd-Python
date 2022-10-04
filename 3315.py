def preencher():

	a,b,c,d,e,f,g = map(int, input().split())

	lista = [a,b,c,d,e,f,g]

	return sum(lista)

dias = []

for i in range(4):

	valor = preencher()

	dias.append(valor)

maior = max(dias)
biMaior = bin(maior)

biMaior = biMaior[2:]

print("{} = {}".format(maior, biMaior))