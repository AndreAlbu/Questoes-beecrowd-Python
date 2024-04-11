def converte(letra):

    numero = -1

    if(letra == "a" or letra == "k" or letra == "u" or letra == "G" or letra == "Q"):

        numero = 0

    elif(letra == "b" or letra == "l" or letra == "v" or letra == "I" or letra == "S"):

        numero = 1

    elif(letra == "c" or letra == "m" or letra == "w" or letra == "E" or letra == "O" or letra == "Y"):

        numero = 2

    elif(letra == "d" or letra == "n" or letra == "x" or letra == "F" or letra == "P" or letra == "Z"):

        numero = 3

    elif(letra == "e" or letra == "o" or letra == "y" or letra == "J" or letra == "T"):

        numero = 4

    elif(letra == "f" or letra == "p" or letra == "z" or letra == "D" or letra == "N" or letra == "X"):

        numero = 5

    elif(letra == "g" or letra == "q" or letra == "A" or letra == "K" or letra == "U"):

        numero = 6

    elif(letra == "h" or letra == "r" or letra == "C" or letra == "M" or letra == "W"):

        numero = 7

    elif(letra == "i" or letra == "s" or letra == "B" or letra == "L" or letra == "V"):

        numero = 8

    elif(letra == "j" or letra == "t" or letra == "H" or letra == "R"):

        numero = 9

    return str(numero)

qtdFrases = (int(input("")))

for i in range(qtdFrases):

    criptografia = ""

    frase = input("")

    frase = frase.replace(" ", "")

    for l in frase:

        criptografia += converte(l)

    print("{0:.12}".format(criptografia))