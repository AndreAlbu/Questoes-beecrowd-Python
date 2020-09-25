a, b, c, d = input().split()

a = float(a)
b = float(b)
c = float(c)
d = float(d)

media = (a * 2 + b * 3 + c * 4 + d * 1) / 10.0

if(media >= 7.0):

    print("Media: {0:.1f}".format(media))
    print("Aluno aprovado.")

elif(media >= 5.0 and media <= 6.9):

    print("Media: {0:.1f}".format(media))
    print("Aluno em exame.")
    notaExame = float(input())
    print("Nota do exame: {0:.1f}".format(notaExame))

    notaFinal = (media + notaExame) / 2

    if(notaFinal >= 5.0):

        print("Aluno aprovado.")
        print("Media final: {0:.1f}".format(notaFinal))

    else:

        print("Aluno reprovado.")
        print("Media final: {0:.1f}".format(notaFinal))

else:

    print("Media: {0:.1f}".format(media))
    print("Aluno reprovado.")

