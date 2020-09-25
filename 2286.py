n = int(input())

j = 1

while(n != 0):

    nomePar = input()
    nomeImp = input()

    soma = 0

    for i in range(n):

        par, impa = map(int, input().split())

        soma = par + impa

        if(i == 0):

            print("Teste {}".format(j))

        if(soma % 2 == 0):

            print(nomePar)

        else:

            print(nomeImp)

    print("")

    j = j + 1

    n = int(input())