palavra = input().split()
while palavra[0] != '*':
    i = 0
    tipo = "Y"
    while i < len(palavra):
        if palavra[i][0].lower() != palavra[0][0].lower():
            tipo = "N"
            break
        i+=1
    print(tipo)
    palavra = input().split()