n = int(input())

for i in range(n):

    num = input()

    led = 0

    for k in range(0, len(num)):

        if(num[k] == '1'):

            led = led + 2

        elif(num[k] == '2'):

            led = led + 5

        elif(num[k] == '3'):

            led = led + 5

        elif(num[k] == '4'):

            led = led + 4

        elif(num[k] == '5'):

            led = led + 5

        elif(num[k] == '6'):

            led = led + 6

        elif(num[k] == '7'):

            led = led + 3

        elif(num[k] == '8'):

            led = led + 7

        elif(num[k] == '9'):

            led = led + 6

        elif(num[k] == '0'):

            led = led + 6

    print("{} leds".format(led))