n = float(input())
notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01];

print('NOTAS:')
for i in range(len(notas)):
	qt = 0
	while n-notas[i] >= 0:
		qt += 1
		n -= notas[i]
	print("%d nota(s) de R$ %.2f" % (qt, notas[i]))

print('MOEDAS:')

for i in range(len(moedas)):
	qt = 0
	while n-moedas[i] >= 0:
		qt += 1
		n = float(format(round(n - moedas[i],2)))

	print("%d moeda(s) de R$ %.2f" % (qt, moedas[i]))
