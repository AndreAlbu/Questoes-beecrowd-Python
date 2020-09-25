n = int(input())

dentro = fora = 0

for i in range(n):

    numero = int(input())

    if(numero >= 10 and numero <= 20):

        dentro = dentro + 1

    else:

        fora = fora + 1

print("{} in".format(dentro))
print("{} out".format(fora))