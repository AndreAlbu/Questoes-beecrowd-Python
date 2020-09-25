while(True):

    try:

        n, m = map(int, input().split())

        cout = 0

        i = n

        for i in range(n, m+1):

            if(len(set(list(str(i)))) == len(str(i))):

                cout = cout + 1

        print(cout)


    except EOFError:

        break