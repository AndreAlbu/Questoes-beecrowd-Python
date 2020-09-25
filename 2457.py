letra = input()

texto = list(input().split())

totalPalavraTexto = len(texto)

cout = 0

for i in range(len(texto)):

    if(letra in texto[i]):

        cout = cout + 1


print("{0:.1f}".format(cout / totalPalavraTexto * 100.00))
