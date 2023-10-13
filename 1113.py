while True:
    dupla = input().split()
    x, y = int(dupla[0]), int(dupla[1])
    
    if x < y: 
        print('Crescente')
    elif x > y:
        print('Decrescente')
    else:
        break
