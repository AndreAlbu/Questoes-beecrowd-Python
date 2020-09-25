n = int(input())

while(n != 0):

    respostaErradas = [ ]
    respostaCorretas = [ ]

    somaTempo = cont = contErrada = 0

    contErradas = 0

    for i in range(n):

        identificador, tempo, resposta = input().split()

        tempo = int(tempo)

        if(resposta == 'incorrect'):

            respostaErradas.append(identificador)

        elif(resposta == 'correct'):

            cont = cont + 1

            somaTempo = somaTempo + tempo

            respostaCorretas.append(identificador)

    for k in respostaErradas:

        if k in respostaCorretas:

            contErradas = contErradas + 1

    contErradas = contErradas * 20

    if(cont == 0):

        contErradas = 0

    print("{} {}".format(cont, somaTempo + contErradas))

    n = int(input())
