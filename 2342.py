maiorNumero = int(input())

num1, sinal, num2 = input().split()

num1 = int(num1)
num2 = int(num2)

soma = mult = 0

if(sinal == '+'):

    soma = num1 + num2

    if(soma <= maiorNumero):

        print("OK")

    else:

        print("OVERFLOW")

elif(sinal == '*'):

    mult = num1 * num2

    if(mult <= maiorNumero):

        print("OK")

    else:

        print("OVERFLOW")
