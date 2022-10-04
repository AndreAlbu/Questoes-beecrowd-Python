numero = int(input(""))

lista = []

for i in range(numero):

    aux = int(input(""))

    lista.append(aux)



i = 0

while(i < numero):

    print("resposta {}: {}".format(i+1, lista[i]))

    i = i + 1
