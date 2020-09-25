n = int(input())

sapo = 0
coelho = 0
rato = 0
total = 0

for i in range(n):

    quantia, tipo = input().split()

    quantia = int(quantia)

    total = total + quantia

    if(tipo == 'R'):

        rato = rato + quantia

    elif(tipo == 'S'):

        sapo = sapo + quantia

    elif(tipo == 'C'):

        coelho = coelho + quantia

percentualCoelho = coelho / total   * 100.00
percentualRato   = rato  /  total   * 100.00
percentualSapo   = sapo /   total   * 100.00

print("Total: {} cobaias".format(total))
print("Total de coelhos: {}".format(coelho))
print("Total de ratos: {}".format(rato))
print("Total de sapos: {}".format(sapo))
print("Percentual de coelhos: {0:.2f} %".format(percentualCoelho))
print("Percentual de ratos: {0:.2f} %".format(percentualRato))
print("Percentual de sapos: {0:.2f} %".format(percentualSapo))