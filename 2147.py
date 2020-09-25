n = int(input())

for i in range(n):

    palavra = input()

    T = len(palavra)

    T = T / 100.00

    print("{0:.2f}".format(T))
