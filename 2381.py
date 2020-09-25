qtdNomes, numeroSorteado = map(int, input().split())

listaAlunos = [ ]

for i in range(qtdNomes):

    nomeAluno = input()

    listaAlunos.append(nomeAluno)


alunosOrdem = sorted(listaAlunos)


print(alunosOrdem[numeroSorteado-1])