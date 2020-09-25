i = 1

cout = 0

while(i < 6):

    numero = int(input())

    if(numero % 2 == 0):

        cout = cout + 1

    i = i + 1

print("{} valores pares".format(cout))