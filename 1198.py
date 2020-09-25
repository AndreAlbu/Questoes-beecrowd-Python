while(True):

    try:

        hashmat, opnente = map(int, input().split())

        if(hashmat > opnente):

            print(hashmat - opnente)

        elif(hashmat < opnente):

            print(opnente - hashmat)

        else:

            print(0)

    except EOFError:

        break

