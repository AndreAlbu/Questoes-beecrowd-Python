def forma_nome(nome, sobrenome):

    junta_nome1 = [ ]

    inicio1 = 0

    for n in range(2, len(nome) + 2, 2):

        parte1 = nome[inicio1: inicio1 + 2]

        junta_nome1.insert(inicio1, parte1)

        inicio1 = n

    inicio2 = 0

    for s in range(2, len(sobrenome) + 2, 2):

        parte2 = sobrenome[inicio2: inicio2 + 2]

        junta_nome1.insert(inicio2 + 1, parte2)

        inicio2 = s

    nome_final = ''.join(junta_nome1)

    return nome_final

qtdNome = int(input(""))

for i in range(1, qtdNome + 1):

    nome = input("")
    sobrenome = input("")

    nome_final = forma_nome(nome, sobrenome)

    print(nome_final)