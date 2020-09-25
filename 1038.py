a, b = input().split()

a = int(a)
b = int(b)

if(a == 1):

    qtd = b * 4.00

elif(a == 2):

    qtd = b * 4.50

elif(a == 3):

    qtd = b * 5.00

elif(a == 4):

    qtd = b * 2.00

elif(a == 5):

    qtd = b * 1.50

print("Total: R$ {0:.2f}".format(qtd))