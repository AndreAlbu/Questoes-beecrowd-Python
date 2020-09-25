import math
n = int(input())

for i in range(n):

    x, y = map(int, input().split())

    rafael = math.pow(3 * x, 2) + math.pow(y, 2)

    beto   = 2 * math.pow(x, 2) + math.pow(5 * y, 2)

    carlos = -100 * x + math.pow(y, 3)

    if(rafael > beto and rafael > carlos):

        print("Rafael ganhou")

    elif(beto > rafael and beto > carlos):

        print("Beto ganhou")

    elif(carlos > rafael and carlos > beto):

        print("Carlos ganhou")