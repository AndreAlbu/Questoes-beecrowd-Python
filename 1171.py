n = int(input())
lista = []
for i in range(n):
    num = int(input())
    lista.append(num)
    
lista.sort()
while lista != []:
    n = lista.count(lista[0])
    print("{} aparece {} vez(es)".format(lista[0], n))
    for i in range(n):
        lista.remove(lista[0])
    
    