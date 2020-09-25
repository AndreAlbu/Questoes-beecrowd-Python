n = int(input())

while(n != 0):

    lista = [int(j) for j in input().split()]

    maior = lista[0]

    for i in range(len(lista)):

        if(maior == max(lista)):

            j = 0

        else:

            j = lista.index(max(lista))

    for i in range(len(lista)):

        if(i == j):

            lista[i] = 0

    suspeito = lista.index(max(lista)) + 1

    print(suspeito)

    n = int(input())