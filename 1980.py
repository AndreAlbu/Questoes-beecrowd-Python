s = input().strip()

while(s != '0'):

    tam = len(s)

    i = 1

    anagrama = 1

    while(i <= tam):

        anagrama = anagrama * i

        i = i + 1

    print(anagrama)

    s = input().strip()