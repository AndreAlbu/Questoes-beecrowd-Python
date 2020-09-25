casos = int(input())

while(casos != 0):

    cout = 0

    for i in range(1, casos+1):

        cout = i * i + cout

    print(cout)

    casos = int(input())