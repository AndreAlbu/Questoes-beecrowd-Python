partidas = int(input())

for i in range(partidas):

    golTime11, carctere, golTime12 = input().split()
    golTime22, carctere, golTime21 = input().split()

    Partida1pontosTime1 = 0
    Partida1pontosTime2 = 0

    Partida2pontosTime1 = 0
    Partida2pontosTime2 = 0

    somaGol1 = 0
    somaGol2 = 0

#Primeira partida
    golTime11 = int(golTime11)
    golTime12 = int(golTime12)

#Segunda partida

    golTime21 = int(golTime21)
    golTime22 = int(golTime22)

    somaGol1 = golTime11 + golTime21
    somaGol2 = golTime22 + golTime12

#Pontos da primeira partida

    if(golTime11 > golTime12):

        Partida1pontosTime1 = Partida1pontosTime1 + 3

    elif(golTime11 < golTime12):

        Partida1pontosTime2 = Partida1pontosTime2 + 3

    else:

        Partida1pontosTime1 =  Partida1pontosTime1 + 1
        Partida1pontosTime2 =  Partida1pontosTime2 + 1

#Pontos da segunda partida

    if(golTime21 > golTime22):

        Partida2pontosTime1 = Partida2pontosTime1 + 3

    elif(golTime21 < golTime22):

        Partida2pontosTime2 = Partida2pontosTime2 + 3

    else:

        Partida2pontosTime1 = Partida2pontosTime1 + 1
        Partida2pontosTime2 = Partida2pontosTime2 + 1

    somaTime1 = Partida1pontosTime1 + Partida2pontosTime1

    somaTime2 = Partida1pontosTime2 + Partida2pontosTime2

    #Condições para verificar que ganhou

    if(somaTime1 == somaTime2):

        if(golTime11 == golTime22 and golTime12 == golTime21):

            print("Penaltis")

        elif(golTime11 == golTime22 and golTime12 < golTime21):

            print("Time 1")

        elif(golTime11 == golTime22 and golTime12 > golTime21):

            print("Time 2")

        elif(somaGol1 > somaGol2):

            print("Time 1")

        elif(somaGol1 < somaGol2):

            print("Time 2")

        elif(somaGol1 == somaGol2):

            if(golTime12 > golTime21):

                print("Time 2")

            else:

                print("Time 1")

    elif(somaTime1 > somaTime2):

        print("Time 1")

    else:

        print("Time 2")