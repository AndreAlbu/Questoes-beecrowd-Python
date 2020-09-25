n = int(input())

aux = 0.0

for i in range(n):

    soma = 0.0

    codigo, qtd = map(int, input().split())

    if(codigo == 1001):

        soma = qtd * 1.50

        aux = aux + soma

    elif(codigo == 1002):

        soma = qtd * 2.50

        aux = aux + soma

    elif(codigo == 1003):

        soma = qtd * 3.50

        aux = aux + soma

    elif(codigo == 1004):

        soma = qtd * 4.50

        aux = aux + soma

    elif(codigo == 1005):

        soma = qtd * 5.50

        aux = aux + soma

print("{:.2f}".format(aux))