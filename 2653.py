joias = []

soma = 0

while(True):
    try:

        entrada = input("")

        if(entrada not in joias):

            joias.append(entrada)

            soma += 1

    except EOFError:

        print(soma)

        break