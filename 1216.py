soma = cont = 0

while(True):

    try:

        nome = input()

        distancia = int(input())

        soma = soma + distancia

        cont = cont + 1

    except EOFError:

        print("{0:.1f}".format(soma/cont))

        break