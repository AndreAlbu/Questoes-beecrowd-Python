import math

a, b, c = input().split()

#Recebe valores inteiros#

a = int(a)
b = int(b)
c = int(c)

maior1 = (a + b + abs(a - b)) / 2.0

maior2 = (maior1 + c + abs(maior1 - c)) / 2.0

print("{} eh o maior".format(int(maior2)))
