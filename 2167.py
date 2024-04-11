qtdEntrada = int(input(""))

lista = [int(x) for x in input("").split(" ")]

controle = -1

for i in range(len(lista)):
    if i == 0:
        anterior = lista[i]
    else:
        anterior = lista[i - 1]

    if lista[i] < anterior and controle == -1:
        controle = i

print(controle + 1)
