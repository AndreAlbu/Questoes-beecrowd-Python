num = int(input())

soma2 = 0
soma3 = 0
soma4 = 0
soma5 = 0

lista = [int(i) for i in input().split()]

for i in range(num):

    if(lista[i] % 2 == 0):

        soma2 = soma2 + 1
    
    if(lista[i] % 3 == 0):

        soma3 = soma3 + 1

    if(lista[i] % 4 == 0):

        soma4 = soma4 + 1

    if(lista[i] % 5 == 0):

        soma5 = soma5 + 1

print("{} Multiplo(s) de 2".format(soma2))
print("{} Multiplo(s) de 3".format(soma3))
print("{} Multiplo(s) de 4".format(soma4))
print("{} Multiplo(s) de 5".format(soma5))

