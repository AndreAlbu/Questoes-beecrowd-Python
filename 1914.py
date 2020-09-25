t = int(input())

i = 0

while(i < t):

    amarelinha = input().split()

    jogador1 = amarelinha[0]
    escolha1 = amarelinha[1]

    jogador2 = amarelinha[2]
    escolha2 = amarelinha[3]

    num1, num2 = map(int, input().split())

    if((num1 + num2) % 2 == 0 and escolha1 == 'PAR'):

        print(jogador1)

    elif((num1 + num2) % 2 == 0 and escolha2 == 'PAR'):

        print(jogador2)

    elif((num1 + num2) % 2 != 0 and escolha1 == 'IMPAR'):

        print(jogador1)

    elif((num1 + num2) % 2 != 0 and escolha2 == 'IMPAR'):

        print(jogador2)

    escolha1 = escolha2 = 0
    num1 = num2 = 0
        
    i = i + 1