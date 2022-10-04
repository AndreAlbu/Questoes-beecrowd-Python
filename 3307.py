qtd = int(input())

for i in range(qtd):

    valor = int(input())

    r = valor / 12.56

    r = r ** 0.5

    if(r < 12):

        valor = valor * 0.09
        print("vermelho = R$ {:.2f}".format(valor))

    elif(r >= 12 and r <= 15):

        valor = valor * 0.07
        print("azul = R$ {:.2f}".format(valor))

    else:

        valor = valor * 0.05
        print("amarelo = R$ {:.2f}".format(valor))