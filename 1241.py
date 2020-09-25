contador = 0

vezes = int(input())

while contador < vezes:

    texto = str(input()).split()

    if texto[1] == texto[0][len(texto[0]) - len(texto[1]):]:
        print("encaixa")
    else:
        print("nao encaixa")

    contador += 1