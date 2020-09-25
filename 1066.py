i = 1

coutPar      = 0
coutImpar    = 0
coutPositivo = 0
coutNegativo = 0

while(i < 6):

    numero = int(input())

    if(numero % 2 == 0):

        coutPar = coutPar + 1

    else:

        coutImpar = coutImpar + 1


    if(numero > 0):

        coutPositivo = coutPositivo + 1

    elif(numero < 0):

        coutNegativo = coutNegativo + 1


    i = i + 1

print("{} valor(es) par(es)".format(coutPar))
print("{} valor(es) impar(es)".format(coutImpar))
print("{} valor(es) positivo(s)".format(coutPositivo))
print("{} valor(es) negativo(s)".format(coutNegativo))