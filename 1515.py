n = int(input())

menor = 0

while(n != 0):

    for i in range(n):

        planetas, anoEnvio, tempo = input().split()

        anoEnvio = int(anoEnvio)
        tempo    = int(tempo)

        enviado = anoEnvio - tempo

        if(i == 0):

            menor = enviado
            planeta = planetas


        if(enviado < menor):

            menor = enviado
            planeta = planetas
            

    print(planeta)

    n = int(input())