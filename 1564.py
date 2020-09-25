while(1):

    try:

        a = int(input())

        if(a == 0):

            print("vai ter copa!")

        else:

            print("vai ter duas!")

    except EOFError:

        break

