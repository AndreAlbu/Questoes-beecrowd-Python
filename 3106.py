n = int(input())

alunos = list(map(int, input().split()))

cont = 0

aux = sum(alunos)

for i in range(len(alunos)):

    while(alunos[i] % 3 != 0):

        cont = cont + 1

        alunos[i] = alunos[i] - 1

print(aux - cont)