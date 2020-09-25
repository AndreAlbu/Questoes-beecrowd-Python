T = 1
N = 1

veri = 0

while(T != 0):

    T, N = map(int, input().split())

    soma = 0

    for i in range(T):

        times, pontos = input().split()

        pontos = int(pontos)

        if(pontos == N):

            soma = soma + 1

        elif(pontos > N):

            soma = pontos - N

    if(soma == N):

        print(0)

    else:

        print(soma)

        