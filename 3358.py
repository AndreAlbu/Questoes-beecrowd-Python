n = int(input())
for i in range(n):
    sobren = input()
    sobren = sobren.lower()
    t3 = 0
    for j in range(len(sobren)):
        if sobren[j] != 'a' and sobren[j] != 'e' and sobren[j] != 'i' and sobren[j] != 'o' and sobren[j] != 'u':
            t3 += 1
        else:
            t3 = 0
        if t3 == 3:
            print(sobren.capitalize(), "nao eh facil")
            break
    if t3 < 3:
        print(sobren.capitalize(), "eh facil")
