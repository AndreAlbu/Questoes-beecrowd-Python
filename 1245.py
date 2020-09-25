while(True):

    try:

        ladoDireito = [ ]
        ladoEsquerdo = [ ]

        par = 0

        n = int(input())

        for i in range(n):

            tamBota, lado = input().split()

            tamBota = int(tamBota)

            if(lado == 'D'):

                ladoDireito.append(tamBota)

            if(lado == 'E'):

                ladoEsquerdo.append(tamBota)

        for j in ladoDireito:

            if j in ladoEsquerdo:

                par = par + 1

                ladoEsquerdo.remove(j)         
                
        print(par)

    except EOFError:

        break

    