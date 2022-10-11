n = int(input())
notas = [100, 50, 20, 10, 5, 2, 1]

print(n)

for i in range(len(notas)):
    if (n >= notas[i]):
        print("%d nota(s) de R$ %d,00"%(n//notas[i], notas[i]))
        n = n%notas[i]
    else:
        print("0 nota(s) de R$ %d,00"%(notas[i]))