c = int(input())

for i in range(c):

    notasAlunos = list(map(int, input().split()))

    remove = notasAlunos[0]

    notasAlunos.remove(remove)

    media = sum(notasAlunos) / remove

    cont = percentual = 0

    for j in range(remove):

        if(notasAlunos[j] > media):

            cont = cont + 1

    percentual = cont * 100.00 / remove

    print("{0:.3f}%".format(percentual))