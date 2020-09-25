m, n = map(int, input().split())

while(m != 0 and n != 0):

    soma = 0

    soma = m + n

    semZero = str(soma)

    mostrar = semZero.replace('0','')

    print(mostrar)

    m, n = map(int, input().split())