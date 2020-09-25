def euclides(a, b):

    if(b == 0):

        return a

    else:

        return euclides(b, a % b)

N = int(input())

for i in range(N):

    a, b = input().split()

    a = int(a)
    b = int(b)

    print("{}".format(euclides(a, b)))