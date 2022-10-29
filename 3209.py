n = int(input(""))

for i in range(n):

	filtros = [int(x) for x in input().split()] 

	dif = filtros[0] - 1

	qtdFiltro = sum(filtros[1:])

	print(qtdFiltro - dif)
