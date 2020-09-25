while(True):

    try:

        cpf = input()

        d1 = int(cpf[0])
        d2 = int(cpf[1])
        d3 = int(cpf[2])
        d4 = int(cpf[4])
        d5 = int(cpf[5])
        d6 = int(cpf[6])
        d7 = int(cpf[8])
        d8 = int(cpf[9])
        d9 = int(cpf[10])
        d10 = int(cpf[12])
        d11 = int(cpf[13])

        b1 = d1 * 1 + d2 * 2 + d3 * 3 + d4 * 4 + d5 * 5 + d6 * 6 + d7 * 7 + d8 * 8 + d9 * 9

        b1 = b1 % 11

        b1 = int(b1)

        if(b1 == 10):

            b1 = 0

        b2 = d1 * 9 + d2 * 8 + d3 * 7 + d4 * 6 + d5 * 5 + d6 * 4 + d7 * 3 + d8 * 2 + d9 * 1

        b2 = b2 % 11

        b2 = int(b2)

        if(b2 == 10):

            b2 = 0

        if(b1 == d10 and b2 == d11):

            print("CPF valido")

        else:

            print("CPF invalido")

    except EOFError:

        break