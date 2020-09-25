import math

A = int(input())
B = int(input())

resto = math.sqrt(A) % math.sqrt(B)

c = int(resto)

print(c+1)