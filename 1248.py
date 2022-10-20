n = int(input())

for i in range(n):
    alim = input()
    cafe = input()
    almo = input()
    almo += cafe
    for j in range(len(almo)):
        if almo[j] not in alim:
            alim = ("CHEATER")
            break
        else:
            alim = alim.replace(almo[j], '')
    if alim == "CHEATER":
        print("CHEATER")
    else:
        alim = sorted(alim)
        alim = ''.join(alim)
        print(alim)
