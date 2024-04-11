maior = 0
palavraMaior = ""
palavra = ""

while palavra != "0":
    saida = ""

    palavra = input("").split(" ")

    if palavra[0] == "0":
        break

    tamanhoPalavra = len(palavra)

    for cada in range(tamanhoPalavra):
        tam = len(palavra[cada])

        if tam >= maior:
            maior = tam
            palavraMaior = palavra[cada]

        if cada == tamanhoPalavra - 1:
            saida += str(tam)

        else:
            saida += str(tam) + "-"

    print(saida)

print("\nThe biggest word:", palavraMaior.replace(" ", ""))
