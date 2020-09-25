i = 0

soma = 0

cout = 0

while(i < 6):

    numero = float(input())

    if(numero > 0):

        cout = cout + 1

        soma = soma + numero

    i = i + 1

media = soma / cout

print("{} valores positivos".format(cout))
print("{0:.1f}".format(media))