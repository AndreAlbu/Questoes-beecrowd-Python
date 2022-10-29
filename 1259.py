n = int(input())
par = []
impar = [] 

for i in range(n):
    valor = int(input())
    if(valor%2==0):
        par.append(valor)
    else:
        impar.append(valor)


par.sort()
impar.sort(reverse=True)

for i in par:
    print(i)
for i in impar:
    print(i)
