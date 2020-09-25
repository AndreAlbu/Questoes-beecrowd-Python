while(True):

    try:

        b, u = map(int, input().split())

        if(b > u):

            cal = b - u

            print(cal - 1)

        elif(b < u):

            cal = b - u

            cal = cal + 1

            if(cal < 0):

                print(cal *  -1)

            else:

                print(cal)

        else:

            print(0)

    except EOFError:

        break