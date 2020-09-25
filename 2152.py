n = int(input())

for i in range(n):

    h, m, o = map(int, input().split())

    if(h < 10):
    
        h = str(h)

        h = '0' + h

    if(m < 10):

        m = str(m)

        m = '0' + m

    if(o == 1):

        print("{}:{} - A porta abriu!".format(h, m))

    elif(o == 0):

        print("{}:{} - A porta fechou!".format(h, m))