n = int(input())

numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

letra = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y', 'X', 'Z']

for i in range(n):

    placa = input()

    letras = [ ]

    num = [ ]

    caract = verifica = pos =  veri = 0

    for k in range(len(placa)):

        if(placa[k] != '-'):

            letras.append(placa[k])

        else:

            caract = 1
            pos = k
            break
            
    for o in range(pos, len(placa)):

        num.append(placa[o])

    num.remove(num[0])

    for l in range(len(letras)):

        if(letras[l] in letra):

            verifica = 1

        else:

            verifica = 0
            break

    for p in range(len(num)):

        if(num[p] in numeros):

            veri = 1

        else:

            veri = 0
            break



    if(len(placa) != 8):

        print("FAILURE")

    elif(verifica == 0):

        print("FAILURE")

    elif(veri == 0):

        print("FAILURE")

    elif(caract == 0):

        print("FAILURE")

    elif(placa[7] == '1' or placa[7] == '2'):

        print("MONDAY")

    elif(placa[7] == '3' or placa[7] == '4'):

        print("TUESDAY")

    elif(placa[7] == '5' or placa[7] == '6'):

        print("WEDNESDAY")

    elif(placa[7] == '7' or placa[7] == '8'):

        print("THURSDAY")

    elif(placa[7] == '9' or placa[7] == '0'):

        print("FRIDAY")

    else:

        print("FAILURE")