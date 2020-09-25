while(True):

    try:

        n, m = input().split()
        
        soma = 0

        for i in range(len(m)):

            soma = soma + int(m[i])

        if(soma % 3 == 0):

            print("{} sim".format(soma))

        else:

            print("{} nao".format(soma))

    except EOFError:

        break
