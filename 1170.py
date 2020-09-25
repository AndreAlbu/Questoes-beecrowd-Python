n = int(input())

for i in range(n):

    num = float(input())

    contDias = 0

    while(num / 2 > 1):

        contDias = contDias + 1

        num = num / 2

    print("{} dias".format(contDias + 1))