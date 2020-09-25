while(True):

    try:

        papagaio = input()

        if(papagaio == 'esquerda'):

            print("ingles")

        elif(papagaio == 'direita'):

            print("frances")

        elif(papagaio == 'nenhuma'):

            print("portugues")

        else:

            print("caiu")

    except EOFError:

        break