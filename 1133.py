inf = int(input())
sup = int(input())

if inf > sup:
    inf, sup = sup, inf

for i in range(inf+1, sup):
    if i % 5 == 2 or i % 5 == 3:
        print(i)
