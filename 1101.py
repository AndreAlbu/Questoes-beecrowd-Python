m, n = map(int, input().split())

while(m != 0 and n != 0 and m > 0 and n > 0):

    soma = 0

    if(m > n):

        for i in range(n, m + 1):

            print("{}".format(i), end = " ")

            soma = soma + i

        print("Sum={}".format(soma))

    elif(m < n):

        for i in range(m, n + 1):

            print("{}".format(i), end = " ")

            soma = soma + i

        print("Sum={}".format(soma))

    else:

        print("{} Sum={}".format(m, m))

    m, n = map(int, input().split())
