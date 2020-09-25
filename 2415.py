tam = int(input())

consecutivos = list(map(int, input().split()))

soma = j = 1

for i in range(1, tam):

    if(consecutivos[i] == consecutivos[i-1]):

        soma = soma + 1

    else:

        if(soma > j):

            j = soma

        soma = 1

if(soma > j):

    j = soma

print(j)