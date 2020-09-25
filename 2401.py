n = int(input())

calculadora = 1

for i in range(n):

    valor, operacao = input().split()

    valor = int(valor)

    if(operacao == '/'):

        calculadora = calculadora / valor

    else:

        calculadora = calculadora * valor


print("{0:.0f}".format(calculadora))