notas = input()

i = 0

contZero = soma = tamanho = 0

notasCorretas = [ ]

notasCorretasNumeros = [ ]

while(i < len(notas)):

    if(len(notas) == 1):

        notasCorretas.append(notas[i])
        
        break

    elif(notas[i] != '0'):

        notasCorretas.append(notas[i])

        i = i + 1

    else:

        contZero = contZero + 1

        i = i + 1


for j in range(len(notasCorretas)):

    notasCorretasNumeros.append(int(notasCorretas[j]))

soma = sum(notasCorretasNumeros)

tamanho = len(notasCorretasNumeros)

if(contZero > 0):

    soma = soma - contZero

soma = soma + 10 * contZero

media = soma / tamanho

print('{0:.2f}'.format(media))
