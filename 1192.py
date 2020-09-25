n = int(input())

for i in range(n):

    entrada = input()

    letra    = entrada[1]
    primeiro = int(entrada[0])
    segundo  = int(entrada[2])

    if(primeiro == segundo):

        produto = primeiro * segundo

        print(produto)
    
    elif(letra.isupper()):

        subtracao = segundo - primeiro

        print(subtracao)

    elif(letra.islower()):

        soma = primeiro + segundo

        print(soma)
 