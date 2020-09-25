opinioes = int(input())

respostas = list(map(int, input().split()))

contra = gostam = 0

for i in range(len(respostas)):

    if(respostas[i] == 0):

        gostam = gostam + 1

    else:

        contra = contra + 1

if(contra >= gostam):

    print("N")

else:

    print("Y")
