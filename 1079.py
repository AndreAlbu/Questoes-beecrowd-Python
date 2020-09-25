n = int(input())

for i in range(n):

    media = 0.0

    num1, num2, num3 = map(float, input().split())

    media = (num1 * 2 + num2 * 3 + num3 * 5) / 10.0

    print("{0:.1f}".format(media))