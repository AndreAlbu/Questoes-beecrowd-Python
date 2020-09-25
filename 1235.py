n = int(input())

for i in range(n):

    parte1 = [ ]
    parte2 = [ ]
    palavra = [ ]
    final = ""

    palavra1 = input()

    palavra1.replace(" ", "")

    for k in range(len(palavra1)):

        palavra.append(palavra1[k])

    for i in range(int(len(palavra)/2)):

        parte1.append(palavra1[i])

        palavra.remove(palavra1[i])

    for i in range(len(palavra)):

        parte2.append(palavra[i])


    parte1[::-1]
    parte2[::-1]

    final = parte2 + parte1

    mostra = ""

    print(mostra.join(final[::-1]))