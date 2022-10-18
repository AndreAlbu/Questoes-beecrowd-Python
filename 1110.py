while True:
    num = int(input())
    lista = list(range(1,num+1))
    lista = lista[::-1]
    descarte = []
    if num == 0:
        break
    elif num > 1:
        for i in range(num-1):
            descarte.append(lista.pop(-1))
            lista.insert(0, lista[-1])
            lista.pop(-1)
        print("Discarded cards: ", end="")
        for i in range(len(descarte)-1):
            print(descarte[i], end="")
            print(", ", end="")
        print(descarte[-1], end="")
        print()
    else:
        print("Discarded cards:", end="")
        print() 
    print("Remaining card:", lista[0])
