qtdEscritorios, escritorioSemana = map(int, input().split())

idEscritorios = list(map(int, input().split()))

outrosEscritorios = [ ]

for i in range(qtdEscritorios):

    escritorio = int(input())

    if(escritorio in idEscritorios or escritorio in outrosEscritorios):

        print(0)
        outrosEscritorios.append(escritorio)

    else:

        print(1)
        outrosEscritorios.append(escritorio)

int a=10
