while(True):

    try:

        num = int(input())

        cout = 0

        i = 1

        while(i % num != 0):

            i = (10 * i + 1) % num

            cout = cout + 1

        print(cout + 1)

    except EOFError:

        break