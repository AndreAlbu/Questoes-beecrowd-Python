n = int(input())

for i in range(n):

    palavra = input()

    if(len(palavra) > 3):

        print(3)

    else:

        cout = 0

        if(palavra[0:1] == 'o'):

            cout = cout + 1

        if(palavra[1:2] == 'n'):

            cout = cout + 1

        if(palavra[2:3] == 'e'):

            cout = cout + 1

        if(cout >= 2):

            print(1)
            
        else:

            print(2)