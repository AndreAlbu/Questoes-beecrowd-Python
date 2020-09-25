vetor = []

i = 1

while(i <= 100):

    valor = int(input())

    vetor.append(valor)

    i = i + 1

print(max(vetor))
print(vetor.index(max(vetor)) + 1)