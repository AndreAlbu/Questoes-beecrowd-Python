n, k = map(int, input().split())

cout = 0

while(n != 0 and k != 0):

    lista = [int(i) for i in input().split()]

    for j in range(n):

        if(lista[j] in [j+1]):

            cout = cout + 1

        else:

            cout = 0

    print(cout)


    n, k = map(int, input().split())

