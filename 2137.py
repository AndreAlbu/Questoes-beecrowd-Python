while(True):

    try:

        n = int(input())

        biblioteca = [ ]

        for i in range(n):

            codigo = input()

            biblioteca.append(codigo)

        biblioteca.sort()

        for j in range(n):

            print("{}".format(biblioteca[j]))

    except EOFError:

        break