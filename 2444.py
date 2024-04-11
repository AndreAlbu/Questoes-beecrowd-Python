entrada = input("").split()

volume = int(entrada[0])
modificacoes  = int(entrada[1])

lista = [int(x) for x in input("").split(" ")]

for i in lista:

    volume += i

    if(volume > 100): 

        volume = 100

    elif(volume < 0):

        volume = 0

print(volume)

