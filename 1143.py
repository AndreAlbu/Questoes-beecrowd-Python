import math

x = int(input())

i = 1

print("{} {} {}".format(i, i, i))

i = 2

while(i <= x):

    quadrado = int(math.pow(i, 2))

    cubo = int(math.pow(i, 3))

    print("{} {} {}".format(i, quadrado, cubo))

    i = i + 1