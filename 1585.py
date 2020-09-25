n = int(input())

for i in range(n):

    x, y = map(int, input().split())

    pipa = x * y / 2

    print("{} cm2".format(int(pipa)))