corvo = input()

soma1 = i = 0

while(True):

    if(corvo == '--*'):

        soma1 = soma1 + 1

    elif(corvo == '*--'):

        soma1 = soma1 + 4

    elif(corvo == '-*-'):

        soma1 = soma1 + 2

    elif(corvo == '-**'):

        soma1 = soma1 + 3

    elif(corvo == '*-*'):

        soma1 = soma1 + 5

    elif(corvo == '**-'):

        soma1 = soma1 + 6

    elif(corvo == '***'):

        soma1 = soma1 + 7

    if(corvo == 'caw caw'):

        print(soma1)

        soma1 = 0

        i = i + 1

    if(i == 3):

        break

    corvo = input()