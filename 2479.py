totalCrianca = int(input())

nomes = [ ]

coutBom = coutMal = 0

for i in range(totalCrianca):

    comportamento, nomeCrianca = input().split()

    nomes.append(nomeCrianca)

    if(comportamento == '+'):

        coutBom = coutBom + 1

    else:

        coutMal = coutMal + 1

nomes.sort()

for i in range(len(nomes)):

    print("{}".format(nomes[i]))

print("Se comportaram: {} | Nao se comportaram: {}".format(coutBom, coutMal))