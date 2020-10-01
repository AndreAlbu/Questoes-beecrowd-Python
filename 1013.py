import math

a, b, c = input().split()

#Recebe valores inteiros#

a = int(a)
b = int(b)
c = int(c)
d = int(d)

maior1 = ((a + b + abs(a - b)) / 2)

maior2 = ((maior1 + c + abs(maior1 - c)) / 2)

print("{} eh o maior".format(int(maior2)))
