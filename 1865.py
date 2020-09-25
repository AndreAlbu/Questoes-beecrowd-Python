qtd = int(input())

i = 0

while(i < qtd):

    heroi, forca = input().split()

    heroi = str(heroi)

    forca = int(forca)

    if(heroi == "Thor"):

        print("Y")

    else:

        print("N")

    i = i + 1