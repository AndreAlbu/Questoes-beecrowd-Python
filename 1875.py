def numeroGols(t1, t2):
    gol = 0

    if t1 == "B":
        if t2 == "R":
            gol += 2

        else:
            gol += 1

    elif t1 == "R":
        if t2 == "G":
            gol += 2

        else:
            gol += 1

    elif t1 == "G":
        if t2 == "B":
            gol += 2

        else:
            gol += 1

    return gol


qtdTeste = int(input(""))

for t in range(qtdTeste):
    blue = 0
    red = 0
    green = 0

    qtdGols = int(input(""))

    for g in range(qtdGols):
        gols = input("").split()

        fez = gols[0]
        lev = gols[1]

        partida = numeroGols(fez, lev)

        if fez == "B":
            blue += partida

        elif fez == "R":
            red += partida

        else:
            green += partida

    if red == green and green == blue:
        print("trempate")

    elif red > blue and red > green:
        print("red")

    elif blue > red and blue > green:
        print("blue")

    elif green > red and green > blue:
        print("green")

    elif red == green and green != blue:
        print("empate")

    elif red != green and green == blue:
        print("empate")

    elif red == blue and blue != green:
        print("empate")
