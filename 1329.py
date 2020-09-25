n = int(input())

while(n != 0):

    jogadas = list(map(int, input().split()))

    contMary = contJonh = 0

    for i in range(len(jogadas)):

        if(jogadas[i] == 0):

            contMary = contMary + 1

        else:

            contJonh = contJonh + 1

    print("Mary won {} times and John won {} times".format(contMary, contJonh))

    n = int(input())