f = [362880, 40320, 5040, 720, 120, 24, 6, 2, 1]

n = int(input())
c = 0

for i in f:

    c = c + int(n / i)
    n = n % i

print(c)