j, r = map(int, input().split())

totalPontos = [ ]

for i in range(j):

  totalPontos.append(0)

lista = list(map(int, input().split()))

for i in range(len(lista)):

    totalPontos[i % j] += lista[i]

pontos = sorted(totalPontos, reverse = True)[0]

totalPontos.reverse()

for i in range(len(totalPontos)):

  if totalPontos[i] == pontos:

    print(len(totalPontos) - i)

    break