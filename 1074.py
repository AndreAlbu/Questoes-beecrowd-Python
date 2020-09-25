n = int(input())

i = 0

while(i < n):

    num = int(input())

    if(num > 0 and num % 2 == 0):

        print("EVEN POSITIVE")

    elif(num < 0 and num % 2 == 0):

        print("EVEN NEGATIVE")

    elif(num > 0 and num % 2 != 0):

        print("ODD POSITIVE")

    elif(num < 0 and num % 2 != 0):

        print("ODD NEGATIVE")

    else:

        print("NULL")

    i = i + 1
