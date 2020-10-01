vet = []

i = 1

while(i <= 100):

    valor = int(input())

    vet.append(valor)

    i = i + 1

print(max(vet))
print(vet.index(max(vet)) + 1)
