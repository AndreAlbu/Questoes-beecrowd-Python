caso = 1
while True:
    try: 
        n = input()
        lista = input().split()
        if caso>1:
            print()
        total = 0
        f = 0
        m = 0
        for i in range(0,len(lista),2):
            if lista[i] == n:
                total+=1
                if lista[i+1] == "F":
                    f+=1
                else:
                    m+=1
        print("Caso {}:".format(caso))
        print("Pares Iguais:", total)
        print("F:", f)
        print("M:", m)
        caso+=1
    except EOFError:
        break       