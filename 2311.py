n = int(input())

competidores = [ ]
pontuacao = [ ]

for i in range(n):

    notasTotal = 0

    nomeCompetidor = input()
    dificuldade = float(input())
    notas = list(map(float, input().split()))

    competidores.append(nomeCompetidor)

    notas.remove(max(notas))
    notas.remove(min(notas))

    notasTotal = sum(notas)

    notasTotal = notasTotal * dificuldade

    pontuacao.append(notasTotal)

    print("{} {:.2f}".format(nomeCompetidor, notasTotal))