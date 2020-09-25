n = int(input())

final = ""

for i in range(n):

    palavra1, palavra2 = map(str, input().split())

    j = 0

    while(j < len(palavra1) and j < len(palavra2)):

        final = final + palavra1[j] + palavra2[j]

        j = j + 1

    if(j < len(palavra1)):

        final = final + palavra1[j:]

    if(j < len(palavra2)):

        final = final + palavra2[j:]

    print(final)

    palavra1 = palavra2 = final = ""